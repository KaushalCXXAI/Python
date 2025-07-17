"""
Exercise Description
    Write a convertIntToStr() function with an integerNum parameter. This function
operates similarly to the str() function in that it returns a string form of the parameter. For
example, convertIntToStr(42) should return the string '42'. The function doesn’t have to
work for floating-point numbers with a decimal point, but it should work for negative integer values.
Avoid using Python's str() function in your code, as that would do the conversion for you and
defeat the purpose of this exercise. However, we use str() with assert statements to check that
your convertIntToStr() function works the same as str() for all integers from -10000 to
9999:
for i in range(-10000, 10000):
    assert convertIntToStr(i) == str(i)
"""

def convertIntToStr(integerNum):
    int_to_str_dict = {0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
    ans = ""
    minus = ""

    if integerNum == 0:
        return "0"

    if integerNum < 0 :
        integerNum = abs(integerNum)
        minus = "-"

    while integerNum > 0:
        r = integerNum % 10
        integerNum = integerNum // 10
        ans += int_to_str_dict[r]

    if minus != "":
        return(minus + ans[::-1])
    else:
        return(ans[::-1])

for i in range(-10000, 10000):
    print(i)
    assert convertIntToStr(i) == str(i)


# chatgpts version given bellow is better than mine because it uses the "divmod" and other function cleverly

def convertIntToStr(n):
    INT_TO_STR = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    if n == 0:
        return '0'

    result = []
    is_negative = n < 0
    n = abs(n)

    while n > 0:
        n, rem = divmod(n, 10)
        result.append(INT_TO_STR[rem])

    if is_negative:
        result.append('-')

    return ''.join(reversed(result))

for i in range(-10000, 10000):
    print(i)
    assert convertIntToStr(i) == str(i)