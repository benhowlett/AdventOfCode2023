class ScratchCard:

    def __init__(self, myNumbers, winningNumbers, qty):
        self.myNumbers = myNumbers
        self.winningNumbers = winningNumbers
        self.qty = qty

    def add_copies(self, copies):
        self.qty += copies

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
    cardNumber = winningNumbers.pop(0)
    # print(winningNumbers)

    myNumbers = line.split('|')[1].strip().split()
    # print(myNumbers)

    scratchCards.append(ScratchCard(myNumbers, winningNumbers, 1))

totalCards = 0

for index, scratchCard in enumerate(scratchCards):
    winningNumbersOnCard = 0
    
    for number in scratchCard.myNumbers:
        if item_is_in_list(number, scratchCard.winningNumbers):
            winningNumbersOnCard += 1
    
    for nextIndex in range(winningNumbersOnCard):
        scratchCards[index + nextIndex + 1].add_copies(scratchCard.qty)
    
    totalCards += scratchCard.qty

print(totalCards)