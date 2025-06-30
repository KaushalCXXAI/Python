"""
Exercise Description
    Write a rollDice() function with a numberOfDice parameter that represents the number of
six-sided dice. The function returns the sum of all of the dice rolls. For this exercise you must import
Python's random module to call its random.randint() function for this exercise.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True. We can't predict rollDice()'s random return value, but we can do
repeated checks that the return value is within the correct range of expected values:
assert rollDice(0) == 0
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
 assert 1 <= rollDice(1) <= 6
 assert 2 <= rollDice(2) <= 12
 assert 3 <= rollDice(3) <= 18
 assert 100 <= rollDice(100) <= 600
"""
import random
def rollDice(numberOfDice):
    if numberOfDice == 0 or numberOfDice == "" :
        return 0
    ans = 0 
    for i in range(numberOfDice):
        ans += random.randint(1,6)
    return ans

# better version by chatgpt
# def rollDice(numberOfDice):
#     return sum(random.randint(1, 6) for _ in range(numberOfDice))

assert rollDice(0) == 0
assert rollDice(1000) != rollDice(1000)
for i in range(1000):
 assert 1 <= rollDice(1) <= 6
 assert 2 <= rollDice(2) <= 12
 assert 3 <= rollDice(3) <= 18
 assert 100 <= rollDice(100) <= 600