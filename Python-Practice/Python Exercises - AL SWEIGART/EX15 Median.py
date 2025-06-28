"""
Exercise Description
    Write a median() function that has a numbers parameter. This function returns the statistical
median of the numbers list. The median of an odd-length list is the number in the middlemost
number when the list is in sorted order. If the list has an even length, the median is the average of the
two middlemost numbers when the list is in sorted order. Feel free to use Python's built-in sort()
method to sort the numbers list.
Passing an empty list to median() should cause it to return None.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True:
assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
 random.shuffle(testData)
 assert median(testData) == 6
Shuffling the order of the numbers should not affect the median.
"""

def median(numbers):
    length = len(numbers)
    if length == 0:
        return None
    numbers = sorted(numbers)
    if length % 2 == 0:
        return (numbers[length//2 - 1] + numbers[length//2]) / 2
    else:
        return numbers[length//2]

assert median([]) == None
assert median([1, 2, 3]) == 2
assert median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5
assert median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6
import random
random.seed(42)
testData = [3, 7, 10, 4, 1, 9, 6, 2, 8]
for i in range(1000):
 random.shuffle(testData)
 assert median(testData) == 6
