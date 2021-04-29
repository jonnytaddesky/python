current_hand = [2, 3, 4, 10, 'Q', 5]
card_sum = 0

cards = {
    2: 1,
    3: 1,
    4: 1,
    5: 1,
    6: 1,
    7: 0,
    8: 0,
    9: 0,
    10: -1,
    'J': -1,
    'Q': -1,
    'K': -1,
    'A': -1
}

for card in current_hand:
    print(cards.items(card))
    for k, v in cards.items():
        if card == k:
            card_sum += v
print(card_sum)

card_sum = sum([cards[card] for card in current_hand])
print(card_sum)

print(cards.items(card))
