import os
from LoadFromUI import ReceivingMatchOrPatchOrSourceCodeFromList, MatchLoadFromString, PatchLoadFromString, DetectProgrammingLanguage
from TokenizeCode import TokenizeCode, FindSpecialOperatorIndixes, CheckAndRunTokenize, RemoveInsignificantTokens
from SearchCode import SearchInsertIndexInTokenList, InsertNestingLevel, SearchInsertIndexInSourseCode, CheckMatchNestingMarkerPairs, MatchNestingLevelInsertALL

# Папки с файлами
test_folder = "test"
source_folder = "source"
results = []
# Получаем списки файлов
test_files = [f for f in os.listdir(test_folder) if f.endswith(".md")]
source_files = [f for f in os.listdir(source_folder) if f.endswith(".cpp")]
print(test_files,source_files)
# Находим пары файлов с одинаковыми базовыми именами
pairs = []
for test_file in test_files:
    base_name = os.path.splitext(test_file)[0]
    source_file = f"{base_name}.cpp"
    if source_file in source_files:
        pairs.append((os.path.join(test_folder, test_file), os.path.join(source_folder, source_file)))
# Обрабатываем каждую пару
for test_path, source_path in pairs:

    base_name = os.path.splitext(os.path.basename(test_path))[0]
    print(f"\n=== Processing files: {test_path} and {source_path} ===")

    # Формируем список для функции
    ListOfCodeAndInstructionAndLanguage = [test_path, "file", source_path, "file", "cpp"]
    Language = ListOfCodeAndInstructionAndLanguage[4]

    # Выполняем предоставленный код
    Match = ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage, True, MatchLoadFromString)
    Patch = ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage, True, PatchLoadFromString)
    SourceCode = ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage, False)
    Match = CheckAndRunTokenize(Match, Language)
    SourceCode = CheckAndRunTokenize(SourceCode, Language)
    SearchDictionary = SearchInsertIndexInTokenList(Match, SourceCode)
    NestingLevel = InsertNestingLevel(Match)
    MatchL = InsertNestingLevel(Match)
    InsertIndexInSourseCode = SearchInsertIndexInSourseCode(Match, SourceCode)
    NestingMap = MatchNestingLevelInsertALL(Match)
    IsNestingMarkerPairsList = CheckMatchNestingMarkerPairs(Match)

    # Собираем результаты в кортеж и добавляем в список
    result_tuple = (
        Match,
        SourceCode,
        NestingMap,
        MatchL,
        SearchDictionary,
        len(SourceCode) - 1,
        InsertIndexInSourseCode,
        base_name
    )
    results.append(result_tuple)

# Выводим все результаты
print("=== All Processing Results ===")
for result in results:
    Match, SourceCode, NestingMap, MatchL, SearchDictionary, source_len, InsertIndexInSourseCode, base_name = result
    print(f"\n=== Results for {base_name} ===")
    print(f"Match nesting map: {NestingMap}")
    print(f"Match nesting: {MatchL}")
    print(f"Insert index in sourcecode TokenList: {SearchDictionary}")
    print(f"Source code TokenList len: {source_len}")
    print(f"Insert index in source code: {InsertIndexInSourseCode}")
    print(f"=== End results for {base_name} ===\n")
print("=== End of All Results ===")