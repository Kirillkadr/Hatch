import argparse
import sys
from ParsingCodeAndInstruction import ReceivingMatchOrPatchOrSourceCodeFromList, MatchLoadFromString, PatchLoadFromString, DetectProgrammingLanguage
from TokenizeCode import CheckAndRunTokenize
from SearchCode import SearchInsertIndexInTokenList, InsertNestingLevel, SearchInsertIndexInSourseCode, GetBracketIndicesForEllipsis, CheckMatchNestingMarkerPairs, MatchNestingLevelInsertALL


def process_match_mode(match_path, in_path, out_path):
    try:
        # Определяем язык программирования
        language = DetectProgrammingLanguage(in_path)
        # Загружаем match и source code
        match = ReceivingMatchOrPatchOrSourceCodeFromList(match_path, 'Match')
        source_code = ReceivingMatchOrPatchOrSourceCodeFromList(in_path, 'SourceCode')
        # Токенизация
        match = CheckAndRunTokenize(match, language)
        source_code = CheckAndRunTokenize(source_code, language)
        # Выполняем анализ
        search_dictionary = SearchInsertIndexInTokenList(match, source_code)
        nesting_level = InsertNestingLevel(match)
        insert_index_in_source = SearchInsertIndexInSourseCode(match, source_code)
        nesting_map = MatchNestingLevelInsertALL(match)
        is_nesting_marker_pairs = CheckMatchNestingMarkerPairs(match)
        nle = GetBracketIndicesForEllipsis(match)
        # Формируем результат
        result = (
            f"Match TokenList: {match}\n"
            f"Source code TokenList: {source_code}\n"
            f"Match nesting map: {nesting_map}\n"
            f"Match nesting: {nesting_level}\n"
            f"Match NLE: {nle}\n"
            f"Insert index in sourcecode TokenList: {search_dictionary}\n"
            f"Source code TokenList len: {len(source_code) - 1}\n"
            f"Insert index in source code: {insert_index_in_source}"
        )
        # Записываем результат в выходной файл
        with open(out_path, 'w', encoding='utf-8') as outf:
            outf.write(result)
        return f"Режим match: обработан {in_path}, результат сохранен в {out_path}"
    except Exception as e:
        return f"Ошибка в режиме match: {e}"


def main():
    # Создаем парсер для аргументов командной строки
    parser = argparse.ArgumentParser(description="Программа для анализа кода с match")

    # Аргументы для режима match
    parser.add_argument('--match', type=str, help='Путь к файлу match (например, file.md)')
    parser.add_argument('--in', type=str, dest='in_file', help='Путь к входному файлу (например, 1.cpp)')
    parser.add_argument('--out', type=str, help='Путь к выходному файлу (например, 1_r.cpp)')
    parser.add_argument('--patch', type=str, help='Путь к файлу patch')

    # Разбираем аргументы
    args = parser.parse_args()

    # Проверяем, используется ли режим match
    if args.match and args.in_file and args.out:
        result = process_match_mode(args.match, args.in_file, args.out)
        print(result)
    else:
        print("Ошибка: некорректные аргументы. Требуются --match, --in и --out")
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()