def is_next_to_symbol(row, col, schematic):
    if row == 0:
        minRow = row
    else:
        minRow = row - 1

    if col == 0:
        minCol = col
    else:
        minCol = col - 1

    if row == len(schematic) - 1:
        maxRow = row
    else:
        maxRow = row + 1

    if col == len(schematic[0]) - 2:
        maxCol = col
    else:
        maxCol = col + 1

    for r in range(minRow, maxRow + 1):
        for c in range(minCol, maxCol + 1):
            if not (schematic[r][c].isnumeric() or schematic[r][c] == "."):
                return True
            
    return False

def number_list_to_int(numList):
    numList.reverse()
    multiplier = 1
    calculatedNumber = 0
    for digit in range(len(numList)):
        calculatedNumber += int(numList[digit]) * multiplier
        multiplier *= 10
    print(calculatedNumber)
    return calculatedNumber


input = open('input', 'r')
output = open('output.txt', 'w')

schematic = []

for line in input:
    tempRow = []
    for item in line:
        tempRow.append(item)
    schematic.append(tempRow)

total = 0

for rIndex, row in enumerate(schematic):
    itemIterator = enumerate(row)
    for cIndex, item in itemIterator:
        if schematic[rIndex][cIndex].isnumeric():
            tempNum = []
            tempCol = cIndex
            while schematic[rIndex][tempCol].isnumeric():
                tempNum.append(schematic[rIndex][tempCol])
                if tempCol == len(row) - 1:
                    break
                else:
                    tempCol += 1
            
            isNextToSymbol = False
            for digit in range(len(tempNum)):
                if is_next_to_symbol(rIndex, cIndex + digit, schematic):
                    isNextToSymbol = True
                    break
            
            if isNextToSymbol:
                number = number_list_to_int(tempNum)
                total += number
                output.write(str(number)+'\n')

            [next(itemIterator, None) for _ in range(len(tempNum) - 1)]

print(total)
