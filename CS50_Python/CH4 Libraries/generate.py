# import random

# coin = random.choice(["Heads", "Tails"])
# print(coin)

# from random import choice

# coin = choice(["Heads", "Tails"])
# print(coin)

# import random 

# number = random.randint(1,10)
# print(number )

import random

cards = ["King", "Jack", "Queen"]

random.shuffle(cards)

for card in cards:
    print(card)