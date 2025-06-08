from LoadFromUI import ReceivingMatchOrPatchOrSourceCodeFromList, MatchLoadFromString, PatchLoadFromString,DetectProgrammingLanguage
from TokenizeCode import TokenizeCode,FindSpecialOperatorIndixes,CheckAndRunTokenize,RemoveInsignificantTokens
from SearchCode import SearchInsertIndexInTokenList, InsertNestingLevel, SearchInsertIndexInSourseCode, GetBracketIndicesForEllipsis, CheckMatchNestingMarkerPairs, MatchNestingLevelInsertALL
import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s', filename='logfile.log')
ListOfCodeAndInstructionAndLanguage = ["C:/Users/droby/Desktop/ghju2/прога/test/unique2.md", "file", "C:/Users/droby/Desktop/ghju2/прога/source/unique2.cpp", "file","cpp"]
# ListOfCodeAndInstructionAndLanguage - List of [matchContent, matchType, sourceContent, sourceType, sourceLanguage]
Language = ListOfCodeAndInstructionAndLanguage[4]
Match = ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage, True, MatchLoadFromString)
Patch = ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage, True, PatchLoadFromString)
SourceCode = ReceivingMatchOrPatchOrSourceCodeFromList(ListOfCodeAndInstructionAndLanguage, False)
Match = CheckAndRunTokenize(Match, Language)
SourceCode = CheckAndRunTokenize(SourceCode, Language)
SearchDictionary = SearchInsertIndexInTokenList(Match, SourceCode)
NestingLevel = InsertNestingLevel(Match)
InsertIndexInSourseCode = SearchInsertIndexInSourseCode(Match, SourceCode)
NestingMap = MatchNestingLevelInsertALL(Match)
IsNestingMarkerPairsList = CheckMatchNestingMarkerPairs(Match)
NLE = GetBracketIndicesForEllipsis(Match)
print(f"Match TokenList: {Match}")
print(f"Source code TokenList: {SourceCode}")
print(f"Match nesting map: {NestingMap}")
print(f"Match nesting : {NestingLevel}")
print(f"Match NLE : {NLE}")
print(f"Insert index in sourcecode TokenList: {SearchDictionary}")
print(f"Source code TokenList len: {len(SourceCode) - 1}")
print(f"Insert index in source code: {InsertIndexInSourseCode}")
