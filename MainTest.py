import os
from LoadFromUI import ReceivingMatchOrPatchOrSourceCodeFromList, MatchLoadFromString, PatchLoadFromString, DetectProgrammingLanguage
from TokenizeCode import TokenizeCode, FindSpecialOperatorIndixes, CheckAndRunTokenize, RemoveInsignificantTokens
from SearchCode import SearchInsertIndexInTokenList, InsertNestingLevel, SearchInsertIndexInSourseCode, CheckMatchNestingMarkerPairs, MatchNestingLevelInsertALL

test_folder = "test"
source_folder = "source"
results = []
test_files = [f for f in os.listdir(test_folder) if f.endswith(".md")]
source_files = [f for f in os.listdir(source_folder) if f.endswith(".cpp")]
print(test_files,source_files)
pairs = []

for test_file in test_files:
    base_name = os.path.splitext(test_file)[0]
    source_file = f"{base_name}.cpp"
    if source_file in source_files:
        pairs.append((os.path.join(test_folder, test_file), os.path.join(source_folder, source_file)))

for test_path, source_path in pairs:
    base_name = os.path.splitext(os.path.basename(test_path))[0]
    print(f"\n=== Processing files: {test_path} and {source_path} ===")
    ListOfCodeAndInstructionAndLanguage = [test_path, "file", source_path, "file", "cpp"]
    Language = ListOfCodeAndInstructionAndLanguage[4]

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