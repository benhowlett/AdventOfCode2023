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
    print(hand1, hand2)
    for i in range(5):
        if hand1[i] != hand2[i]:
            print(hand1[i], hand2[i])
            if second_card_is_higher(hand1[i], hand2[i]):
                return True
            else:
                break
    return False

print(second_hand_is_higher("AA8AA", "AQQQQ"))