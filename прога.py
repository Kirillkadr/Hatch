import re
from pygments import lex
from pygments.lexers import get_lexer_by_name
from pygments.token import Token, is_token_subtype
from typing import List, Dict, Tuple, Any

def load_code_from_markdown(filepath: str):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()

    match_pattern = re.compile(r'### match:\s*```(.*?)```', re.DOTALL)
    patch_pattern = re.compile(r'### patch\s*```(.*?)```', re.DOTALL)
    match = match_pattern.search(content)
    patch = patch_pattern.search(content)
    match_text = match.group(1).strip() if match else None
    patch_text = patch.group(1).strip() if patch else None

    # Ищем отступы перед >>> в match_text
    indentation = ''
    if match_text:
        lines = match_text.split('\n')
        for line in lines:
            if '>>>' in line:
                stripped_line = line.lstrip()
                if stripped_line:  # Если строка не пустая после удаления пробелов слева
                    indentation = line[:len(line) - len(stripped_line)]  # Все пробелы перед >>>
                break
    return match_text, patch_text, indentation


def detect_programming_language(filename):
    language_extensions = {
        '.py': 'Python',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.cs': 'C#',
        '.js': 'JavaScript',
        '.rb': 'Ruby',
        '.ts': 'TypeScript',
        '.go': 'Go',
        '.rs': 'Rust',
        '.kt': 'Kotlin',
        '.swift': 'Swift',
    }

    extension = '.' + filename.split('.')[-1].lower()

    return language_extensions.get(extension, 'Неизвестный язык')

def tokenize_code(code: str, language: str) -> List[Tuple]:
    try:
        lexer = get_lexer_by_name(language)
        tokens = []
        special_ops = {"...", ">>>", "<<<"}
        buffer = code

        while buffer:
            match = re.search(r'(\.\.\.|>>>|<<<)', buffer)
            if match:
                start = match.start()
                if start > 0:
                    part = buffer[:start]
                    tokens.extend(lex(part, lexer))
                tokens.append((Token.Operator, match.group()))
                buffer = buffer[match.end():]
            else:
                tokens.extend(lex(buffer, lexer))
                break

        return tokens
    except Exception as e:
        raise ValueError(f"Tokenization error: {str(e)}")

def source_to_tokenList(file_path: str, func, extra_param: str) -> List[List[Tuple]]:
    result_list = []
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            processed_string = remove_insignificant_tokens(func(line, extra_param), extra_param)
            result_list.append(processed_string)
    return result_list

def remove_insignificant_tokens(token_list: List[Tuple], language: str) -> List[Tuple]:
    filtered = []
    is_leading = True

    for token_type, token_value in token_list:
        if is_token_subtype(token_type, Token.Text.Whitespace) and token_value == '\n':
            continue
        if language.lower() == 'python':
            if is_token_subtype(token_type, Token.Text):
                if is_leading:
                    filtered.append((token_type, token_value))
            else:
                filtered.append((token_type, token_value))
                is_leading = False
        else:
            filtered.append((token_type, token_value))

    return filtered

def remove_in_tok_match(filepath: str, language: str) -> List[Tuple[str, List[Tuple]]]:
    match, _, _ = load_code_from_markdown(filepath)
    match = match.split('\n')
    token_list = []

    for mch in match:
        tokens = tokenize_code(mch, language)
        filtered_tokens = remove_insignificant_tokens(tokens, language)

        paren_level = 0
        cleaned_tokens = []
        for token_type, token_value in filtered_tokens:
            if token_type == Token.Punctuation and token_value == '(':
                paren_level += 1
                cleaned_tokens.append((token_type, token_value))
            elif token_type == Token.Punctuation and token_value == ')':
                paren_level -= 1
                cleaned_tokens.append((token_type, token_value))
            elif token_type == Token.Operator and token_value == '...' and paren_level > 0:
                continue
            else:
                cleaned_tokens.append((token_type, token_value))

        token_list.extend(cleaned_tokens)

    return group_tokens(token_list)

def group_tokens(tokens: List[Tuple]) -> List[Tuple[str, List[Tuple]]]:
    result = []
    current_operator = None
    current_group = []
    paren_level = 0

    for token in tokens:
        token_type, token_value = token
        if token_type == Token.Punctuation and token_value == '(':
            paren_level += 1
            current_group.append(token)
        elif token_type == Token.Punctuation and token_value == ')':
            paren_level -= 1
            current_group.append(token)
        elif is_token_subtype(token_type, Token.Operator) and token_value == '...' and paren_level == 0:
            if current_operator or current_group:
                result.append((current_operator, current_group))
            current_operator = token_value
            current_group = []
        elif is_token_subtype(token_type, Token.Operator) and token_value == '>>>':
            current_group.append(token)
        elif is_token_subtype(token_type, Token.Operator) and token_value == '<<<':
            continue
        else:
            current_group.append(token)

    if current_operator or current_group:
        result.append((current_operator, current_group))

    return result

def process_match_structure(match_structure: List[Tuple[str, List[Tuple]]]) -> None:
    tokens_after_ellipsis = []
    for operator, tokens in match_structure:
        if operator == '...':
            if tokens_after_ellipsis:
                print(f'Tokens after "...":')
                for token in tokens_after_ellipsis:
                    print(f'  {token}')
            tokens_after_ellipsis = tokens
        elif operator == '>>>':
            if tokens_after_ellipsis:
                print(f'Tokens after "...":')
                for token in tokens_after_ellipsis:
                    print(f'  {token}')
            tokens_after_ellipsis = []
            print(f'Encountered operator ">>>", stopping token collection.')
    if tokens_after_ellipsis:
        print(f'Tokens after "...":')
        for token in tokens_after_ellipsis:
            print(f'  {token}')
def find_matching_lines(match_structure: List[Tuple[str, List[Tuple]]], source_code_tokens: List[List[Tuple]]) -> List[str]:
    matched_lines = set()
    flat_tokens = []
    line_numbers = []

    for line_idx, line in enumerate(source_code_tokens):
        for token_info in line:
            token_type, token_value = token_info
            if not is_token_subtype(token_type, Token.Text):
                flat_tokens.append(token_info)
                line_numbers.append(line_idx + 1)

    for operator, tokens in match_structure:
        if operator != '...':
            continue

        match_tokens = [t for t in tokens if not is_token_subtype(t[0], Token.Text) and not (is_token_subtype(t[0], Token.Operator) and t[1] == '>>>')]
        if not match_tokens:
            continue

        match_idx = 0
        source_idx = 0
        start_line = None
        paren_level = 0

        while source_idx < len(flat_tokens) and match_idx < len(match_tokens):
            match_type, match_value = match_tokens[match_idx]
            source_type, source_value = flat_tokens[source_idx]

            if match_type == Token.Punctuation and match_value == '(':
                paren_level += 1
                if start_line is None:
                    start_line = line_numbers[source_idx]
                match_idx += 1
                source_idx += 1
            elif match_type == Token.Punctuation and match_value == ')':
                paren_level -= 1
                while source_idx < len(flat_tokens) and (flat_tokens[source_idx][0] != Token.Punctuation or flat_tokens[source_idx][1] != ')'):
                    source_idx += 1
                if source_idx < len(flat_tokens):
                    source_idx += 1
                match_idx += 1
            elif match_type == source_type and match_value == source_value:
                if start_line is None:
                    start_line = line_numbers[source_idx]
                match_idx += 1
                source_idx += 1
            elif paren_level > 0:
                source_idx += 1
            else:
                match_idx = 0
                source_idx += 1
                start_line = None
                paren_level = 0

            if match_idx == len(match_tokens) and start_line is not None:
                matched_lines.update(range(start_line, line_numbers[source_idx - 1] + 1))

        if match_idx == len(match_tokens) and start_line is not None:
            matched_lines.update(range(start_line, line_numbers[source_idx - 1] + 1))

    sorted_lines = sorted(matched_lines)
    ranges = []
    if not sorted_lines:
        return []

    start = sorted_lines[0]
    prev = start
    for curr in sorted_lines[1:] + [None]:
        if curr != prev + 1:
            if start == prev:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}-{prev}")
            start = curr
        prev = curr if curr is not None else prev

    return ranges

def check_ggg_in_lines(match_text: str, language: str) -> List[Dict[str, Any]]:
    lines = match_text.split('\n')
    ggg_count = 0
    results = []

    for line in lines:
        if not line.strip():
            continue

        tokens = tokenize_code(line.strip(), language)
        filtered_tokens = remove_insignificant_tokens(tokens, language)

        ggg_index = next((i for i, t in enumerate(filtered_tokens) if is_token_subtype(t[0], Token.Operator) and t[1] == '>>>'), -1)

        if ggg_index != -1:
            ggg_count += 1
            before_ggg = [t for t in filtered_tokens[:ggg_index] if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
            after_ggg = [t for t in filtered_tokens[ggg_index + 1:] if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]

            before_ellipsis = []
            after_ellipsis = []
            paren_level = 0
            ellipsis_found = False

            for token_type, token_value in after_ggg:
                if token_type == Token.Punctuation and token_value == '(':
                    paren_level += 1
                    if not ellipsis_found:
                        before_ellipsis.append((token_type, token_value))
                elif token_type == Token.Punctuation and token_value == ')':
                    paren_level -= 1
                    if paren_level == 0 and ellipsis_found:
                        after_ellipsis.append((token_type, token_value))
                    elif not ellipsis_found:
                        before_ellipsis.append((token_type, token_value))
                elif token_type == Token.Operator and token_value == '...' and paren_level > 0:
                    ellipsis_found = True
                elif not ellipsis_found:
                    before_ellipsis.append((token_type, token_value))
                elif ellipsis_found and paren_level == 0:
                    after_ellipsis.append((token_type, token_value))

            results.append({
                'operator_number': ggg_count,
                'before': before_ggg,
                'after': {'before_ellipsis': before_ellipsis, 'after_ellipsis': after_ellipsis}
            })

    return results

def find_tokens_in_source(ggg_data: List[Dict[str, Any]], source_tokens: List[List[Tuple]]) -> Dict:
    def search_token_group(before_group, after_group):
        if not before_group and not after_group:
            return []
        matched_lines = []
        for line_idx, line_tokens in enumerate(source_tokens):
            filtered_line = [t for t in line_tokens if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
            if len(filtered_line) < len(before_group) + len(after_group):
                continue
            for i in range(len(filtered_line) - len(before_group) - len(after_group) + 1):
                if filtered_line[i:i + len(before_group)] == before_group:
                    if not after_group:
                        matched_lines.append((line_idx + 1, i))
                        break
                    remaining_tokens = filtered_line[i + len(before_group):]
                    if len(remaining_tokens) >= len(after_group):
                        for j in range(len(remaining_tokens) - len(after_group) + 1):
                            if remaining_tokens[j:j + len(after_group)] == after_group:
                                matched_lines.append((line_idx + 1, i))
                                break
                        if matched_lines and matched_lines[-1][0] == line_idx + 1:
                            break
        return matched_lines

    results = {}
    for entry in ggg_data:
        operator_num = entry['operator_number']
        before_ggg = entry['before']
        after_ggg = entry['after']
        before_ellipsis = after_ggg['before_ellipsis']
        after_ellipsis = after_ggg['after_ellipsis']

        results[operator_num] = {}
        if before_ggg:
            before_lines = search_token_group(before_ggg, [])
            results[operator_num]['before_lines'] = before_lines
            results[operator_num]['before_group'] = before_ggg
        if before_ellipsis or after_ellipsis:
            after_lines = search_token_group(before_ellipsis, after_ellipsis)
            results[operator_num]['after_lines'] = after_lines
            results[operator_num]['after_group'] = before_ellipsis + after_ellipsis

    return results
def get_token_positions(line: str, line_tokens: List[Tuple]) -> List[Tuple[int, int, Tuple]]:
    positions = []
    current_pos = 0
    print(f"Обработка строки: '{line}'")
    for token_type, token_value in line_tokens:
        try:
            start = line.index(token_value, current_pos)
            end = start + len(token_value)
            positions.append((start, end, (token_type, token_value)))
            current_pos = end
            print(f"Токен '{token_value}' найден в позиции {start}-{end}")
        except ValueError:
            print(f"Токен '{token_value}' не найден в строке с позиции {current_pos}")
            break
    return positions

def find_alternative_tokens(ggg_data: List[Dict[str, Any]], match_results: Dict, source_tokens: List[List[Tuple]], match_text: str) -> Dict:
    match_lines = match_text.split('\n')

    def search_token_group(group: List[Tuple]) -> List[int]:
        if not group:
            return []
        matched_lines = []
        for line_idx, line_tokens in enumerate(source_tokens):
            filtered_line = [t for t in line_tokens if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
            if len(filtered_line) < len(group):
                continue
            for i in range(len(filtered_line) - len(group) + 1):
                if filtered_line[i:i + len(group)] == group:
                    matched_lines.append(line_idx + 1)
                    break
        return matched_lines

    results = {}
    for entry in ggg_data:
        operator_num = entry['operator_number']
        before_ggg = entry['before']
        after_ggg = entry['after']
        before_ellipsis = after_ggg['before_ellipsis']
        after_ellipsis = after_ggg['after_ellipsis']

        # Если есть токены до или после >>>, пропускаем
        has_tokens = bool(before_ggg or before_ellipsis or after_ellipsis)
        if has_tokens:
            continue

        # Находим строку с данным >>> в match_text
        ggg_line_idx = None
        for i, line in enumerate(match_lines):
            if '>>>' in line:
                temp_ggg_data = check_ggg_in_lines('\n'.join(match_lines[:i + 1]), detect_programming_language(source_file))
                if any(e['operator_number'] == operator_num for e in temp_ggg_data):
                    ggg_line_idx = i
                    break

        if ggg_line_idx is None:
            continue

        results[operator_num] = {}

        # Проверяем следующую строку
        next_line_empty = True
        if ggg_line_idx + 1 < len(match_lines):
            next_line = match_lines[ggg_line_idx + 1].strip()
            next_tokens = tokenize_code(next_line, detect_programming_language(source_file))
            filtered_next_tokens = remove_insignificant_tokens(next_tokens, detect_programming_language(source_file))
            if filtered_next_tokens:  # Если есть значимые токены, следующая строка не пустая
                next_line_empty = False
                # Логика вставки перед следующей строкой
                matched_lines = search_token_group(filtered_next_tokens)
                if matched_lines:
                    results[operator_num]['next_line_matches'] = matched_lines

        # Если следующая строка пустая или её нет, идём к предыдущей строке
        if next_line_empty and ggg_line_idx > 0:
            prev_line = match_lines[ggg_line_idx - 1].strip()
            prev_tokens = tokenize_code(prev_line, detect_programming_language(source_file))
            filtered_prev_tokens = remove_insignificant_tokens(prev_tokens, detect_programming_language(source_file))
            # Исключаем строки с ...
            has_ellipsis = any(t[1] == '...' for t in filtered_prev_tokens)
            if not has_ellipsis and filtered_prev_tokens:
                matched_lines = search_token_group(filtered_prev_tokens)
                if matched_lines:
                    results[operator_num]['prev_line_matches'] = matched_lines

    return results
def insert_patch(source_file: str, markdown_file: str, match_results: Dict) -> None:
    _, patch_text, _ = load_code_from_markdown(markdown_file)
    source_tokens = source_to_tokenList(source_file, tokenize_code, detect_programming_language(source_file))

    with open(source_file, 'r', encoding='utf-8') as f:
        source_lines = f.readlines()

    def get_token_positions(line: str, line_tokens: List[Tuple]) -> List[Tuple[int, int, Tuple]]:
        positions = []
        current_pos = 0
        for token in line_tokens:
            token_type, token_value = token
            try:
                start = line.index(token_value, current_pos)
                end = start + len(token_value)
                positions.append((start, end, token))
                current_pos = end
            except ValueError:
                break
        return positions

    processed_lines = set()
    for operator_num, matches in match_results.items():
        if 'before_lines' in matches and matches['before_lines']:
            before_group = matches['before_group']
            for line_num, token_start_idx in matches['before_lines']:
                line_idx = line_num - 1
                if line_idx in processed_lines:
                    continue

                line = source_lines[line_idx]
                line_tokens = source_tokens[line_idx]
                filtered_line = [t for t in line_tokens if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
                token_positions = get_token_positions(line, line_tokens)
                filtered_indices = [i for i, t in enumerate(line_tokens) if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
                actual_start_idx = filtered_indices[token_start_idx]

                group_size = len(before_group)
                end_idx = actual_start_idx + group_size - 1
                if end_idx < len(token_positions):
                    _, end_pos, _ = token_positions[end_idx]
                    source_lines[line_idx] = line[:end_pos] + " " + patch_text + line[end_pos:]
                else:
                    source_lines[line_idx] = line.rstrip() + " " + patch_text

                processed_lines.add(line_idx)

        if 'after_lines' in matches and matches['after_lines']:
            after_group = matches['after_group']
            for line_num, token_start_idx in matches['after_lines']:
                line_idx = line_num - 1
                if line_idx in processed_lines:
                    continue

                line = source_lines[line_idx]
                line_tokens = source_tokens[line_idx]
                filtered_line = [t for t in line_tokens if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
                token_positions = get_token_positions(line, line_tokens)
                filtered_indices = [i for i, t in enumerate(line_tokens) if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
                actual_start_idx = filtered_indices[token_start_idx]

                start_pos, _, _ = token_positions[actual_start_idx]
                source_lines[line_idx] = line[:start_pos] + patch_text + " " + line[start_pos:]

                processed_lines.add(line_idx)

    with open(source_file, 'w', encoding='utf-8') as f:
        f.writelines(source_lines)

def insert_patch_based_on_alternative(source_file: str, markdown_file: str, alternative_results: dict, language) -> None:
    _, patch_text, indentation = load_code_from_markdown(markdown_file)
    with open(source_file, 'r', encoding='utf-8') as f:
        source_lines = f.readlines()

    line_offset = 0
    for operator_num, matches in alternative_results.items():
        # Проверяем, есть ли next_line_matches и пуст ли он
        has_next_matches = 'next_line_matches' in matches and len(matches['next_line_matches']) > 0

        # Вставка после prev_line_matches, только если после >>> ничего нет
        if 'prev_line_matches' in matches and not has_next_matches:
            for line_num in matches['prev_line_matches']:
                insert_idx = line_num + line_offset
                if language == "python":
                    source_lines.insert(insert_idx, indentation + patch_text + '\n')
                else:
                    source_lines.insert(insert_idx, patch_text + '\n')
                line_offset += 1
                print(f"Патч вставлен после строки {line_num} для '>>>' (номер {operator_num})")

        # Вставка перед next_line_matches (если они есть)
        if has_next_matches:
            for line_num in matches['next_line_matches']:
                insert_idx = line_num - 1 + line_offset
                if language == "python":
                    source_lines.insert(insert_idx, indentation + patch_text + '\n')
                else:
                    source_lines.insert(insert_idx, patch_text + '\n')
                line_offset += 1
                print(f"Патч вставлен перед строкой {line_num} для '>>>' (номер {operator_num})")

    with open(source_file, 'w', encoding='utf-8') as f:
        f.writelines(source_lines)


def get_token_positions(param, curr_line_tokens):
    pass


def handle_nested_structures(ggg_data: List[Dict[str, Any]], source_tokens: List[List[Tuple]], patch_text: str, indentation: str, source_file: str) -> None:
    """
    Обрабатывает случаи с вложенными структурами после >>>, находя закрывающую скобку и вставляя патч перед ней.
    """
    with open(source_file, 'r', encoding='utf-8') as f:
        source_lines = f.readlines()

    opening_brackets = {'(': ')', '[': ']', '{': '}'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    line_offset = 0
    for entry in ggg_data:
        operator_num = entry['operator_number']
        before_ggg = entry['before']
        after_ggg = entry['after']
        before_ellipsis = after_ggg['before_ellipsis']
        after_ellipsis = after_ggg['after_ellipsis']

        # Проверяем, есть ли открывающая скобка в before_ggg или after_ggg
        opening_bracket = None
        for token_type, token_value in before_ggg + before_ellipsis + after_ellipsis:
            if token_type == Token.Punctuation and token_value in opening_brackets:
                opening_bracket = token_value
                break

        # Если нет открывающей скобки, пропускаем
        if not opening_bracket:
            continue

        closing_bracket = opening_brackets[opening_bracket]

        # Ищем строки в исходном коде, соответствующие before_ggg
        matched_lines = []
        for line_idx, line_tokens in enumerate(source_tokens):
            filtered_line = [t for t in line_tokens if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
            if len(filtered_line) < len(before_ggg):
                continue
            for i in range(len(filtered_line) - len(before_ggg) + 1):
                if filtered_line[i:i + len(before_ggg)] == before_ggg:
                    matched_lines.append(line_idx)
                    break

        if not matched_lines:
            continue

        # Для каждой подходящей строки ищем закрывающую скобку с учетом вложенности
        for line_idx in matched_lines:
            nest_level = 0
            insert_pos = None
            start_found = False

            for curr_line_idx in range(line_idx, len(source_tokens)):
                curr_line_tokens = source_tokens[curr_line_idx]
                filtered_curr_line = [t for t in curr_line_tokens if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]

                for token_idx, (token_type, token_value) in enumerate(filtered_curr_line):
                    if not start_found:
                        if filtered_curr_line[:len(before_ggg)] == before_ggg:
                            start_found = True
                            # Проверяем следующий токен после before_ggg
                            if token_idx + len(before_ggg) < len(filtered_curr_line):
                                next_token = filtered_curr_line[token_idx + len(before_ggg)]
                                if next_token[0] == Token.Punctuation and next_token[1] == opening_bracket:
                                    nest_level = 1
                        continue

                    if token_type == Token.Punctuation:
                        if token_value == opening_bracket:
                            nest_level += 1
                        elif token_value == closing_bracket:
                            nest_level -= 1
                            if nest_level == 0:
                                token_positions = get_token_positions(source_lines[curr_line_idx + line_offset], curr_line_tokens)
                                filtered_indices = [i for i, t in enumerate(curr_line_tokens) if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
                                actual_idx = filtered_indices[token_idx]
                                insert_pos = token_positions[actual_idx][0]
                                source_lines[curr_line_idx + line_offset] = (
                                    source_lines[curr_line_idx + line_offset][:insert_pos] +
                                    indentation + patch_text + "\n" + indentation +
                                    source_lines[curr_line_idx + line_offset][insert_pos:]
                                )
                                line_offset += source_lines[curr_line_idx + line_offset].count('\n') - 1
                                break
                if insert_pos is not None:
                    break

            if insert_pos is not None:
                print(f"Патч вставлен перед закрывающей скобкой в строке {line_idx + 1} для '>>>' (номер {operator_num})")

    with open(source_file, 'w', encoding='utf-8') as f:
        f.writelines(source_lines)


def insert_patch_for_brackets(source_file: str, markdown_file: str, match_text: str, source_tokens: List[List[Tuple]], language: str) -> None:
    """
    Вставляет патч перед закрывающей скобкой, соответствующей открывающей скобке в match,
    с учетом вложенности и токенов в той же строке.
    """
    match_lines = match_text.split('\n')
    _, patch_text, indentation = load_code_from_markdown(markdown_file)

    with open(source_file, 'r', encoding='utf-8') as f:
        source_lines = f.readlines()

    opening_brackets = {'(': ')', '[': ']', '{': '}'}
    closing_brackets = {')': '(', ']': '[', '}': '{'}

    # Ищем строку с >>> в match, чтобы понять, с какими скобками работать
    ggg_line_idx = None
    for i, line in enumerate(match_lines):
        if '>>>' in line:
            ggg_line_idx = i
            break

    if ggg_line_idx is None:
        print("Не найдена строка с >>> в match.")
        return

    # Собираем токены из match до >>>, чтобы найти соответствующую открывающую скобку
    tokens_before_ggg = []
    opening_bracket = None
    for line in match_lines[:ggg_line_idx]:
        if '...' in line or '>>>' in line:
            continue
        tokens = tokenize_code(line.strip(), language)
        filtered_tokens = remove_insignificant_tokens(tokens, language)
        for i, (token_type, token_value) in enumerate(filtered_tokens):
            if token_type == Token.Punctuation and token_value in opening_brackets:
                opening_bracket = token_value
                tokens_before_ggg = filtered_tokens[:i]
                break
        if opening_bracket:
            break

    if not opening_bracket or not tokens_before_ggg:
        print("Не найдена открывающая скобка или токены перед ней в match.")
        return

    closing_bracket = opening_brackets[opening_bracket]
    print(f"Найдена открывающая скобка '{opening_bracket}' с токенами перед ней: {tokens_before_ggg}")

    # Ищем строки в исходном коде, соответствующие tokens_before_ggg
    matched_lines = []
    for line_idx, line_tokens in enumerate(source_tokens):
        filtered_line = [t for t in line_tokens if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
        if len(filtered_line) < len(tokens_before_ggg) + 1:
            continue
        for i in range(len(filtered_line) - len(tokens_before_ggg)):
            if filtered_line[i:i + len(tokens_before_ggg)] == tokens_before_ggg:
                next_token = filtered_line[i + len(tokens_before_ggg)]
                if next_token[0] == Token.Punctuation and next_token[1] == opening_bracket:
                    matched_lines.append(line_idx)
                    break

    if not matched_lines:
        print("Не найдено совпадений для токенов перед открывающей скобкой в исходном коде.")
        return

    # Для каждой подходящей строки ищем закрывающую скобку с учетом вложенности
    line_offset = 0
    for line_idx in matched_lines:
        nest_level = 0
        insert_pos = None
        start_found = False

        print(f"Начинаем поиск закрывающей скобки для строки {line_idx + 1}")
        for curr_line_idx in range(line_idx, len(source_tokens)):
            curr_line_tokens = source_tokens[curr_line_idx]
            filtered_curr_line = [t for t in curr_line_tokens if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]

            if not filtered_curr_line:  # Пропускаем пустые строки
                continue

            for token_idx, (token_type, token_value) in enumerate(filtered_curr_line):
                if not start_found:
                    if (token_idx + len(tokens_before_ggg) < len(filtered_curr_line) and
                        filtered_curr_line[token_idx:token_idx + len(tokens_before_ggg)] == tokens_before_ggg):
                        next_token = filtered_curr_line[token_idx + len(tokens_before_ggg)]
                        if next_token[0] == Token.Punctuation and next_token[1] == opening_bracket:
                            nest_level = 1
                            start_found = True
                            print(f"Начало вложенности найдено в строке {curr_line_idx + 1}, nest_level = {nest_level}")
                    continue

                if token_type == Token.Punctuation:
                    if token_value == opening_bracket:
                        nest_level += 1
                        print(f"Строка {curr_line_idx + 1}: Открывающая '{opening_bracket}', nest_level = {nest_level}")
                    elif token_value == closing_bracket:
                        nest_level -= 1
                        print(f"Строка {curr_line_idx + 1}: Закрывающая '{closing_bracket}', nest_level = {nest_level}")
                        if nest_level == 0:
                            token_positions = get_token_positions(source_lines[curr_line_idx + line_offset], curr_line_tokens)
                            if not token_positions:
                                print(f"Ошибка: не удалось определить позиции токенов для строки {curr_line_idx + 1}")
                                insert_pos = 0
                                source_lines[curr_line_idx + line_offset] = (
                                    indentation + patch_text + "\n" + indentation +
                                    source_lines[curr_line_idx + line_offset]
                                )
                            else:
                                filtered_indices = [i for i, t in enumerate(curr_line_tokens) if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
                                actual_idx = filtered_indices[token_idx]
                                insert_pos = token_positions[actual_idx][0]
                                source_lines[curr_line_idx + line_offset] = (
                                    source_lines[curr_line_idx + line_offset][:insert_pos] +
                                    indentation + patch_text + "\n" + indentation +
                                    source_lines[curr_line_idx + line_offset][insert_pos:]
                                )
                            line_offset += source_lines[curr_line_idx + line_offset].count('\n') - 1
                            break
            if insert_pos is not None:
                break

        if insert_pos is not None:
            print(f"Патч вставлен перед закрывающей скобкой в строке {curr_line_idx + 1}")
        else:
            print(f"Не удалось найти подходящую закрывающую скобку для строки {line_idx + 1}")

    with open(source_file, 'w', encoding='utf-8') as f:
        f.writelines(source_lines)

def insert_patch_in_function_signature(source_file: str, markdown_file: str, match_text: str, source_tokens: List[List[Tuple]], language: str) -> None:
    """
    Вставляет патч перед закрывающей скобкой в сигнатуре функции, обозначенной >>> в match.
    """
    match_lines = match_text.split('\n')
    _, patch_text, indentation = load_code_from_markdown(markdown_file)

    with open(source_file, 'r', encoding='utf-8') as f:
        source_lines = f.readlines()

    # Ищем строку с >>> в сигнатуре функции в match
    func_line = None
    tokens_before_ggg = []
    for line in match_lines:
        tokens = tokenize_code(line.strip(), language)
        filtered_tokens = remove_insignificant_tokens(tokens, language)
        ggg_index = next((i for i, t in enumerate(filtered_tokens) if t[1] == '>>>'), -1)
        if ggg_index != -1:
            func_line = line
            tokens_before_ggg = filtered_tokens[:ggg_index]
            break

    if not func_line or not tokens_before_ggg:
        print("Не найдена строка с >>> в сигнатуре функции в match.")
        return

    # Ищем соответствующую строку в исходном коде
    matched_line_idx = None
    for line_idx, line_tokens in enumerate(source_tokens):
        filtered_line = [t for t in line_tokens if not (is_token_subtype(t[0], Token.Text) and t[1].isspace())]
        if len(filtered_line) < len(tokens_before_ggg):
            continue
        for i in range(len(filtered_line) - len(tokens_before_ggg) + 1):
            if filtered_line[i:i + len(tokens_before_ggg)] == tokens_before_ggg:
                matched_line_idx = line_idx
                break
        if matched_line_idx is None:
            break

    if matched_line_idx is None:
        print("Не найдено совпадение для сигнатуры функции в исходном коде.")
        return

    # Вставляем патч перед закрывающей скобкой )
    line = source_lines[matched_line_idx]
    line_tokens = source_tokens[matched_line_idx]
    closing_paren_idx = next((i for i, t in enumerate(line_tokens) if t[1] == ')'), -1)
    if closing_paren_idx == -1:
        print(f"Не найдена закрывающая скобка ) в строке {matched_line_idx + 1}")
        return

    token_positions = get_token_positions(line, line_tokens)
    insert_pos = token_positions[closing_paren_idx][0]
    source_lines[matched_line_idx] = (
        line[:insert_pos] +
        patch_text +
        line[insert_pos:]
    )
    print(f"Патч вставлен в сигнатуру функции в строке {matched_line_idx + 1}")

    with open(source_file, 'w', encoding='utf-8') as f:
        f.writelines(source_lines)

def main():
    source_file = "/xpressions.cpp"
    markdown_file = "C:/Users/droby/Desktop/прога/py_add_beg.md"
    language = detect_programming_language(source_file)

    match_text, patch_text, indentation = load_code_from_markdown(markdown_file)
    source_tokens = source_to_tokenList(source_file, tokenize_code, language)
    tr4 = remove_in_tok_match(markdown_file, language)
    print(tokenize_code(match_text,"python"))
    print("Match:", tr4)
    print("Source:", source_tokens)
    process_match_structure(tr4)

    matched_lines = find_matching_lines(tr4, source_tokens)
    print("Matched lines indices:", matched_lines)

    ggg_data = check_ggg_in_lines(match_text, language)

    # Определяем условия для выбора логики
    has_opening_bracket = any('{' in line or '(' in line or '[' in line
                             for line in match_text.split('\n')
                             if '>>>' not in line and '...' not in line)
    has_closing_bracket_after_ggg = False
    has_ggg_in_function = False
    for line in match_text.split('\n'):
        tokens = tokenize_code(line.strip(), language)
        filtered_tokens = remove_insignificant_tokens(tokens, language)
        ggg_index = next((i for i, t in enumerate(filtered_tokens) if t[1] == '>>>'), -1)
        if ggg_index != -1:
            before_ggg = filtered_tokens[:ggg_index]
            after_ggg = filtered_tokens[ggg_index + 1:]
            if not before_ggg and after_ggg and any(t[1] in {')', ']', '}'} for t in after_ggg):
                has_closing_bracket_after_ggg = True
            elif before_ggg and not any(t[1] in {')', ']', '}'} for t in after_ggg):
                has_ggg_in_function = True
            break

    # Выполняем логику в зависимости от условий
    if has_opening_bracket and has_closing_bracket_after_ggg:
        insert_patch_for_brackets(source_file, markdown_file, match_text, source_tokens, language)
        handle_nested_structures(ggg_data, source_tokens, patch_text, indentation, source_file)
    elif has_ggg_in_function:
        insert_patch_in_function_signature(source_file, markdown_file, match_text, source_tokens, language)
    elif has_opening_bracket:
        insert_patch_for_brackets(source_file, markdown_file, match_text, source_tokens, language)
    else:
        match_results = find_tokens_in_source(ggg_data, source_tokens)
        insert_patch(source_file, markdown_file, match_results)
        alternative_results = find_alternative_tokens(ggg_data, match_results, source_tokens, match_text)
        insert_patch_based_on_alternative(source_file, markdown_file, alternative_results, language)
        if any('>>>' in line for line in match_text.split('\n')):
            handle_nested_structures(ggg_data, source_tokens, patch_text, indentation, source_file)

if __name__ == "__main__":
    main()