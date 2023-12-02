total = 0

input = open('input', 'r')

for line in input:
    numbersInLine = []
    for item in line:
        if item.isnumeric():
            numbersInLine.append(item)
    total += (int(numbersInLine[0]) * 10) + int(numbersInLine[-1])

print(total)
