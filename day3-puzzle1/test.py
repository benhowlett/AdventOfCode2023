input = [['4','6','7','.','.','1','1','4','.','.','.']]

total = 0

for rIndex, row in enumerate(input):
    itemIterator = enumerate(row)
    for cIndex, item in itemIterator:
        print(input[rIndex][cIndex])
        if input[rIndex][cIndex].isnumeric():
            tempNum = []
            tempCol = cIndex
            while input[rIndex][tempCol].isnumeric():
                tempNum.append(input[rIndex][tempCol])
                if tempCol == len(row) - 1:
                    break
                else:
                    tempCol += 1

            [next(itemIterator, None) for _ in range(len(tempNum) - 1)]

