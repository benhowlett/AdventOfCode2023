def determine_hand_type(hand) -> int:
    counts = []
    for card in hand:
        cardNotFound = True
        if len(counts) > 0:            
            for count in counts:
                if count[0] == card:
                   cardNotFound = False
                   break
        if cardNotFound:
            counts.append((card, hand.count(card)))
        
    counts.sort(key=lambda a: a[1], reverse=True)

    for index, count in enumerate(counts):
        match count[1]:
            case 5:
                return 7
            case 4:
                return 6
            case 3:
                if counts[index + 1][1] == 2:
                    return 5
                else:
                    return 4
            case 2:
                if counts[index + 1][1] == 2:
                    return 3
                else:
                    return 2
            case _:
                return 1

def second_card_is_higher(card1, card2):
    ranks = {
        "2":1,
        "3":2,
        "4":3,
        "5":4,
        "6":5,
        "7":6,
        "8":7,
        "9":8,
        "T":9,
        "J":10,
        "Q":11,
        "K":12,
        "A":13
    }        
    if ranks[card1] < ranks[card2]:
        return True
    else:
        return False
    
def second_hand_is_higher(hand1, hand2) -> bool:
    for i in range(5):
        if hand1[i] != hand2[i]:
            if second_card_is_higher(hand1[i], hand2[i]):
                return True
            else:
                break
    return False

def sort_hands_by_card_value(hands):
    n = len(hands)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-1):
            if hands[j][1] == hands[j+1][1]:
                if second_hand_is_higher(hands[j][0], hands[j+1][0]):
                    swapped = True
                    hands[j], hands[j+1] = hands[j+1], hands[j]
        if not swapped:
            return

input = open('input.txt', 'r')

hands = []

for line in input:
    hand = line.split()
    hands.append((hand[0], determine_hand_type(hand[0]), int(hand[1])))

hands.sort(key=lambda a: a[1], reverse=True)
sort_hands_by_card_value(hands)

totalWinnings = 0

for i in range(len(hands)):
    totalWinnings += hands[i][2] * (len(hands) - i)

print(totalWinnings)