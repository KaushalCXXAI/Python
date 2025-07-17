"""
Exercise Description
    Write a convertStrToInt() function with a stringNum parameter. This function returns an
integer form of the parameter just like the int() function. For example,
convertStrToInt('42') should return the integer 42. The function doesn't have to work for
floating-point numbers with a decimal point, but it should work for negative number values.
Avoid using int()in your code, as that would do the conversion for you and defeat the purpose
of this exercise. However, we do use int() with assert statements to check that your
convertStrToInt() function works the same as int() for all integers from -10000 to 9999:
for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
"""

def convertStrToInt(stringNum):
    str_to_int_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    ans = 0
    is_negative = False

    if "-" in stringNum:
        stringNum = stringNum.replace("-","")
        is_negative = True

    for i in stringNum:
        ans = ans * 10 + str_to_int_dict[i]

    return -ans if is_negative else ans

for i in range(-10000, 10000):
    assert convertStrToInt(str(i)) == i
