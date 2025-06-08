import webview
from LoadFromUI import ReceivingMatchOrPatchOrSourceCodeFromList, MatchLoadFromString, PatchLoadFromString,DetectProgrammingLanguage
from TokenizeCode import TokenizeCode,FindSpecialOperatorIndixes,CheckAndRunTokenize,RemoveInsignificantTokens
from SearchCode import SearchInsertIndexInTokenList, InsertNestingLevel, SearchInsertIndexInSourseCode, CheckMatchNestingMarkerPairs

class DataProcessor:
        def ProcessInputData(self, ListOfCodeAndInstructionAndLanguage):
            #ListOfCodeAndInstructionAndLanguage - List of [matchContent, matchType, sourceContent, sourceType, sourceLanguage]
            Language = ListOfCodeAndInstructionAndLanguage[4]
            Match = ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage, True, MatchLoadFromString)
            Patch = ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage, True, PatchLoadFromString)
            SourceCode = ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage, False)
            Match = CheckAndRunTokenize(Match, Language)
            SourceCode = CheckAndRunTokenize(SourceCode, Language)
            SearchDictionary = SearchInsertIndexInTokenList(Match,SourceCode)
            NestingLevel = InsertNestingLevel(Match)
            InsertIndexInSourseCode = SearchInsertIndexInSourseCode(Match,SourceCode)
            NestingMap = CheckMatchNestingMarkerPairs(Match)
            print(f"Match TokenList: {Match}")
            print(f"Source code TokenList: {SourceCode}")
            print(f"Match nesting map: {NestingMap}")
            print(f"Match nesting Level: {NestingLevel}")
            print(f"Insert index in sourcecode TokenList: {SearchDictionary}")
            print(f"Source code TokenList len: {len(SourceCode) - 1}")
            print(f"Insert index in source code: {InsertIndexInSourseCode}")
            return process_data(ListOfCodeAndInstructionAndLanguage)

def process_data(ListOfCodeAndInstruction):
    return ListOfCodeAndInstruction

def StartUI():
    processor = DataProcessor()
    window = webview.create_window(
        "File Processor",
        url="UsersUX.html",
        js_api=processor,
        width=900,
        height=700
    )
    webview.start()

if __name__ == "__main__":

    StartUI()
