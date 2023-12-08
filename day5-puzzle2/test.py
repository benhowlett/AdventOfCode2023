input = [79, 14, 55, 13]

for index, value in enumerate(input):
    input[index] = [value, input[index + 1]]
    del input[index + 1]

input = sorted(input, key=lambda x: x[0])

print(input) 