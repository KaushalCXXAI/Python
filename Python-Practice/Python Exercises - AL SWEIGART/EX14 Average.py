import math
def average(numbers):
    
    if (length := len(numbers)) == 0:
        return None
    total = 0
    # [total:= total + s for s in numbers]
    # or
    for s in numbers:
        total += s
    return(math.floor(total/length))

assert average([1, 2, 3]) == 2
assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
assert average([12, 20, 37]) == 23
assert average([0, 0, 0, 0, 0]) == 0
import random
random.seed(42)
testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
for i in range(1000):
    random.shuffle(testData)
    assert average(testData) == 2