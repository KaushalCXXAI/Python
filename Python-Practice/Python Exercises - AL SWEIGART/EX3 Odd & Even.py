"""
Exercise Description
    Write two functions, isOdd() and isEven(), with a single numeric parameter named
number. The isOdd() function returns True if number is odd and False if number is even. The
isEven() function returns the True if number is even and False if number is odd. Both
functions return False for numbers with fractional parts, such as 3.14 or -4.5. Zero is considered
an even number.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True:
assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False
"""

def isOdd(n):
    return n % 2 == 1
    
def isEven(n):
    return n % 2 == 0

assert isOdd(42) == False
assert isOdd(9999) == True
assert isOdd(-10) == False
assert isOdd(-11) == True
assert isOdd(3.1415) == False
assert isEven(42) == True
assert isEven(9999) == False
assert isEven(-10) == True
assert isEven(-11) == False
assert isEven(3.1415) == False