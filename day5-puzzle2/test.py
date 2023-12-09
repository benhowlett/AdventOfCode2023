input = [2906961955, 52237479, 1600322402, 372221628, 2347782594, 164705568, 541904540, 89745770, 126821306, 192539923, 3411274151, 496169308, 919015581, 8667739, 654599767, 160781040, 3945616935, 85197451, 999146581, 344584779]

initialInputLength = 0

for index in range(len(input)):
    if index % 2 == 1: initialInputLength += input[index]

for index, value in enumerate(input):
    input[index] = [value, input[index + 1]]
    del input[index + 1]

input = sorted(input, key=lambda x: x[0])

for index, value in enumerate(input):
    if index < len(input) - 1 and input[index + 1][0] - value[0] <= value[1]:
        if value[0] + value[1] < input[index + 1][0] + input[index + 1][1]:
            value[1] = (input[index + 1][0] + input[index + 1][1]) - value[0]
        del input[index + 1]
    
totalInputLength = 0

for item in input:
    totalInputLength += item[1]

print(initialInputLength, input, totalInputLength) 