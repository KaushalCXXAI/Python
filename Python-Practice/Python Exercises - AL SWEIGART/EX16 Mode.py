"""
Exercise Description
    Write a mode() function that has a numbers parameter. This function returns the mode, or
most frequently appearing number, of the list of integer and floating-point numbers passed to the
function.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True:
assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
 random.shuffle(testData)
 assert mode(testData) == 4
Shuffling the order of the numbers should not affect the mode. 
"""

def mode(numbers):
    if len(numbers) == 0:
        return None
    counts = {i: numbers.count(i) for i in numbers}
    i = 0
    answer = None
    for key,value in counts.items():
        if i < value :
            i = value
            answer = key
    return answer

assert mode([]) == None
assert mode([1, 2, 3, 4, 4]) == 4
assert mode([1, 1, 2, 3, 4]) == 1
import random
random.seed(42)
testData = [1, 2, 3, 4, 4]
for i in range(1000):
 random.shuffle(testData)
 assert mode(testData) == 4