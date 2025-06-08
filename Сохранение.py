
def Search(MatchTokenList,SourceCodeTokenList ):
    ResultTokenInsert = {}
    CurentSourceCodeTokenIndex = 0
    for MatchTokenIndex in range(len(MatchTokenList)):
        if MatchTokenList[MatchTokenIndex][1] == "...":
            for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex,len(SourceCodeTokenList)):
                if MatchTokenIndex+1 < len(MatchTokenList):
                    if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex+1]:
                        ComparisonIndex = 1
                        NumberTokenMatch = 0
                        NumberTokenSource = 0
                        while MatchTokenList[MatchTokenIndex+1+ComparisonIndex][1] != "..." or MatchTokenList[MatchTokenIndex+1+ComparisonIndex][1] != ">>>" or MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) :
                            NumberTokenMatch = NumberTokenMatch + 1
                            if MatchTokenList[MatchTokenIndex+1+ComparisonIndex] != SourceCodeTokenList[SourceCodeTokenIndex+ComparisonIndex + CurentSourceCodeTokenIndex]:
                                CurentSourceCodeTokenIndex = 0
                                break
                            NumberTokenSource = NumberTokenSource + 1
                            ComparisonIndex = ComparisonIndex + 1
                        if NumberTokenSource == NumberTokenMatch:
                            CurentSourceCodeTokenIndex = CurentSourceCodeTokenIndex + ComparisonIndex + SourceCodeTokenIndex
        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            SourceCodeInsertIndex = CurentSourceCodeTokenIndex
            if MatchTokenList[MatchTokenIndex - 1][1] != "..." and MatchTokenList[MatchTokenIndex + 1][1] == "...":
                ResultTokenInsert = {'Prev': SourceCodeInsertIndex}
            if MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][1] != "...":
                for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex,len(SourceCodeTokenList)):
                    ComparisonIndex = 1
                    NumberTokenMatch = 0
                    NumberTokenSource = 0
                    if MatchTokenIndex+1 < len(MatchTokenList):
                        while MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != "..." or MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != ">>>" or MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) :
                            NumberTokenMatch = NumberTokenMatch + 1
                            if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex] != SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex + CurentSourceCodeTokenIndex]:
                                CurentSourceCodeTokenIndex = 0
                                break
                            NumberTokenSource = NumberTokenSource + 1
                            ComparisonIndex = ComparisonIndex + 1

                        if NumberTokenSource == NumberTokenMatch:
                            ResultTokenInsert = { 'Next': SourceCodeInsertIndex}
    return ResultTokenInsert



def Search2(MatchTokenList, SourceCodeTokenList):
    ResultTokenInsert = {}
    print(f"Инициализирован ResultTokenInsert: {ResultTokenInsert}")
    CurentSourceCodeTokenIndex = 0
    print(f"Инициализирован CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")

    for MatchTokenIndex in range(len(MatchTokenList)):
        print(f"Обработка MatchTokenIndex: {MatchTokenIndex}, Токен: {MatchTokenList[MatchTokenIndex]}")

        if MatchTokenList[MatchTokenIndex][1] == '...':
            print(f"Найден '...' на MatchTokenIndex: {MatchTokenIndex}")
            if MatchTokenList[MatchTokenIndex + 1][1] == '>>>':
                MatchTokenIndex = MatchTokenIndex + 1

            for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                print(
                    f"Проверка SourceCodeTokenIndex: {SourceCodeTokenIndex}, CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")

                if MatchTokenIndex + 1 < len(MatchTokenList):
                    print(f"MatchTokenIndex + 1 допустим: {MatchTokenIndex + 1}")

                    if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex] == MatchTokenList[
                        MatchTokenIndex + 1]:
                        print(
                            f"Совпадение найдено: SourceCodeTokenList[{SourceCodeTokenIndex + CurentSourceCodeTokenIndex}] == MatchTokenList[{MatchTokenIndex + 1}]")
                        ComparisonIndex = 1
                        print(f"Инициализирован ComparisonIndex: {ComparisonIndex}")
                        NumberTokenMatch = 0
                        print(f"Инициализирован NumberTokenMatch: {NumberTokenMatch}")
                        NumberTokenSource = 0
                        print(f"Инициализирован NumberTokenSource: {NumberTokenSource}")

                        while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                               MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                            print(
                                f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}, TokenValue: {MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1]}")
                            NumberTokenMatch = NumberTokenMatch + 1
                            print(f"Увеличен NumberTokenMatch: {NumberTokenMatch}")

                            if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex] != SourceCodeTokenList[
                                SourceCodeTokenIndex + ComparisonIndex + CurentSourceCodeTokenIndex]:
                                print(f"Обнаружено несовпадение, сброс CurentSourceCodeTokenIndex на 0")
                                CurentSourceCodeTokenIndex = 0
                                break

                            NumberTokenSource = NumberTokenSource + 1
                            print(f"Увеличен NumberTokenSource: {NumberTokenSource}")
                            ComparisonIndex = ComparisonIndex + 1
                            print(f"Увеличен ComparisonIndex: {ComparisonIndex}")

                        if NumberTokenSource == NumberTokenMatch:
                            print(
                                f"Токены совпали: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                            CurentSourceCodeTokenIndex = CurentSourceCodeTokenIndex + ComparisonIndex + SourceCodeTokenIndex - 1
                            print(f"Обновлен CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
                            break

        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            print(f"Найден '>>>' на MatchTokenIndex: {MatchTokenIndex}")
            SourceCodeInsertIndex = CurentSourceCodeTokenIndex
            print(f"Установлен SourceCodeInsertIndex: {SourceCodeInsertIndex}")

            if MatchTokenList[MatchTokenIndex - 1][1] != '...' and MatchTokenList[MatchTokenIndex + 1][1] == '...':
                print(f"Случай: Предыдущий не '...', следующий '...', установка ResultTokenInsert['Prev']")
                ResultTokenInsert = {'Prev': SourceCodeInsertIndex}
                print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")

            if MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][1] != '..."':
                print(f"Случай: Предыдущий '...', следующий не '...', начало поиска")

                for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                    print(f"Проверка SourceCodeTokenIndex: {SourceCodeTokenIndex}")
                    ComparisonIndex = 1
                    print(f"Инициализирован ComparisonIndex: {ComparisonIndex}")
                    NumberTokenMatch = 0
                    print(f"Инициализирован NumberTokenMatch: {NumberTokenMatch}")
                    NumberTokenSource = 0
                    print(f"Инициализирован NumberTokenSource: {NumberTokenSource}")

                    if MatchTokenIndex + 1 < len(MatchTokenList):
                        print(f"MatchTokenIndex + 1 допустим: {MatchTokenIndex + 1}")

                        while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                               MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                            print(
                                f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}")
                            NumberTokenMatch = NumberTokenMatch + 1
                            print(f"Увеличен NumberTokenMatch: {NumberTokenMatch}")

                            if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex] != SourceCodeTokenList[
                                SourceCodeTokenIndex + ComparisonIndex + CurentSourceCodeTokenIndex]:
                                print(f"Обнаружено несовпадение, сброс CurentSourceCodeTokenIndex на 0")
                                CurentSourceCodeTokenIndex = 0
                                break

                            NumberTokenSource = NumberTokenSource + 1
                            print(f"Увеличен NumberTokenSource: {NumberTokenSource}")
                            ComparisonIndex = ComparisonIndex + 1
                            print(f"Увеличен ComparisonIndex: {ComparisonIndex}")

                        if NumberTokenSource == NumberTokenMatch:
                            print(
                                f"Токены совпали: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                            ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                            print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                            break

    print(f"Возвращается ResultTokenInsert: {ResultTokenInsert}")
    return ResultTokenInsert

def SearchIndexInsertInSource3(MatchTokenList, SourceCodeTokenList):
    ResultTokenInsert = {}
    CurentSourceCodeTokenIndex = 0

    for MatchTokenIndex in range(len(MatchTokenList)):
        if MatchTokenList[MatchTokenIndex][1] == '...':
            skip_rest = False

            if MatchTokenIndex + 1 < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1][1] == '>>>':
                MatchTokenIndex = MatchTokenIndex + 1
                skip_rest = True

            if not skip_rest:
                for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                    if MatchTokenIndex + 1 < len(MatchTokenList):
                        if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex] == MatchTokenList[
                            MatchTokenIndex + 1]:
                            ComparisonIndex = 1
                            NumberTokenMatch = 0
                            NumberTokenSource = 0

                            while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                                   MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                                NumberTokenMatch = NumberTokenMatch + 1

                                if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex] != SourceCodeTokenList[
                                    SourceCodeTokenIndex + ComparisonIndex + CurentSourceCodeTokenIndex]:
                                    CurentSourceCodeTokenIndex = 0
                                    break

                                NumberTokenSource = NumberTokenSource + 1
                                ComparisonIndex = ComparisonIndex + 1

                            if NumberTokenSource == NumberTokenMatch:
                                CurentSourceCodeTokenIndex = CurentSourceCodeTokenIndex + ComparisonIndex + SourceCodeTokenIndex - 1
                                break

        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            SourceCodeInsertIndex = CurentSourceCodeTokenIndex

            if MatchTokenIndex > 0 and MatchTokenIndex + 1 < len(MatchTokenList):
                if MatchTokenList[MatchTokenIndex - 1][1] != '...' and MatchTokenList[MatchTokenIndex + 1][1] == '...':
                    ResultTokenInsert = {'Prev': SourceCodeInsertIndex}

                if MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...':
                    for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                        NumberTokenMatch = 0
                        NumberTokenSource = 0
                        SourceCodeInsertIndex = SourceCodeTokenIndex
                        if MatchTokenIndex + 1 < len(MatchTokenList):
                            if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex] == MatchTokenList[
                                MatchTokenIndex + 1]:
                                ComparisonIndex = 1
                                while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                                       MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                                    NumberTokenMatch = NumberTokenMatch + 1

                                    if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex] != SourceCodeTokenList[
                                        SourceCodeTokenIndex + ComparisonIndex + CurentSourceCodeTokenIndex]:
                                        CurentSourceCodeTokenIndex = 0
                                        break

                                    NumberTokenSource = NumberTokenSource + 1
                                    ComparisonIndex = ComparisonIndex + 1

                                if NumberTokenSource == NumberTokenMatch:
                                    ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                                    break

    return ResultTokenInsert

def SearchIndexInsertInSource4(MatchTokenList: list[tuple], SourceCodeTokenList: list[tuple]):
    ResultTokenInsert = {}
    CurentSourceCodeTokenIndex = 0
    MatchNestingLevel = MatchNestingLevelInsert(MatchTokenList)
    SourceCodeNestingLevel = 0
    for MatchTokenIndex in range(len(MatchTokenList)):
        if MatchTokenList[MatchTokenIndex][1] == '...':
            skip_rest = False

            if MatchTokenIndex + 1 < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1][1] == '>>>':
                MatchTokenIndex = MatchTokenIndex + 1
                skip_rest = True

            if not skip_rest:
                for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                    if MatchTokenIndex + 1 < len(MatchTokenList):
                        if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                            ComparisonIndex = 1
                            NumberTokenMatch = 0
                            NumberTokenSource = 0
                            while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                                   MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                                NumberTokenMatch = NumberTokenMatch + 1
                                if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex + ComparisonIndex] in ["{", "(", "[", "<",]:
                                    SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                                if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex + ComparisonIndex] in ["}", ")", "]", ">", ]:
                                    SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                                if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex] != SourceCodeTokenList[
                                    SourceCodeTokenIndex + ComparisonIndex + CurentSourceCodeTokenIndex]:
                                    if SourceCodeTokenIndex == 0:
                                        SourceCodeNestingLevel = 0
                                    break

                                NumberTokenSource = NumberTokenSource + 1
                                ComparisonIndex = ComparisonIndex + 1

                            if NumberTokenSource == NumberTokenMatch:
                                CurentSourceCodeTokenIndex = CurentSourceCodeTokenIndex + ComparisonIndex + SourceCodeTokenIndex - 1
                                break
                            elif NumberTokenSource == NumberTokenMatch:
                                CurentSourceCodeTokenIndex = CurentSourceCodeTokenIndex + ComparisonIndex
        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            SourceCodeInsertIndex = CurentSourceCodeTokenIndex

            if MatchTokenIndex > 0 and MatchTokenIndex + 1 < len(MatchTokenList):
                if MatchTokenList[MatchTokenIndex - 1][1] != '...' and MatchTokenList[MatchTokenIndex + 1][1] == '...' and MatchNestingLevel == SourceCodeNestingLevel:
                    ResultTokenInsert = {'Prev': SourceCodeInsertIndex}

                if MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...':
                    for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                        NumberTokenMatch = 0
                        NumberTokenSource = 0
                        SourceCodeInsertIndex = SourceCodeTokenIndex
                        if MatchTokenIndex + 1 < len(MatchTokenList):
                            if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                                ComparisonIndex = 1
                                while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                                       MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                                    NumberTokenMatch = NumberTokenMatch + 1
                                    if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex + ComparisonIndex] in ["{","(", "[", "<" ]:
                                        SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                                    if SourceCodeTokenList[SourceCodeTokenIndex + CurentSourceCodeTokenIndex + ComparisonIndex] in ["}",")","]",">" ]:
                                        SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                                    if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex] != SourceCodeTokenList[
                                        SourceCodeTokenIndex + ComparisonIndex + CurentSourceCodeTokenIndex]:
                                        CurentSourceCodeTokenIndex = 0
                                        break

                                    NumberTokenSource = NumberTokenSource + 1
                                    ComparisonIndex = ComparisonIndex + 1

                                if NumberTokenSource == NumberTokenMatch and MatchNestingLevel == SourceCodeNestingLevel:
                                    ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                                    break
                                elif NumberTokenSource == NumberTokenMatch:
                                    CurentSourceCodeTokenIndex = CurentSourceCodeTokenIndex + ComparisonIndex

    return ResultTokenInsert

def SearchIndexInsertInSource5(MatchTokenList: list[tuple], SourceCodeTokenList: list[tuple]):
    ResultTokenInsert = {}
    print(f"Инициализирован ResultTokenInsert: {ResultTokenInsert}")
    CurentSourceCodeTokenIndex = 0
    print(f"Инициализирован CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
    MatchNestingLevel = MatchNestingLevelInsert(MatchTokenList)
    print(f"Инициализирован MatchNestingLevel: {MatchNestingLevel}")
    SourceCodeNestingLevel = 0
    print(f"Инициализирован SourceCodeNestingLevel: {SourceCodeNestingLevel}")

    for MatchTokenIndex in range(len(MatchTokenList)):
        print(f"Обработка MatchTokenIndex: {MatchTokenIndex}, Токен: {MatchTokenList[MatchTokenIndex]}")

        if MatchTokenList[MatchTokenIndex][1] == '...':
            print(f"Найден '...' на MatchTokenIndex: {MatchTokenIndex}")
            skip_rest = False
            print(f"Инициализирован skip_rest: {skip_rest}")

            if MatchTokenIndex + 1 < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1][1] == '>>>':
                print(f"Найден '>>>' на MatchTokenIndex + 1: {MatchTokenIndex + 1}")
                print(f"Обновлен MatchTokenIndex: {MatchTokenIndex}")
                skip_rest = True
                print(f"Установлен skip_rest: {skip_rest}")

            if not skip_rest:
                print(f"skip_rest ложно, продолжаем обработку '...'")
                for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                    print(f"Проверка SourceCodeTokenIndex: {SourceCodeTokenIndex}, CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")

                    if MatchTokenIndex + 1 < len(MatchTokenList):
                        print(f"MatchTokenIndex + 1 допустим: {MatchTokenIndex + 1}, SSourceCodeTokenValue: {SourceCodeTokenList[SourceCodeTokenIndex][1]}")
                        if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                            print(f"Совпадение найдено: SourceCodeTokenList[{SourceCodeTokenIndex }] == MatchTokenList[{MatchTokenIndex + 1}]")
                            ComparisonIndex = 1
                            print(f"Инициализирован ComparisonIndex: {ComparisonIndex}")
                            NumberTokenMatch = 0
                            print(f"Инициализирован NumberTokenMatch: {NumberTokenMatch}")
                            NumberTokenSource = 0
                            print(f"Инициализирован NumberTokenSource: {NumberTokenSource}")
                            if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["{", "(", "["]:
                                SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                                print(f"Обнаружена открывающая скобка 1, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                            if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["}", ")", "]"]:
                                SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                                print(f"Обнаружена закрывающая скобка 1, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")
                            while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                                   MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                                print(f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}, TokenValue: {MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1]}")
                                NumberTokenMatch = NumberTokenMatch + 1
                                print(f"Увеличен NumberTokenMatch: {NumberTokenMatch}")

                                if SourceCodeTokenList[SourceCodeTokenIndex  + ComparisonIndex][1] in ["{", "(", "["]:
                                    SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                                    print(f"Обнаружена открывающая скобка, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                                if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["}", ")", "]"]:
                                    SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                                    print(f"Обнаружена закрывающая скобка, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")

                                if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1]:
                                    print(f"Обнаружено несовпадение токенов")
                                    if MatchTokenIndex == 0:
                                        SourceCodeNestingLevel = 0
                                        print(f"SourceCodeTokenIndex равен 0, сброс SourceCodeNestingLevel: {SourceCodeNestingLevel}")
                                    break
                                print(f"Токены совпадают, продолжаем сравнение")

                                NumberTokenSource = NumberTokenSource + 1
                                print(f"Увеличен NumberTokenSource: {NumberTokenSource}")
                                ComparisonIndex = ComparisonIndex + 1
                                print(f"Увеличен ComparisonIndex: {ComparisonIndex}")

                            if NumberTokenSource == NumberTokenMatch:
                                print(f"Токены совпали: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                CurentSourceCodeTokenIndex =  ComparisonIndex + SourceCodeTokenIndex
                                print(f"Обновлен CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
                                break

        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            print(f"Найден '>>>' на MatchTokenIndex: {MatchTokenIndex}")
            SourceCodeInsertIndex = CurentSourceCodeTokenIndex
            print(f"Установлен SourceCodeInsertIndex: {SourceCodeInsertIndex}")

            if MatchTokenIndex > 0 and MatchTokenIndex + 1 < len(MatchTokenList):
                print(f"Проверка условий для '>>>': MatchTokenIndex > 0 и MatchTokenIndex + 1 < len(MatchTokenList)")
                if MatchTokenList[MatchTokenIndex - 1][1] != '...' and MatchTokenList[MatchTokenIndex + 1][1] == '...' and MatchNestingLevel == SourceCodeNestingLevel:
                    print(f"Случай: Предыдущий не '...', следующий '...', и уровни вложенности совпадают, установка ResultTokenInsert['Prev']")
                    ResultTokenInsert = {'Prev': SourceCodeInsertIndex-1}
                    print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                    return ResultTokenInsert
                if (MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...') or (MatchTokenList[MatchTokenIndex - 1][1] != "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...'):
                    print(f"Случай: Предыдущий '...', следующий не '...' или оба не '...', начало поиска")
                    SourceCodeTokenIndex = CurentSourceCodeTokenIndex
                    while SourceCodeTokenIndex < len(SourceCodeTokenList):
                        print(f"Проверка SourceCodeTokenIndex: {SourceCodeTokenIndex}, SourceCodeTokenValue: {SourceCodeTokenList[SourceCodeTokenIndex][1]}")
                        NumberTokenMatch = 0
                        print(f"Инициализирован NumberTokenMatch: {NumberTokenMatch}")
                        NumberTokenSource = 0
                        print(f"Инициализирован NumberTokenSource: {NumberTokenSource}")
                        SourceCodeInsertIndex = SourceCodeTokenIndex
                        print(f"Установлен SourceCodeInsertIndex: {SourceCodeInsertIndex}")
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["{", "(", "["]  and MatchTokenIndex != 1:
                            SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                            print(f"Обнаружена открывающая скобка, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["}", ")", "]"]  and MatchTokenIndex != 1:
                            SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                            print(f"Обнаружена закрывающая скобка, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")
                        if MatchTokenIndex + 1 < len(MatchTokenList):
                            print(f"MatchTokenIndex + 1 допустим: {MatchTokenIndex + 1}")
                            if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                                print(f"Совпадение найдено: SourceCodeTokenList[{SourceCodeTokenIndex}] == MatchTokenList[{MatchTokenIndex + 1}]")
                                ComparisonIndex = 1
                                print(f"Инициализирован ComparisonIndex: {ComparisonIndex}")

                                while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                                       MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                                    print(f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}")
                                    NumberTokenMatch = NumberTokenMatch + 1
                                    print(f"Увеличен NumberTokenMatch: {NumberTokenMatch}")

                                    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["{", "(", "["]:
                                        SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                                        print(f"Обнаружена открывающая скобка, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                                    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["}", ")", "]"]:
                                        SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                                        print(f"Обнаружена закрывающая скобка, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")

                                    if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1]:
                                        print(f"Обнаружено несовпадение, сброс CurentSourceCodeTokenIndex на 0")
                                        break
                                    print(f"Токены совпадают, продолжаем сравнение")

                                    NumberTokenSource = NumberTokenSource + 1
                                    print(f"Увеличен NumberTokenSource: {NumberTokenSource}")
                                    ComparisonIndex = ComparisonIndex + 1
                                    print(f"Увеличен ComparisonIndex: {ComparisonIndex}")

                                if NumberTokenSource == NumberTokenMatch and MatchNestingLevel - 1 == SourceCodeNestingLevel:
                                    print(f"Токены совпали и уровни вложенности совпадают: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                    ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                                    print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                                    return ResultTokenInsert
                                elif NumberTokenSource == NumberTokenMatch and MatchNestingLevel == 0:
                                    print(f"Токены совпали случай если >>> 2 токен в Match: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                    ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                                    print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                                    return ResultTokenInsert
                                elif NumberTokenSource == NumberTokenMatch:
                                    print(f"Токены совпали уровень вложенности нет")
                                    SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                                    print(f"Обновлен SourceCodeTokenIndex: {SourceCodeTokenIndex}")
                                else:
                                    SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                            else:
                                SourceCodeTokenIndex = SourceCodeTokenIndex + 1
    return 0


def SearchInsertIndexInTokenList6(MatchTokenList: list[tuple], SourceCodeTokenList: list[tuple]):
    ResultTokenInsert = {}
    FlagFirstCircle = True
    print(f"Инициализирован ResultTokenInsert: {ResultTokenInsert}")
    CurentSourceCodeTokenIndex = 0
    print(f"Инициализирован CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
    MatchNestingLevel = InsertNestingLevel(MatchTokenList)
    NestingMap = MatchNestingLevelInsertALL(MatchTokenList)
    FlagEndInsert = IsInsertedAtEndOfNesting(MatchTokenList)
    print(f"Инициализирован MatchNestingLevel: {MatchNestingLevel}")
    SourceCodeNestingLevel = 0
    print(f"Инициализирован SourceCodeNestingLevel: {SourceCodeNestingLevel}")

    for MatchTokenIndex in range(len(MatchTokenList)):
        print(f"Обработка MatchTokenIndex: {MatchTokenIndex}, Токен: {MatchTokenList[MatchTokenIndex]}")

        if MatchTokenList[MatchTokenIndex][1] == '...':
            print(f"Найден '...' на MatchTokenIndex: {MatchTokenIndex}")
            skip_rest = False
            print(f"Инициализирован skip_rest: {skip_rest}")

            if MatchTokenIndex + 1 < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1][1] == '>>>':
                print(f"Найден '>>>' на MatchTokenIndex + 1: {MatchTokenIndex + 1}")
                print(f"Обновлен MatchTokenIndex: {MatchTokenIndex}")
                skip_rest = True
                print(f"Установлен skip_rest: {skip_rest}")

            if not skip_rest:
                print(f"skip_rest ложно, продолжаем обработку '...'")
                for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                    print(
                        f"Проверка SourceCodeTokenIndex: {SourceCodeTokenIndex}, CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
                    if MatchTokenIndex + 1 < len(MatchTokenList):
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["{", "(", "["] and FlagFirstCircle == False:
                            SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                            print(
                                f"Обнаружена открывающая скобка 1, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["}", ")", "]"] and FlagFirstCircle == False:
                            SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                            print(
                                f"Обнаружена закрывающая скобка 1, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")
                        print(
                            f"MatchTokenIndex + 1 допустим: {MatchTokenIndex + 1}, SSourceCodeTokenValue: {SourceCodeTokenList[SourceCodeTokenIndex][1]}")
                        if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                            print(
                                f"Совпадение найдено: SourceCodeTokenList[{SourceCodeTokenIndex}] == MatchTokenList[{MatchTokenIndex + 1}]")
                            ComparisonIndex = 1
                            print(f"Инициализирован ComparisonIndex: {ComparisonIndex}")
                            NumberTokenMatch = 0
                            print(f"Инициализирован NumberTokenMatch: {NumberTokenMatch}")
                            NumberTokenSource = 0
                            print(f"Инициализирован NumberTokenSource: {NumberTokenSource}")
                            ComparisonSourceCodeNestingLevel = 0
                            if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["{", "(", "["] and FlagFirstCircle == True:
                                SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                                print(
                                    f"Обнаружена открывающая скобка 1, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                            if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["}", ")", "]"] and FlagFirstCircle == True:
                                SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                                print(
                                    f"Обнаружена закрывающая скобка 1, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")
                            while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                                   MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                                print(
                                    f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}, TokenValue: {MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1]}")
                                NumberTokenMatch = NumberTokenMatch + 1
                                print(f"Увеличен NumberTokenMatch: {NumberTokenMatch}")

                                if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["{", "(", "["]:
                                    ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel + 1
                                    print(
                                        f"Обнаружена открывающая скобка, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}")
                                if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["}", ")", "]"]:
                                    ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel - 1
                                    print(
                                        f"Обнаружена закрывающая скобка, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}")

                                if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != \
                                        SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1]:
                                    print(f"Обнаружено несовпадение токенов")
                                    ComparisonSourceCodeNestingLevel = 0
                                    break
                                print(f"Токены совпадают, продолжаем сравнение")

                                NumberTokenSource = NumberTokenSource + 1
                                print(f"Увеличен NumberTokenSource: {NumberTokenSource}")
                                ComparisonIndex = ComparisonIndex + 1
                                print(f"Увеличен ComparisonIndex: {ComparisonIndex}")
                                print(f"сравненине SourceCodeNestingLevel с NestingMap: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}, {NestingMap[MatchTokenIndex + 1 + ComparisonIndex]}")

                            if  NumberTokenSource == NumberTokenMatch:
                                if FlagEndInsert and (NestingMap[MatchTokenIndex + 1 + ComparisonIndex] == SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel   or  NestingMap[MatchTokenIndex + 1 + ComparisonIndex] == -1):
                                    print(f"Токены совпали1: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                    CurentSourceCodeTokenIndex = ComparisonIndex + SourceCodeTokenIndex
                                    print(f"Обновлен CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
                                    FlagFirstCircle = False
                                    SourceCodeNestingLevel = SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel
                                    ComparisonSourceCodeNestingLevel = 0
                                    break
                                elif not FlagEndInsert:
                                    print(
                                        f"Токены совпали: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                    CurentSourceCodeTokenIndex = ComparisonIndex + SourceCodeTokenIndex
                                    print(f"Обновлен CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
                                    FlagFirstCircle = False
                                    SourceCodeNestingLevel = SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel
                                    ComparisonSourceCodeNestingLevel = 0
                                    break
        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            print(f"Найден '>>>' на MatchTokenIndex: {MatchTokenIndex}")
            SourceCodeInsertIndex = CurentSourceCodeTokenIndex
            print(f"Установлен SourceCodeInsertIndex: {SourceCodeInsertIndex}")

            if MatchTokenIndex > 0 and MatchTokenIndex + 1 < len(MatchTokenList):
                print(f"Проверка условий для '>>>': MatchTokenIndex > 0 и MatchTokenIndex + 1 < len(MatchTokenList)")
                if MatchTokenList[MatchTokenIndex - 1][1] != '...' and MatchTokenList[MatchTokenIndex + 1][1] == '...' and MatchNestingLevel == SourceCodeNestingLevel:
                    print(
                        f"Случай: Предыдущий не '...', следующий '...', и уровни вложенности совпадают, установка ResultTokenInsert['Prev']")
                    ResultTokenInsert = {'Prev': SourceCodeInsertIndex - 1}
                    print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                    return ResultTokenInsert
                if (MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][
                    1] != '...') or (
                        MatchTokenList[MatchTokenIndex - 1][1] != "..." and MatchTokenList[MatchTokenIndex + 1][
                    1] != '...'):
                    print(f"Случай: Предыдущий '...', следующий не '...' или оба не '...', начало поиска")
                    ComparisonSourceCodeNestingLevel = 0
                    SourceCodeTokenIndex = CurentSourceCodeTokenIndex
                    while SourceCodeTokenIndex < len(SourceCodeTokenList):
                        print(
                            f"Проверка SourceCodeTokenIndex: {SourceCodeTokenIndex}, SourceCodeTokenValue: {SourceCodeTokenList[SourceCodeTokenIndex][1]}")
                        NumberTokenMatch = 0
                        print(f"Инициализирован NumberTokenMatch: {NumberTokenMatch}")
                        NumberTokenSource = 0
                        print(f"Инициализирован NumberTokenSource: {NumberTokenSource}")
                        SourceCodeInsertIndex = SourceCodeTokenIndex
                        print(f"Установлен SourceCodeInsertIndex: {SourceCodeInsertIndex}")
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["{", "(", "["] and MatchTokenIndex != 1:
                            SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                            print(
                                f"Обнаружена открывающая скобка, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["}", ")", "]"] and MatchTokenIndex != 1:
                            SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                            print(
                                f"Обнаружена закрывающая скобка, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")
                        if MatchTokenIndex + 1 < len(MatchTokenList):
                            print(f"MatchTokenIndex + 1 допустим: {MatchTokenIndex + 1}")
                            if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                                print(
                                    f"Совпадение найдено: SourceCodeTokenList[{SourceCodeTokenIndex}] == MatchTokenList[{MatchTokenIndex + 1}]")
                                ComparisonIndex = 1
                                print(f"Инициализирован ComparisonIndex: {ComparisonIndex}")

                                while (MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and
                                       MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]):
                                    print(
                                        f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}")
                                    NumberTokenMatch = NumberTokenMatch + 1
                                    print(f"Увеличен NumberTokenMatch: {NumberTokenMatch}")

                                    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["{", "(","["]:
                                        ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel + 1
                                        print(
                                            f"Обнаружена открывающая скобка, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}")
                                    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["}", ")", "]"]:
                                        ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel - 1
                                        print(
                                            f"Обнаружена закрывающая скобка, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}")

                                    if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != \
                                            SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1]:
                                        print(f"Обнаружено несовпадение, сброс CurentSourceCodeTokenIndex на 0")
                                        break
                                    print(f"Токены совпадают, продолжаем сравнение")

                                    NumberTokenSource = NumberTokenSource + 1
                                    print(f"Увеличен NumberTokenSource: {NumberTokenSource}")
                                    ComparisonIndex = ComparisonIndex + 1
                                    print(f"Увеличен ComparisonIndex: {ComparisonIndex}")

                                if NumberTokenSource == NumberTokenMatch and MatchNestingLevel - 1 == SourceCodeNestingLevel:
                                    print(
                                        f"Токены совпали и уровни вложенности совпадают: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                    ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                                    print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                                    return ResultTokenInsert
                                elif NumberTokenSource == NumberTokenMatch and MatchNestingLevel == 0:
                                    print(
                                        f"Токены совпали случай если >>> 2 токен в Match: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                    ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                                    print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                                    return ResultTokenInsert
                                elif NumberTokenSource == NumberTokenMatch:
                                    print(f"Токены совпали уровень вложенности нет")
                                    SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                                    print(f"Обновлен SourceCodeTokenIndex: {SourceCodeTokenIndex}")
                                else:
                                    SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                            else:
                                SourceCodeTokenIndex = SourceCodeTokenIndex + 1
    return 0




def MatchNestingLevelInsert(MatchTokenList: list[tuple]):
    СounterNesting = 0
    for MatchToken in MatchTokenList:
        if MatchToken[1]  in ["{", "(", "[",]:
            СounterNesting = СounterNesting + 1
        elif MatchToken[1] in ["}", ")", "]", ]:
            СounterNesting = СounterNesting - 1
        elif MatchToken[1] == '>>>':
            break
    return СounterNesting




def SearchInsertIndexInTokenList8(MatchTokenList: list[tuple], SourceCodeTokenList: list[tuple]):
    FlagFirstCircle = True
    CurentSourceCodeTokenIndex = 0
    SourceCodeNestingLevel = 0
    for MatchTokenIndex in range(len(MatchTokenList)):
        if MatchTokenList[MatchTokenIndex][1] == '...':
            CurentSourceCodeTokenIndex, FlagFirstCircle, CurentSourceCodeTokenIndex, SourceCodeNestingLevel = IsPass(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, CurentSourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle)

        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            ResultTokenInsert = IsInsert(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, CurentSourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle)
            return ResultTokenInsert
    return 0


def ComparisonToken(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, SourceCodeTokenIndex, SourceCodeNestingLevel,FlagFirstCircle):
    ComparisonIndex = 1
    NumberTokenMatch = 0
    NumberTokenSource = 0
    ComparisonSourceCodeNestingLevel = 0
    if FlagFirstCircle:
        SourceCodeNestingLevel = SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex)
    while MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]:
        NumberTokenMatch = NumberTokenMatch + 1
        if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["{", "(", "["]:
            ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel + 1
        if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["}", ")", "]"]:
            ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel - 1
        if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1]:
            ComparisonSourceCodeNestingLevel = 0
            break
        NumberTokenSource = NumberTokenSource + 1
        ComparisonIndex = ComparisonIndex + 1
    return ComparisonIndex, NumberTokenMatch, NumberTokenSource, SourceCodeNestingLevel, ComparisonSourceCodeNestingLevel

def SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex):
    if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["{", "(", "["]:
        SourceCodeNestingLevel = SourceCodeNestingLevel + 1
    if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["}", ")", "]"]:
        SourceCodeNestingLevel = SourceCodeNestingLevel - 1
    return SourceCodeNestingLevel

def IsPass(MatchTokenList, MatchTokenIndex,SourceCodeTokenList, CurentSourceCodeTokenIndex, SourceCodeNestingLevel,  FlagFirstCircle):
    NestingMap = MatchNestingLevelInsertALL(MatchTokenList)
    skip_rest = False
    if MatchTokenIndex + 1 < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1][1] == '>>>':
        skip_rest = True
    if not skip_rest:
        for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
            if MatchTokenIndex + 1 < len(MatchTokenList):
                if not FlagFirstCircle:
                    SourceCodeNestingLevel = SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex)
                if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                    ComparisonIndex, NumberTokenMatch, NumberTokenSource, SourceCodeNestingLevel, ComparisonSourceCodeNestingLevel = ComparisonToken(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, SourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle)
                    if NumberTokenSource == NumberTokenMatch:
                        if NestingMap[MatchTokenIndex + 1 + ComparisonIndex] == SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel or NestingMap[MatchTokenIndex + 1 + ComparisonIndex] == -1:
                            CurentSourceCodeTokenIndex = ComparisonIndex + SourceCodeTokenIndex
                            FlagFirstCircle = False
                            SourceCodeNestingLevel = SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel
                            ComparisonSourceCodeNestingLevel = 0
                            break
    return CurentSourceCodeTokenIndex, FlagFirstCircle, CurentSourceCodeTokenIndex, SourceCodeNestingLevel

def IsInsert(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, CurentSourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle):
    MatchNestingLevel = InsertNestingLevel(MatchTokenList)
    SourceCodeInsertIndex = CurentSourceCodeTokenIndex
    if MatchTokenIndex > 0 and MatchTokenIndex + 1 < len(MatchTokenList):
        if MatchTokenList[MatchTokenIndex - 1][1] != '...' and MatchTokenList[MatchTokenIndex + 1][1] == '...' and (MatchNestingLevel == SourceCodeNestingLevel or MatchNestingLevel == -1):
            ResultTokenInsert = {'Prev': SourceCodeInsertIndex - 1}
            return ResultTokenInsert
        if (MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...') or (MatchTokenList[MatchTokenIndex - 1][1] != "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...'):
            SourceCodeTokenIndex = CurentSourceCodeTokenIndex
            while SourceCodeTokenIndex < len(SourceCodeTokenList):
                SourceCodeInsertIndex = SourceCodeTokenIndex
                if MatchTokenIndex != 1:
                    SourceCodeNestingLevel = SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex)
                if MatchTokenIndex + 1 < len(MatchTokenList):
                    if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                        ComparisonIndex, NumberTokenMatch, NumberTokenSource, SourceCodeNestingLevel, ComparisonSourceCodeNestingLevel = ComparisonToken(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, SourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle)
                        if NumberTokenSource == NumberTokenMatch and MatchNestingLevel - 1 == SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel:
                            ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                            return ResultTokenInsert
                        elif NumberTokenSource == NumberTokenMatch and MatchNestingLevel == 0:
                            ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                            return ResultTokenInsert
                        elif NumberTokenSource == NumberTokenMatch:
                            SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                        else:
                            SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                    else:
                        SourceCodeTokenIndex = SourceCodeTokenIndex + 1


def SearchInsertIndexInTokenList7(MatchTokenList: list[tuple], SourceCodeTokenList: list[tuple]):
    ResultTokenInsert = {}
    FlagFirstCircle = True
    print(f"Инициализирован ResultTokenInsert: {ResultTokenInsert}")
    CurentSourceCodeTokenIndex = 0
    print(f"Инициализирован CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
    MatchNestingLevel = InsertNestingLevel(MatchTokenList)
    NestingMap = MatchNestingLevelInsertALL(MatchTokenList)
    print(f"Инициализирован MatchNestingLevel: {MatchNestingLevel}")
    SourceCodeNestingLevel = 0
    print(f"Инициализирован SourceCodeNestingLevel: {SourceCodeNestingLevel}")
    for MatchTokenIndex in range(len(MatchTokenList)):
        print(f"Обработка MatchTokenIndex: {MatchTokenIndex}, Токен: {MatchTokenList[MatchTokenIndex]}")
        if MatchTokenList[MatchTokenIndex][1] == '...':
            print(f"Найден '...' на MatchTokenIndex: {MatchTokenIndex}")
            skip_rest = False
            print(f"Инициализирован skip_rest: {skip_rest}")
            if MatchTokenIndex + 1 < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1][1] == '>>>':
                print(f"Найден '>>>' на MatchTokenIndex + 1: {MatchTokenIndex + 1}")
                print(f"Обновлен MatchTokenIndex: {MatchTokenIndex}")
                skip_rest = True
                print(f"Установлен skip_rest: {skip_rest}")
            if not skip_rest:
                print(f"skip_rest ложно, продолжаем обработку '...'")
                for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
                    print(f"Проверка SourceCodeTokenIndex: {SourceCodeTokenIndex}, CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
                    if MatchTokenIndex + 1 < len(MatchTokenList):
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["{", "(", "["] and FlagFirstCircle == False:
                            SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                            print(f"Обнаружена открывающая скобка 1, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["}", ")", "]"] and FlagFirstCircle == False:
                            SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                            print(f"Обнаружена закрывающая скобка 1, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")
                        print(f"MatchTokenIndex + 1 допустим: {MatchTokenIndex + 1}, SSourceCodeTokenValue: {SourceCodeTokenList[SourceCodeTokenIndex][1]}")
                        if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                            print(f"Совпадение найдено: SourceCodeTokenList[{SourceCodeTokenIndex}] == MatchTokenList[{MatchTokenIndex + 1}]")
                            ComparisonIndex = 1
                            print(f"Инициализирован ComparisonIndex: {ComparisonIndex}")
                            NumberTokenMatch = 0
                            print(f"Инициализирован NumberTokenMatch: {NumberTokenMatch}")
                            NumberTokenSource = 0
                            print(f"Инициализирован NumberTokenSource: {NumberTokenSource}")
                            ComparisonSourceCodeNestingLevel = 0
                            if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["{", "(", "["] and FlagFirstCircle == True:
                                SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                                print(f"Обнаружена открывающая скобка 1, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                            if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["}", ")", "]"] and FlagFirstCircle == True:
                                SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                                print(f"Обнаружена закрывающая скобка 1, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")
                            while MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]:
                                print(f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}, TokenValue: {MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1]}")
                                NumberTokenMatch = NumberTokenMatch + 1
                                print(f"Увеличен NumberTokenMatch: {NumberTokenMatch}")
                                if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["{", "(", "["]:
                                    ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel + 1
                                    print(f"Обнаружена открывающая скобка, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}")
                                if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["}", ")", "]"]:
                                    ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel - 1
                                    print(f"Обнаружена закрывающая скобка, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}")
                                if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1]:
                                    print(f"Обнаружено несовпадение токенов")
                                    ComparisonSourceCodeNestingLevel = 0
                                    break
                                print(f"Токены совпадают, продолжаем сравнение")
                                NumberTokenSource = NumberTokenSource + 1
                                print(f"Увеличен NumberTokenSource: {NumberTokenSource}")
                                ComparisonIndex = ComparisonIndex + 1
                                print(f"Увеличен ComparisonIndex: {ComparisonIndex}")
                                print(f"сравненине SourceCodeNestingLevel с NestingMap: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}, {NestingMap[MatchTokenIndex + 1 + ComparisonIndex]}")
                            if NumberTokenSource == NumberTokenMatch:
                                if NestingMap[MatchTokenIndex + 1 + ComparisonIndex] == SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel or NestingMap[MatchTokenIndex + 1 + ComparisonIndex] == -1:
                                    print(f"Токены совпали1: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                    print(NestingMap[MatchTokenIndex + 1 + ComparisonIndex], MatchTokenIndex + 1 + ComparisonIndex)
                                    CurentSourceCodeTokenIndex = ComparisonIndex + SourceCodeTokenIndex
                                    print(f"Обновлен CurentSourceCodeTokenIndex: {CurentSourceCodeTokenIndex}")
                                    FlagFirstCircle = False
                                    SourceCodeNestingLevel = SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel
                                    ComparisonSourceCodeNestingLevel = 0
                                    break

        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            print(f"Найден '>>>' на MatchTokenIndex: {MatchTokenIndex}")
            SourceCodeInsertIndex = CurentSourceCodeTokenIndex
            print(f"Установлен SourceCodeInsertIndex: {SourceCodeInsertIndex}")
            if MatchTokenIndex > 0 and MatchTokenIndex + 1 < len(MatchTokenList):
                print(f"Проверка условий для '>>>': MatchTokenIndex > 0 и MatchTokenIndex + 1 < len(MatchTokenList)")
                if MatchTokenList[MatchTokenIndex - 1][1] != '...' and MatchTokenList[MatchTokenIndex + 1][1] == '...' and (MatchNestingLevel == SourceCodeNestingLevel or MatchNestingLevel == -1):
                    print(f"Случай: Предыдущий не '...', следующий '...', и уровни вложенности совпадают, установка ResultTokenInsert['Prev']")
                    ResultTokenInsert = {'Prev': SourceCodeInsertIndex - 1}
                    print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                    return ResultTokenInsert
                if (MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...') or (MatchTokenList[MatchTokenIndex - 1][1] != "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...'):
                    print(f"Случай: Предыдущий '...', следующий не '...' или оба не '...', начало поиска")
                    SourceCodeTokenIndex = CurentSourceCodeTokenIndex
                    while SourceCodeTokenIndex < len(SourceCodeTokenList):
                        print(f"Проверка SourceCodeTokenIndex: {SourceCodeTokenIndex}, SourceCodeTokenValue: {SourceCodeTokenList[SourceCodeTokenIndex][1]}")
                        NumberTokenMatch = 0
                        print(f"Инициализирован NumberTokenMatch: {NumberTokenMatch}")
                        NumberTokenSource = 0
                        print(f"Инициализирован NumberTokenSource: {NumberTokenSource}")
                        SourceCodeInsertIndex = SourceCodeTokenIndex
                        print(f"Установлен SourceCodeInsertIndex: {SourceCodeInsertIndex}")
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["{", "(", "["] and MatchTokenIndex != 1:
                            SourceCodeNestingLevel = SourceCodeNestingLevel + 1
                            print(f"Обнаружена открывающая скобка, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel}")
                        if SourceCodeTokenList[SourceCodeTokenIndex][1] in ["}", ")", "]"] and MatchTokenIndex != 1:
                            SourceCodeNestingLevel = SourceCodeNestingLevel - 1
                            print(f"Обнаружена закрывающая скобка, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel}")
                        if MatchTokenIndex + 1 < len(MatchTokenList):
                            print(f"MatchTokenIndex + 1 допустим: {MatchTokenIndex + 1}")
                            if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                                ComparisonSourceCodeNestingLevel = 0
                                print(f"Совпадение найдено: SourceCodeTokenList[{SourceCodeTokenIndex}] == MatchTokenList[{MatchTokenIndex + 1}]")
                                ComparisonIndex = 1
                                print(f"Инициализирован ComparisonIndex: {ComparisonIndex}")
                                while MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]:
                                    print(f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}")
                                    NumberTokenMatch = NumberTokenMatch + 1
                                    print(f"Увеличен NumberTokenMatch: {NumberTokenMatch}")
                                    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["{", "(", "["]:
                                        ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel + 1
                                        print(f"Обнаружена открывающая скобка, SourceCodeNestingLevel увеличен: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}")
                                    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["}", ")", "]"]:
                                        ComparisonSourceCodeNestingLevel = ComparisonSourceCodeNestingLevel - 1
                                        print(f"Обнаружена закрывающая скобка, SourceCodeNestingLevel уменьшен: {SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel}")
                                    if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1]:
                                        print(f"Обнаружено несовпадение, сброс CurentSourceCodeTokenIndex на 0")
                                        break
                                    print(f"Токены совпадают, продолжаем сравнение")
                                    NumberTokenSource = NumberTokenSource + 1
                                    print(f"Увеличен NumberTokenSource: {NumberTokenSource}")
                                    ComparisonIndex = ComparisonIndex + 1
                                    print(f"Увеличен ComparisonIndex: {ComparisonIndex}")
                                if NumberTokenSource == NumberTokenMatch and MatchNestingLevel - 1 == SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel:
                                    print(f"Токены совпали и уровни вложенности совпадают: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                    ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                                    print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                                    return ResultTokenInsert
                                elif NumberTokenSource == NumberTokenMatch and MatchNestingLevel == 0:
                                    print(f"Токены совпали случай если >>> 2 токен в Match: NumberTokenSource ({NumberTokenSource}) == NumberTokenMatch ({NumberTokenMatch})")
                                    ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                                    print(f"Обновлен ResultTokenInsert: {ResultTokenInsert}")
                                    return ResultTokenInsert
                                elif NumberTokenSource == NumberTokenMatch:
                                    print(f"Токены совпали уровень вложенности нет")
                                    SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                                    print(f"Обновлен SourceCodeTokenIndex: {SourceCodeTokenIndex}")
                                else:
                                    SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                            else:
                                SourceCodeTokenIndex = SourceCodeTokenIndex + 1
    return 0
---------------------------------------------Search9----------------------------------------------------------------------------------------------------------
def SearchInsertIndexInTokenList(MatchTokenList: list[tuple], SourceCodeTokenList: list[tuple]):
    print("Входим в функцию SearchInsertIndexInTokenList с MatchTokenList и SourceCodeTokenList")
    FlagFirstCircle = True
    print(f"Инициализируем FlagFirstCircle значением {FlagFirstCircle}")
    CurentSourceCodeTokenIndex = 0
    print(f"Инициализируем CurentSourceCodeTokenIndex значением {CurentSourceCodeTokenIndex}")
    SourceCodeNestingLevel = 0
    print(f"Инициализируем SourceCodeNestingLevel значением {SourceCodeNestingLevel}")
    for MatchTokenIndex in range(len(MatchTokenList)):
        print(f"Начинаем итерацию цикла с MatchTokenIndex = {MatchTokenIndex}")
        if MatchTokenList[MatchTokenIndex][1] == '...':
            print(f"Обнаружен '...' в MatchTokenList[{MatchTokenIndex}]")
            CurentSourceCodeTokenIndex, FlagFirstCircle, _, SourceCodeNestingLevel = IsPass(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, CurentSourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle)
            print(f"После вызова IsPass: CurentSourceCodeTokenIndex = {CurentSourceCodeTokenIndex}, FlagFirstCircle = {FlagFirstCircle}, SourceCodeNestingLevel = {SourceCodeNestingLevel}")
        if MatchTokenList[MatchTokenIndex][1] == ">>>":
            print(f"Обнаружен '>>>' в MatchTokenList[{MatchTokenIndex}]")
            ResultTokenInsert = IsInsert(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, CurentSourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle)
            print(f"Получен результат от IsInsert: {ResultTokenInsert}")
            return ResultTokenInsert
    print("Цикл завершен, возвращаем 0")
    return 0


def ComparisonToken(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, SourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle):
    print(f"Входим в функцию ComparisonToken с MatchTokenIndex = {MatchTokenIndex}, SourceCodeTokenIndex = {SourceCodeTokenIndex}")
    ComparisonIndex = 1
    print(f"Инициализируем ComparisonIndex значением {ComparisonIndex}")
    NumberTokenMatch = 0
    print(f"Инициализируем NumberTokenMatch значением {NumberTokenMatch}")
    NumberTokenSource = 0
    print(f"Инициализируем NumberTokenSource значением {NumberTokenSource}")
    ComparisonSourceCodeNestingLevel = 0
    print(f"Инициализируем ComparisonSourceCodeNestingLevel значением {ComparisonSourceCodeNestingLevel}")
    if FlagFirstCircle:
        print("FlagFirstCircle = True, обновляем SourceCodeNestingLevel")
        SourceCodeNestingLevel = SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, 0)
        print(f"SourceCodeNestingLevel обновлен до {SourceCodeNestingLevel}")
    while MatchTokenIndex + 1 + ComparisonIndex < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] not in ["...", ">>>"]:
        print(f"Сравнение токенов на MatchTokenIndex + 1 + ComparisonIndex: {MatchTokenIndex + 1 + ComparisonIndex}, ComparisonIndex: {ComparisonIndex}, значение = {SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex]}")
        NumberTokenMatch = NumberTokenMatch + 1
        print(f"В цикле while, ComparisonIndex = {ComparisonIndex}")
        ComparisonSourceCodeNestingLevel = SourceNestingLevelChange(ComparisonSourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, ComparisonIndex)
        print(f"Обновлен ComparisonSourceCodeNestingLevel до {ComparisonSourceCodeNestingLevel}")
        if MatchTokenList[MatchTokenIndex + 1 + ComparisonIndex][1] != SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1]:
            print(f"Токены не совпадают: MatchTokenList[{MatchTokenIndex + 1 + ComparisonIndex}] и SourceCodeTokenList[{SourceCodeTokenIndex + ComparisonIndex}]")
            ComparisonSourceCodeNestingLevel = 0
            print(f"Сбрасываем ComparisonSourceCodeNestingLevel до {ComparisonSourceCodeNestingLevel}")
            break
        NumberTokenSource = NumberTokenSource + 1
        print(f"Увеличиваем NumberTokenSource до {NumberTokenSource}")
        ComparisonIndex = ComparisonIndex + 1
        print(f"Увеличиваем ComparisonIndex до {ComparisonIndex}")
    print(f"Выходим из ComparisonToken, возвращаем: ComparisonIndex = {ComparisonIndex}, NumberTokenMatch = {NumberTokenMatch}, NumberTokenSource = {NumberTokenSource}, SourceCodeNestingLevel = {SourceCodeNestingLevel}, ComparisonSourceCodeNestingLevel = {ComparisonSourceCodeNestingLevel}")
    return ComparisonIndex, NumberTokenMatch, NumberTokenSource, SourceCodeNestingLevel, ComparisonSourceCodeNestingLevel


def SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, ComparisonIndex):
    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["{", "(", "["]:
        SourceCodeNestingLevel = SourceCodeNestingLevel + 1
        print(f"SourceCodeNestingLevel увеличен до {SourceCodeNestingLevel}")
    if SourceCodeTokenList[SourceCodeTokenIndex + ComparisonIndex][1] in ["}", ")", "]"]:
        SourceCodeNestingLevel = SourceCodeNestingLevel - 1
        print(f"SourceCodeNestingLevel уменьшен до {SourceCodeNestingLevel}")
    return SourceCodeNestingLevel


def IsPass(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, CurentSourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle):
    print(f"Входим в функцию IsPass с MatchTokenIndex = {MatchTokenIndex}, CurentSourceCodeTokenIndex = {CurentSourceCodeTokenIndex}")
    NestingMap = MatchNestingLevelInsertALL(MatchTokenList)
    print(f"Получена NestingMap: {NestingMap}")
    skip_rest = False
    print(f"Инициализируем skip_rest = {skip_rest}")
    if MatchTokenIndex + 1 < len(MatchTokenList) and MatchTokenList[MatchTokenIndex + 1][1] == '>>>':
        print(f"Следующий токен '>>>', устанавливаем skip_rest = True")
        skip_rest = True
    if not skip_rest:
        print("skip_rest = False, начинаем цикл по SourceCodeTokenList")
        for SourceCodeTokenIndex in range(CurentSourceCodeTokenIndex, len(SourceCodeTokenList)):
            print(f"Итерация цикла с SourceCodeTokenIndex = {SourceCodeTokenIndex}, значение = {SourceCodeTokenList[SourceCodeTokenIndex]} ")
            if MatchTokenIndex + 1 < len(MatchTokenList):
                if not FlagFirstCircle:
                    print("FlagFirstCircle = False, обновляем SourceCodeNestingLevel")
                    SourceCodeNestingLevel = SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, 0)
                if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                    print(f"Токены совпадают: SourceCodeTokenList[{SourceCodeTokenIndex}] и MatchTokenList[{MatchTokenIndex + 1}]")
                    ComparisonIndex, NumberTokenMatch, NumberTokenSource, SourceCodeNestingLevel, ComparisonSourceCodeNestingLevel = ComparisonToken(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, SourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle)
                    print(f"Результат ComparisonToken: ComparisonIndex = {ComparisonIndex}, NumberTokenMatch = {NumberTokenMatch}, NumberTokenSource = {NumberTokenSource}, SourceCodeNestingLevel = {SourceCodeNestingLevel}, ComparisonSourceCodeNestingLevel = {ComparisonSourceCodeNestingLevel}")
                    if NumberTokenSource == NumberTokenMatch:
                        print("NumberTokenSource равно NumberTokenMatch, проверяем уровни вложенности")
                        if NestingMap[MatchTokenIndex  + ComparisonIndex][0] == SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel or NestingMap[MatchTokenIndex  + ComparisonIndex][0] == -1:
                            print("Уровни вложенности совпадают или NestingMap = -1")
                            CurentSourceCodeTokenIndex = ComparisonIndex + SourceCodeTokenIndex
                            print(f"Обновляем CurentSourceCodeTokenIndex до {CurentSourceCodeTokenIndex}")
                            FlagFirstCircle = False
                            print(f"Устанавливаем FlagFirstCircle = {FlagFirstCircle}")
                            SourceCodeNestingLevel = SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel
                            print(f"Обновляем SourceCodeNestingLevel до {SourceCodeNestingLevel}")
                            ComparisonSourceCodeNestingLevel = 0
                            print(f"Сбрасываем ComparisonSourceCodeNestingLevel до {ComparisonSourceCodeNestingLevel}")
                            break
    print(f"Выходим из IsPass, возвращаем: CurentSourceCodeTokenIndex = {CurentSourceCodeTokenIndex}, FlagFirstCircle = {FlagFirstCircle}, SourceCodeNestingLevel = {SourceCodeNestingLevel}")
    return CurentSourceCodeTokenIndex, FlagFirstCircle, CurentSourceCodeTokenIndex, SourceCodeNestingLevel


def IsInsert(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, CurentSourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle):
    print(f"Входим в функцию IsInsert с MatchTokenIndex = {MatchTokenIndex}, CurentSourceCodeTokenIndex = {CurentSourceCodeTokenIndex}")
    MatchNestingLevel = InsertNestingLevel(MatchTokenList)
    print(f"Получен MatchNestingLevel: {MatchNestingLevel}")
    SourceCodeInsertIndex = CurentSourceCodeTokenIndex
    print(f"Инициализируем SourceCodeInsertIndex = {SourceCodeInsertIndex}")
    if MatchTokenIndex > 0 and MatchTokenIndex + 1 < len(MatchTokenList):
        print("Проверяем условие для вставки 'Prev'")
        if MatchTokenList[MatchTokenIndex - 1][1] != '...' and MatchTokenList[MatchTokenIndex + 1][1] == '...' and (MatchNestingLevel[0] == SourceCodeNestingLevel or MatchNestingLevel[0] == -1):
            print("Условие для вставки 'Prev' выполнено")
            ResultTokenInsert = {'Prev': SourceCodeInsertIndex - 1}
            print(f"Возвращаем ResultTokenInsert = {ResultTokenInsert}")
            return ResultTokenInsert
        if (MatchTokenList[MatchTokenIndex - 1][1] == "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...') or (MatchTokenList[MatchTokenIndex - 1][1] != "..." and MatchTokenList[MatchTokenIndex + 1][1] != '...'):
            print("Проверяем условие для вставки 'Next'")
            SourceCodeTokenIndex = CurentSourceCodeTokenIndex
            print(f"Инициализируем SourceCodeTokenIndex = {SourceCodeTokenIndex}")
            while SourceCodeTokenIndex < len(SourceCodeTokenList):
                print(f"Итерация цикла с SourceCodeTokenIndex = {SourceCodeTokenIndex}, значение = {SourceCodeTokenList[SourceCodeTokenIndex]}")
                SourceCodeInsertIndex = SourceCodeTokenIndex
                if MatchTokenIndex != 1:
                    print("MatchTokenIndex != 1, обновляем SourceCodeNestingLevel")
                    SourceCodeNestingLevel = SourceNestingLevelChange(SourceCodeNestingLevel, SourceCodeTokenList, SourceCodeTokenIndex, 0)
                    print(f"SourceCodeNestingLevel обновлен до {SourceCodeNestingLevel}")
                if MatchTokenIndex + 1 < len(MatchTokenList):
                    print("Проверяем следующий токен в MatchTokenList")
                    if SourceCodeTokenList[SourceCodeTokenIndex] == MatchTokenList[MatchTokenIndex + 1]:
                        print(f"Токены совпадают: SourceCodeTokenList[{SourceCodeTokenIndex}] и MatchTokenList[{MatchTokenIndex + 1}]")
                        ComparisonIndex, NumberTokenMatch, NumberTokenSource, SourceCodeNestingLevel, ComparisonSourceCodeNestingLevel = ComparisonToken(MatchTokenList, MatchTokenIndex, SourceCodeTokenList, SourceCodeTokenIndex, SourceCodeNestingLevel, FlagFirstCircle)
                        print(f"Результат ComparisonToken: ComparisonIndex = {ComparisonIndex}, NumberTokenMatch = {NumberTokenMatch}, NumberTokenSource = {NumberTokenSource}, SourceCodeNestingLevel = {SourceCodeNestingLevel}, ComparisonSourceCodeNestingLevel = {ComparisonSourceCodeNestingLevel}")
                        if NumberTokenSource == NumberTokenMatch and (MatchNestingLevel[0] - 1 == SourceCodeNestingLevel + ComparisonSourceCodeNestingLevel or MatchNestingLevel[0] == -1):
                            print("Условие для вставки 'Next' выполнено (уровни вложенности)")
                            ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                            print(f"Возвращаем ResultTokenInsert = {ResultTokenInsert}")
                            return ResultTokenInsert
                        elif NumberTokenSource == NumberTokenMatch and MatchNestingLevel[0] == 0:
                            print("Условие для вставки 'Next' выполнено (MatchNestingLevel = 0)")
                            ResultTokenInsert = {'Next': SourceCodeInsertIndex}
                            print(f"Возвращаем ResultTokenInsert = {ResultTokenInsert}")
                            return ResultTokenInsert
                        elif NumberTokenSource == NumberTokenMatch:
                            print("Токены совпадают, увеличиваем SourceCodeTokenIndex")
                            SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                            print(f"SourceCodeTokenIndex увеличен до {SourceCodeTokenIndex}")
                        else:
                            print("Токены не совпадают, увеличиваем SourceCodeTokenIndex")
                            SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                            print(f"SourceCodeTokenIndex увеличен до {SourceCodeTokenIndex}")
                    else:
                        print("Токены не совпадают, увеличиваем SourceCodeTokenIndex")
                        SourceCodeTokenIndex = SourceCodeTokenIndex + 1
                        print(f"SourceCodeTokenIndex увеличен до {SourceCodeTokenIndex}")
    print("Условия для вставки не выполнены, возвращаем 0")
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