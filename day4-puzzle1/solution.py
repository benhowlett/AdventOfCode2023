def item_is_in_list(item, list):
    for listItem in list:
        # print(item, listItem)
        if int(listItem) == int(item):
            return True
    return False

input = open('input', 'r')

scratchCards = []

for line in input:
    winningNumbers = line.split('|')[0].strip().split()
    winningNumbers.pop(0)
    winningNumbers.pop(0)
    # print(winningNumbers)

    myNumbers = line.split('|')[1].strip().split()
    # print(myNumbers)

    scratchCards.append([myNumbers, winningNumbers])

total = 0

for scratchCard in scratchCards:
    cardTotal = 0
    for number in scratchCard[0]:
        if item_is_in_list(number, scratchCard[1]):
            if cardTotal == 0:
                cardTotal = 1
            else:
                cardTotal *= 2
    total += cardTotal

print(total)