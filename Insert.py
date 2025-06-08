from SearchCode import SearchInsertIndexInSourseCode
from ParsingCodeAndInstruction import ReadLine, WriteLine
def Insert(Match, Patch, SourceCode, OutPath, IsNexLine):
    position, count, SearchString = SearchInsertIndexInSourseCode(Match, SourceCode)
    lines = ReadLine(OutPath)
    occurrence = 0
    found = False
    ResultLines = []

    for i, line in enumerate(lines):
        ResultLines.append(line)
        if SearchString in line:
            occurrence += 1
            if occurrence == count:
                found = True
                if position == 'Next':
                    if IsNexLine:
                        ResultLines.append(Patch + '\n')
                    else:
                        ResultLines[-1] = line.rstrip('\n') + Patch + '\n'
                elif position == 'Prev':
                    if IsNexLine:
                        ResultLines[-1] = Patch + '\n' + line
                    else:
                        ResultLines[-1] = Patch + line
                else:
                    return False
    if not found:
        print(f"Вхождение {count} строки '{SearchString}' не найдено в файле")
        return False

    WriteLine(OutPath, ResultLines)
    return True
