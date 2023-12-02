def find_written_number(list):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for index, number in enumerate(numbers):
        if list[:len(number)] == number:
            return True, index + 1
    return False, 0

total = 0

input = open('input', 'r')

for line in input:
    numbersInLine = []
    for index, item in enumerate(line):
        writtenNumberResult = find_written_number(line[index:])
        if item.isnumeric():
            numbersInLine.append(item)
        elif writtenNumberResult[0]:
            numbersInLine.append(writtenNumberResult[1])

    total += (int(numbersInLine[0]) * 10) + int(numbersInLine[-1])

print(total)

