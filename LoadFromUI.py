import re
from typing import Optional

def ReadFile(FileNameMarkdown):
    try:
        with open(FileNameMarkdown, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        return f"Ошибка: файл {FileNameMarkdown} не найден"

def MatchLoadFromString(StringOfMarkdownContent):
    match = re.search(r'### match:\s*```(.*?)```', StringOfMarkdownContent, re.DOTALL)
    return match.group(1).strip() if match else None

def PatchLoadFromString(StringOfMarkdownContent):
    patch = re.search(r'### patch\s*```(.*?)```', StringOfMarkdownContent, re.DOTALL)
    return patch.group(1).strip() if patch else None

def DetectProgrammingLanguage(FileNameSourceCode):
    extensions = {
    '.py': 'python', '.java': 'java', '.cpp': 'cpp',
    '.c': 'c', '.cs': 'csharp', '.js': 'javascript',
    '.rb': 'ruby', '.ts': 'typescript', '.go': 'go',
    '.rs': ' ', }
    ext = '.' + FileNameSourceCode.split('.')[-1]
    return extensions.get(ext, 'Неизвестный язык')

def ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage,IsInstruction, functionMatchOrPatch: Optional = None):
    if IsInstruction:
        if functionMatchOrPatch is None: raise ValueError("match_or_patch_function must be provided when is_instruction is True")

        elif ListOfCodeAndInstructionAndLanguage[1] == 'text': return  functionMatchOrPatch( ListOfCodeAndInstructionAndLanguage[0] )

        else: return functionMatchOrPatch(ReadFile( ListOfCodeAndInstructionAndLanguage[0]) )
    else:
        if ListOfCodeAndInstructionAndLanguage[3] != 'text': return ReadFile( ListOfCodeAndInstructionAndLanguage[2] )

        else: return ListOfCodeAndInstructionAndLanguage[2]
