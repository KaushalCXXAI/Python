"""
Exercise Description
    Write a getSmallest() function that has a numbers parameter. The numbers parameter will
be a list of integer and floating-point number values. The function returns the smallest value in the
list. If the list is empty, the function should return None. Since this function replicates Python's
min() function, your solution shouldn't use it.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True:
assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None
"""
def getSmallest(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(length):
            if numbers[i] < numbers[j]:
                a = numbers[i]
                numbers[i] = numbers[j]
                numbers[j] = a

    return numbers[0] if numbers and numbers[0] != "" else None

assert getSmallest([1, 2, 3]) == 1
assert getSmallest([3, 2, 1]) == 1
assert getSmallest([28, 25, 42, 2, 28]) == 2
assert getSmallest([1]) == 1
assert getSmallest([]) == None

# my answer is techinically right but logically its like draining the entire ocean just to get one fish the answer shocul be like this
# def getSmallest(numbers):
#     if not numbers:
#         return None

#     smallest = numbers[0]
#     for num in numbers[1:]:
#         if num < smallest:
#             smallest = num
#     return smallest

# assert getSmallest([1, 2, 3]) == 1
# assert getSmallest([3, 2, 1]) == 1
# assert getSmallest([28, 25, 42, 2, 28]) == 2
# assert getSmallest([1]) == 1
# assert getSmallest([]) == None
