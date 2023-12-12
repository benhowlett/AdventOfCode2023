def get_diff_list(list):
    diffList = []
    for i in range(len(list) - 1):
        diffList.append(list[i + 1] - list[i])
    return diffList

def list_is_all_zeroes(list):
    for item in list:
        if item != 0: return False
    return True

def convert_list_items_to_int(list):
    convertedList = []
    for item in list:
        convertedList.append(int(item))
    return convertedList

def extrapolate_previous_value(listOfLists):
    listOfLists[0].append(0)
    for i in range(len(listOfLists) - 1):
        listOfLists[i+1].reverse()
        listOfLists[i+1].append(listOfLists[i+1][-1] - listOfLists[i][-1])
    return listOfLists[-1][-1]


input = open('input.txt', 'r')

sumOfExtrapolatedValues = 0

for line in input:
    reportLine = convert_list_items_to_int(line.strip().split())
    extrapolation = [reportLine]
    while not list_is_all_zeroes(extrapolation[-1]):
        extrapolation.append(get_diff_list(extrapolation[-1]))
    extrapolation.reverse()
    sumOfExtrapolatedValues += extrapolate_previous_value(extrapolation)

print(sumOfExtrapolatedValues)

