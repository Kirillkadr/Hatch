def SearchInsertIndexInTokenList(MatchTokenList: list[tuple], SourceCodeTokenList: list[tuple]):
    IsPassList = [("",0,0,0)]
    print("Входим в функцию SearchInsertIndexInTokenList с MatchTokenList и SourceCodeTokenList")
    FlagFirstCircle = True
    print(f"Инициализируем FlagFirstCircle значением {FlagFirstCircle}")
    CurentSourceCodeTokenIndex = 0
    print(f"Инициализируем CurentSourceCodeTokenIndex значением {CurentSourceCodeTokenIndex}")
    SourceCodeNestingLevel = 0
    SourceCodeRelativeNestingLevel = 0
    print(f"Инициализируем SourceCodeNestingLevel значением {SourceCodeNestingLevel}")
    NestingMap = MatchNestingLevelInsertALL(MatchTokenList)
    for MatchTokenIndex in range(len(MatchTokenList)):
        print(f"Начинаем итерацию цикла с MatchTokenIndex = {MatchTokenIndex}")
        if MatchTokenList[MatchTokenIndex][1] == '...':
            print(f"Обнаружен '...' в MatchTokenList[{MatchTokenIndex}]")
            IsPassList, FlagFirstCircle = IsPass(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, IsPassList, FlagFirstCircle, NestingMap)
            print(f"После вызова IsPass:  = {IsPassList}")
        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            print(f"Обнаружен '>>>' в MatchTokenList[{MatchTokenIndex}]")
            ResultTokenInsert = IsInsert(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, IsPassList, FlagFirstCircle,NestingMap)
            print(f"Получен результат от IsInsert: {ResultTokenInsert}")
            return ResultTokenInsert
    print("Цикл завершен, возвращаем 0")
    return 0
def ComparisonToken(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, SourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle, SourceCodeRelativeNestingLevel,NestingMap):
    print(f"Входим в функцию ComparisonToken с MatchTokenIndex = {MatchTokenIndex}, SourceCodeTokenIndex = {SourceCodeTokenIndex}")
    ComparisonIndex = 1
    print(f"Инициализируем ComparisonIndex значением {ComparisonIndex}")
    NumberTokenMatch = 0
    print(f"Инициализируем NumberTokenMatch значением {NumberTokenMatch}")
    NumberTokenSource = 0
    print(f"Инициализируем NumberTokenSource значением {NumberTokenSource}")
    ComparisonSourceCodeNestingLevel = 0
    ComprasionSourceCodeRelativeNestingLevel = 0
    print(f"Инициализируем ComparisonSourceCodeNestingLevel значением {ComparisonSourceCodeNestingLevel}")
    if FlagFirstCircle:
        print("FlagFirstCircle = True, обновляем SourceCodeNestingLevel")
        if NestingMap[MatchTokenIndex + 1][0] == -1:
            SourceCodeRelativeNestingLevel = SourceNestingLevelChange(SourceCodeRelativeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, 0)
            print(f"обновляем SourceCodeRelativeNestingLevel{SourceCodeRelativeNestingLevel}")
        SourceCodeNestingLevel = SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, 0)
        print(f"SourceCodeNestingLevel обновлен до {SourceCodeNestingLevel}")
    while MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]:
        print(f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}, значение = {SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex]}")
        NumberTokenMatch = NumberTokenMatch + 1
        print(f"В цикле while, ComparisonIndex = {ComparisonIndex}")
        if NestingMap[MatchTokenIndex + 1][0] == -1:
            ComprasionSourceCodeRelativeNestingLevel = SourceNestingLevelChange(ComprasionSourceCodeRelativeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, ComparisonIndex)
            print(f"обновляем ComprasionSourceCodeRelativeNestingLeve{ComprasionSourceCodeRelativeNestingLevel}")

        ComparisonSourceCodeNestingLevel = SourceNestingLevelChange(ComparisonSourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, ComparisonIndex)
        print(f"Обновлен ComparisonSourceCodeNestingLevel до {ComparisonSourceCodeNestingLevel}")
        if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1]:
            print(f"Токены не совпадают: MatchTokenList[{MatchTokenIndex + 1 + ComparisonIndex}] и SourceCodeTokenList[{SourceCodeTokenIndex + ComparisonIndex}]")
            ComparisonSourceCodeNestingLevel = 0
            ComprasionSourceCodeRelativeNestingLevel = 0
            print(f"Сбрасываем ComparisonSourceCodeNestingLevel до {ComparisonSourceCodeNestingLevel}")
            break
        NumberTokenSource = NumberTokenSource + 1
        print(f"Увеличиваем NumberTokenSource до {NumberTokenSource}")
        ComparisonIndex = ComparisonIndex + 1
        print(f"Увеличиваем ComparisonIndex до {ComparisonIndex}")
    print(f"Выходим из ComparisonToken, возвращаем: ComparisonIndex = {ComparisonIndex}, NumberTokenMatch = {NumberTokenMatch}, NumberTokenSource = {NumberTokenSource}, SourceCodeNestingLevel = {SourceCodeNestingLevel}, ComparisonSourceCodeNestingLevel = {ComparisonSourceCodeNestingLevel},SourceCodeRelativeNestingLevel = {SourceCodeRelativeNestingLevel},ComprasionSourceCodeRelativeNestingLevel = {ComprasionSourceCodeRelativeNestingLevel}")
    return ComparisonIndex, NumberTokenMatch, NumberTokenSource, SourceCodeNestingLevel, ComparisonSourceCodeNestingLevel,SourceCodeRelativeNestingLevel,  ComprasionSourceCodeRelativeNestingLevel


def SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, ComparisonIndex):
    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["{", "(", "["]:
        SourceCodeNestingLevel = SourceCodeNestingLevel + 1
        print(f"SourceCodeNestingLevel увеличен до {SourceCodeNestingLevel}")
    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["}", ")", "]"]:
        SourceCodeNestingLevel = SourceCodeNestingLevel - 1
        print(f"SourceCodeNestingLevel уменьшен до {SourceCodeNestingLevel}")
    return SourceCodeNestingLevel


def IsPass(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, IsPassList, FlagFirstCircle, NestingMap):
    IsPassOutputList = []
    if IsPassList:
        skip_rest = False
        print(f"Инициализируем skip_rest = {skip_rest}")
        if MatchTokenIndex + 1 < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1][1] == '>>>':
            print(f"Следующий токен '>>>', устанавливаем skip_rest = True")
            skip_rest = True
        if not skip_rest:
            print("skip_rest = False, начинаем цикл по SourceCodeTokenList")
            for  IsPassOutput in IsPassList:
                CurentSourceCodeTokenIndex = IsPassOutput[1]
                SourceCodeNestingLevel = IsPassOutput[2]
                SourceCodeRelativeNestingLevel = IsPassOutput[3]
                StartCurentSourceCodeTokenIndex = IsPassOutput[1]
                print(f"Входим в функцию IsPass с MatchTokenIndex = {MatchTokenIndex}, CurentSourceCodeTokenIndex = {CurentSourceCodeTokenIndex}")
                print(f"Получена NestingMap: {NestingMap}")
                CounterMatches = 0
                for SourceCodeTokenIndex in range(StartCurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                    print(f"Итерация цикла с SourceCodeTokenIndex = {SourceCodeTokenIndex}, значение = {SourceCodeTokenList[SourceCodeTokenIndex]} ")
                    if MatchTokenIndex + 1 < len(MatchTokenList):
                        if not FlagFirstCircle:
                            print("FlagFirstCircle = False, обновляем SourceCodeNestingLevel")
                            SourceCodeNestingLevel = SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, 0)
                            print(f"обновляем SourceCodeRelativeNestingLevel{SourceCodeRelativeNestingLevel}")
                        if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                            print(f"Токены совпадают: SourceCodeTokenList[{SourceCodeTokenIndex}] и MatchTokenList[{MatchTokenIndex + 1}]")
                            StartSourceCodeRelativeNestingLevel = SourceCodeRelativeNestingLevel
                            StartSourceCodeNestingLevel = SourceCodeNestingLevel
                            ComparisonIndex, NumberTokenMatch, NumberTokenSource, SourceCodeNestingLevel, ComparisonSourceCodeNestingLevel,SourceCodeRelativeNestingLevel,  ComprasionSourceCodeRelativeNestingLevel  = ComparisonToken(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, SourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle, SourceCodeRelativeNestingLevel,NestingMap)
                            print(f"Результат ComparisonToken: ComparisonIndex = {ComparisonIndex}, NumberTokenMatch = {NumberTokenMatch}, NumberTokenSource = {NumberTokenSource}, SourceCodeNestingLevel = {SourceCodeNestingLevel}, ComparisonSourceCodeNestingLevel = {ComparisonSourceCodeNestingLevel}")
                            if NumberTokenSource == NumberTokenMatch:
                                IndexString = IsPassOutput[0] + str(CounterMatches) + '/'
                                if NestingMap[MatchTokenIndex + ComparisonIndex][0] != -1:
                                    print("NumberTokenSource равно NumberTokenMatch, проверяем уровни вложенности")
                                    if NestingMap[MatchTokenIndex  + ComparisonIndex][0] == SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel:
                                        print("Уровни вложенности совпадают ")
                                        CurentSourceCodeTokenIndex = ComparisonIndex + SourceCodeTokenIndex
                                        print(f"Обновляем CurentSourceCodeTokenIndex до {CurentSourceCodeTokenIndex}")
                                        SourceCodeNestingLevel = SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel
                                        print(f"Обновляем SourceCodeNestingLevel до {SourceCodeNestingLevel}")
                                        CounterMatches += 1
                                        IsPassOutputList.append((IndexString,CurentSourceCodeTokenIndex,SourceCodeNestingLevel, SourceCodeRelativeNestingLevel))
                                        print(f"Обновляем IsPassList до {IsPassList}")
                                        ComparisonSourceCodeNestingLevel = 0
                                        print(f"Сбрасываем ComparisonSourceCodeNestingLevel до {ComparisonSourceCodeNestingLevel}")
                                        SourceCodeNestingLevel = StartSourceCodeNestingLevel
                                        SourceCodeRelativeNestingLevel = StartSourceCodeRelativeNestingLevel

                                else:
                                    if NestingMap[MatchTokenIndex  + ComparisonIndex][1] == ComprasionSourceCodeRelativeNestingLevel + SourceCodeRelativeNestingLevel or NestingMap[MatchTokenIndex  + ComparisonIndex][1] == 0:
                                        print("Уровни вложенности совпадают при NestingMap = -1")
                                        CurentSourceCodeTokenIndex = ComparisonIndex + SourceCodeTokenIndex
                                        print(f"Обновляем CurentSourceCodeTokenIndex до {CurentSourceCodeTokenIndex}")
                                        SourceCodeRelativeNestingLevel = SourceCodeRelativeNestingLevel + ComprasionSourceCodeRelativeNestingLevel
                                        print(f"Обновляем SourceCodeRelativeNestingLevel до {SourceCodeRelativeNestingLevel}")
                                        IsPassOutputList.append((IndexString,CurentSourceCodeTokenIndex,SourceCodeNestingLevel, SourceCodeRelativeNestingLevel))
                                        print(f"Обновляем IsPassList до {IsPassList}")
                                        CounterMatches += 1
                                        ComprasionSourceCodeRelativeNestingLevel = 0
                                        print(f"Сбрасываем ComprasionSourceCodeRelativeNestingLevel до {ComprasionSourceCodeRelativeNestingLevel}")
                                        SourceCodeNestingLevel = StartSourceCodeNestingLevel
                                        SourceCodeRelativeNestingLevel = StartSourceCodeRelativeNestingLevel
                                    if NestingMap[MatchTokenIndex + ComparisonIndex + 1][0] != -1:
                                        SourceCodeRelativeNestingLevel = 0
                                        print(f"Сбрасываем SourceCodeRelativeNestingLevel до {SourceCodeRelativeNestingLevel}")
        else:
            print(f"Выходим из IsPass, возвращаем IsPassList = {IsPassList}")
            return IsPassList, FlagFirstCircle

    if FlagFirstCircle:
        FlagFirstCircle = False
    print(f"Выходим из IsPass, возвращаем IsPassList = {IsPassList}")
    return IsPassOutputList, FlagFirstCircle


def IsInsert(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, IsPassList, FlagFirstCircle,NestingMap):
    MatchNestingLevel = InsertNestingLevel(MatchTokenList)
    print(f"Получен MatchNestingLevel: {MatchNestingLevel}")
    if MatchTokenIndex > 0 and MatchTokenIndex + 1 < len(MatchTokenList):
        print("Проверяем условие для вставки 'Prev'")
        if MatchTokenList[MatchTokenIndex - 1][1] != '...' and MatchTokenList[MatchTokenIndex + 1][1] == '...' :
            print("Условие для вставки 'Prev' выполнено")
            if len(IsPassList) > 1:
                return 0
            else:
                ResultTokenInsert = {'Prev': IsPassList[0][1] - 1}
                print(f"Возвращаем ResultTokenInsert = {ResultTokenInsert}")
                return ResultTokenInsert
        IsInsertOutputList = []
        if IsPassList:
            for IsPassOutput in IsPassList:
                CurentSourceCodeTokenIndex = IsPassOutput[1]
                SourceCodeNestingLevel = IsPassOutput[2]
                SourceCodeRelativeNestingLevel = IsPassOutput[3]
                print("qwer")
                if (MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...') or (MatchTokenList[MatchTokenIndex - 1][1] != "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...'):
                    print("Проверяем условие для вставки 'Next'")
                    SourceCodeTokenIndex = CurentSourceCodeTokenIndex
                    print(f"Инициализируем SourceCodeTokenIndex = {SourceCodeTokenIndex}")
                    while SourceCodeTokenIndex < len(SourceCodeTokenList):
                        print('RTYU')
                        print(f"Итерация цикла с SourceCodeTokenIndex = {SourceCodeTokenIndex}, значение = {SourceCodeTokenList[SourceCodeTokenIndex]}")
                        SourceCodeInsertIndex = SourceCodeTokenIndex
                        if MatchTokenIndex != 1:
                            print("MatchTokenIndex != 1, обновляем SourceCodeNestingLevel")
                            if NestingMap[MatchTokenIndex + 1][0] == -1:
                                SourceCodeRelativeNestingLevel = SourceNestingLevelChange(SourceCodeRelativeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, 0)
                                print(f"обновляем SourceCodeRelativeNestingLevel{SourceCodeRelativeNestingLevel}")
                            SourceCodeNestingLevel = SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, 0)
                            print(f"SourceCodeNestingLevel обновлен до {SourceCodeNestingLevel}")
                        if MatchTokenIndex + 1 < len(MatchTokenList):
                            print("Проверяем следующий токен в MatchTokenList")
                            if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                                print(f"Токены совпадают: SourceCodeTokenList[{SourceCodeTokenIndex}] и MatchTokenList[{MatchTokenIndex + 1}]")
                                StartSourceCodeRelativeNestingLevel = SourceCodeRelativeNestingLevel
                                StartSourceCodeNestingLevel = SourceCodeNestingLevel
                                ComparisonIndex, NumberTokenMatch, NumberTokenSource, SourceCodeNestingLevel, ComparisonSourceCodeNestingLevel,SourceCodeRelativeNestingLevel,  ComprasionSourceCodeRelativeNestingLevel = ComparisonToken(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, SourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle, SourceCodeRelativeNestingLevel,NestingMap)
                                print(f"Результат ComparisonToken: ComparisonIndex = {ComparisonIndex}, NumberTokenMatch = {NumberTokenMatch}, NumberTokenSource = {NumberTokenSource}, SourceCodeNestingLevel = {SourceCodeNestingLevel}, ComparisonSourceCodeNestingLevel = {ComparisonSourceCodeNestingLevel}")
                                if NumberTokenSource == NumberTokenMatch:
                                    if MatchNestingLevel[0] != -1:
                                        if NestingMap[MatchTokenIndex  + ComparisonIndex][0] == SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel:
                                            print("Условие для вставки 'Nextwwww' выполнено (уровни вложенности)")
                                            IsInsertOutputList.append({'Next': SourceCodeInsertIndex})
                                            SourceCodeNestingLevel = StartSourceCodeNestingLevel
                                            SourceCodeRelativeNestingLevel = StartSourceCodeRelativeNestingLevel
                                            SourceCodeTokenIndex += 1
                                        else:
                                            print("Токены совпадают, увеличиваем SourceCodeTokenIndex")
                                            SourceCodeTokenIndex += 1
                                            print(f"SourceCodeTokenIndex увеличен до {SourceCodeTokenIndex}")
                                    else:
                                        if NestingMap[MatchTokenIndex  + ComparisonIndex][1]  == SourceCodeRelativeNestingLevel + ComprasionSourceCodeRelativeNestingLevel:
                                            print("Условие для вставки 'Nextb' выполнено (уровни вложенности)")
                                            IsInsertOutputList.append({'Next': SourceCodeInsertIndex})
                                            SourceCodeNestingLevel = StartSourceCodeNestingLevel
                                            SourceCodeRelativeNestingLevel = StartSourceCodeRelativeNestingLevel
                                            SourceCodeTokenIndex += 1


                                        elif NestingMap[MatchTokenIndex  + ComparisonIndex][1] == 0 and MatchTokenList[MatchTokenIndex + ComparisonIndex][1] not in ["}", ")", "]"]:
                                            print(NestingMap[MatchTokenIndex  + ComparisonIndex])
                                            print("Условие для вставки 'Next' выполнено (уровни вложенности)")
                                            IsInsertOutputList.append({'Next': SourceCodeInsertIndex})
                                            SourceCodeNestingLevel = StartSourceCodeNestingLevel
                                            SourceCodeRelativeNestingLevel = StartSourceCodeRelativeNestingLevel
                                            SourceCodeTokenIndex += 1

                                        else:
                                            print("Токены совпадают, увеличиваем SourceCodeTokenIndex")
                                            SourceCodeTokenIndex += 1
                                            print(f"SourceCodeTokenIndex увеличен до {SourceCodeTokenIndex}")
                                            ComprasionSourceCodeRelativeNestingLevel = 0

                                else:
                                    print("Токены не совпадают, увеличиваем SourceCodeTokenIndex")
                                    SourceCodeTokenIndex += 1
                                    print(f"SourceCodeTokenIndex увеличен до {SourceCodeTokenIndex}")
                            else:
                                print("Токены не совпадают, увеличиваем SourceCodeTokenIndex")
                                SourceCodeTokenIndex += 1
                                print(f"SourceCodeTokenIndex увеличен до {SourceCodeTokenIndex}")
            if len(IsInsertOutputList) > 1:
                return 0
            else:
                return IsInsertOutputList[0]
        else:
            return 0

def InsertNestingLevel(MatchTokenList: list[tuple]):
    CounterNesting = 0
    IsNestingMarkerPairsDictionary = CheckMatchNestingMarkerPairs(MatchTokenList)
    IsNestingDefined = True
    NestingMap = MatchNestingLevelInsertALL(MatchTokenList)
    for i, MatchToken in enumerate(MatchTokenList):
        if MatchToken[1] == ">>>":
            return NestingMap[i]
    return 0


def GetBracketIndicesForEllipsis(MatchTokenList: list[tuple]):
    stack = []
    IsNestingMarkerPairsDictionary = CheckMatchNestingMarkerPairs(MatchTokenList)
    IsNestingDefined = True
    result = []
    for i, MatchToken in enumerate(MatchTokenList):
        if MatchToken[1] == '...' and i > 0:
            bracket_index = stack[-1][0] if stack and IsNestingDefined else -1
            result.append({"EllipsisIndex": i, "BracketIndex": bracket_index})
        elif MatchToken[1] in ["{", "(", "["] and IsNestingMarkerPairsDictionary.get(i, False):
            stack.append((i, MatchToken[1]))
            IsNestingDefined = True
        elif MatchToken[1] in ["}", ")", "]"] and IsNestingMarkerPairsDictionary.get(i, False):
            if stack:
                stack.pop()

    return result


def MatchNestingLevelInsertALL(MatchTokenList: list[tuple]):
    NestingMap = []
    CounterNesting = 0
    CounterRelativeNesting = 0
    IsNestingDefined = True
    BracketIndicesForEllipsis = GetBracketIndicesForEllipsis(MatchTokenList)
    IsNestingMarkerPairsDictionary = CheckMatchNestingMarkerPairs(MatchTokenList)
    BetweenEllipsis = set()

    for i, CurentBracket in enumerate(BracketIndicesForEllipsis):
        for NextBracket in BracketIndicesForEllipsis[i + 1:]:
            if CurentBracket["BracketIndex"] == NextBracket["BracketIndex"] and CurentBracket["BracketIndex"]:
                BetweenEllipsis.update(range(CurentBracket["EllipsisIndex"] + 1, NextBracket["EllipsisIndex"]))
    for i, MatchToken in enumerate(MatchTokenList):
        if i in BetweenEllipsis:
            IsNestingDefined, CounterRelativeNesting = CheckCounterNesting( MatchToken, CounterRelativeNesting, IsNestingDefined, i)
            NestingMap.append((-1,CounterRelativeNesting))
        else:
            IsNestingDefined, CounterNesting = CheckCounterNesting( MatchToken, CounterNesting, IsNestingDefined, i)
            NestingMap.append((CounterNesting if IsNestingDefined else -1,0))
    return NestingMap

def CheckCounterNesting( MatchToken,CounterNesting, IsNestingDefined, index):
    if MatchToken[1] == '...' and index > 0:
        if CounterNesting == 0:
            IsNestingDefined = False
    elif MatchToken[1] in ["{", "(", "["]:
        CounterNesting += 1
        IsNestingDefined = True
    elif MatchToken[1] in ["}", ")", "]"]:
        CounterNesting -= 1
    return IsNestingDefined, CounterNesting

def SearchInsertIndexInSourseCode(MatchTokenList: list[tuple], SourceCodeTokenList: list[tuple]):
    InsertIndexInTokenList = SearchInsertIndexInTokenList(MatchTokenList, SourceCodeTokenList)
    if InsertIndexInTokenList == 0:
        return 0
    TokenDirection, TokenPosition = list(InsertIndexInTokenList.items())[0]
    TokenValue = SourceCodeTokenList[TokenPosition][1]
    CounterIdenticalToken = 0
    for SourceCodeTokenIndex in range(TokenPosition + 1):
        if SourceCodeTokenList[SourceCodeTokenIndex][1] == TokenValue:
            CounterIdenticalToken = CounterIdenticalToken + 1
    return [TokenDirection, CounterIdenticalToken, TokenValue]


def CheckMatchNestingMarkerPairs(MatchTokenList: list[tuple]):
    IsNestingMarkerPairsDictionary = {}
    stack = []
    DictionaryNestingMarker = {')': '(', '}': '{', ']': '['}
    NestingMarkerList = [(i, MatchToken[1]) for i, MatchToken in enumerate(MatchTokenList) if MatchToken[1] in ["{", "(", "[", "}", ")", "]"]]

    for index, _ in NestingMarkerList:
        IsNestingMarkerPairsDictionary[index] = False

    for i, (IndexOnMatch, NestingMarker) in enumerate(NestingMarkerList):
        if NestingMarker in ["{", "(", "["]:
            stack.append((IndexOnMatch, NestingMarker, i))
        elif NestingMarker in ["}", ")", "]"]:
            for j in range(len(stack) - 1, -1, -1):
                if stack[j][1] == DictionaryNestingMarker[NestingMarker]:
                    OpenNestingMarkerIndexOnMatch, _, _ = stack.pop(j)
                    IsNestingMarkerPairsDictionary[OpenNestingMarkerIndexOnMatch] = True
                    IsNestingMarkerPairsDictionary[IndexOnMatch] = True
                    break
    return IsNestingMarkerPairsDictionary