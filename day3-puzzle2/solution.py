def number_list_to_int(numList):
    numList.reverse()
    multiplier = 1
    calculatedNumber = 0
    for digit in range(len(numList)):
        calculatedNumber += int(numList[digit]) * multiplier
        multiplier *= 10
    return calculatedNumber

input = open('input', 'r')

numbers = []
gears = []

for rIndex, row in enumerate(input):
    itemIterator = enumerate(row)
    for cIndex, item in itemIterator:
        if item.isnumeric():
            tempNum = []
            tempCol = cIndex
            while row[tempCol].isnumeric():
                tempNum.append(row[tempCol])
                if tempCol == len(row) - 1:
                    break
                else:
                    tempCol += 1
            numbers.append((number_list_to_int(tempNum), rIndex, cIndex, cIndex + len(tempNum) - 1))
            [next(itemIterator, None) for _ in range(len(tempNum) - 1)]
        elif item == "*":
            gears.append((rIndex, cIndex))

total = 0

for gear in gears:
    adjacentNumbers = []
    for number in numbers:
        if number[1] == gear[0] or number[1] == gear[0] - 1 or number[1] == gear[0] + 1:
            if (number[2] == gear[1] or number[2] == gear[1] - 1 or number[2] == gear[1] + 1) or (number[3] == gear[1] or number[3] == gear[1] - 1 or number[3] == gear[1] + 1):
                adjacentNumbers.append(number)
    
    if len(adjacentNumbers) == 2:
        total += adjacentNumbers[0][0] * adjacentNumbers[1][0]


print(total)
