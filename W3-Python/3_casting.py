print("--------------------------------------------------------------------------------------------------------------------")

# Integer from negative int
x = int(-1)
print(type(x), "   value of x:", x)

# Integer from positive int
x = int(1)
print(type(x), "   value of x:", x)

# Integer from negative float (decimal part is truncated, not rounded)
y = int(-1.1)
print(type(y), "   value of y:", y)

# Integer from positive float (again, decimal is truncated)
y = int(1.1)
print(type(y), "   value of y:", y)

# Integer from small float
y = int(0.1)
print(type(y), "   value of y:", y)

# Invalid conversions (will throw ValueError)
# z = int("3.1")  # Error: invalid literal for int() with base 10: '3.1'
# z = int("str")  # Error: invalid literal for int() with base 10: 'str'

# Valid conversion from numeric string
z = int("3")
print(type(z), "   value of z:", z)

print("--------------------------------------------------------------------------------------------------------------------")

# Float from negative int
x = float(-1)
print(type(x), "   value of x:", x)

# Float from positive int
x = float(1)
print(type(x), "   value of x:", x)

# Float from negative float
y = float(-1.1)
print(type(y), "   value of y:", y)

# Float from positive float
y = float(1.1)
print(type(y), "   value of y:", y)

# Float from string (valid numeric string)
z = float("3.14")
print(type(z), "   value of z:", z)

# Float from integer string
z = float("5")
print(type(z), "   value of z:", z)

# Float from boolean (True → 1.0, False → 0.0)
z = float(True)
print(type(z), "   value of z:", z)

z = float(False)
print(type(z), "   value of z:", z)

# Invalid conversions — uncommenting these will throw ValueError
# a = float("abc")      # Error: cannot convert string to float
# b = float("12.3.4")   # Error: malformed float string
# c = float("1,000")    # Error: commas not allowed in float()

print("--------------------------------------------------------------------------------------------------------------------")

# String from integer
x = str(123)
print(type(x), "   value of x:", x)

# String from float
x = str(3.14)
print(type(x), "   value of x:", x)

# String from boolean
x = str(True)
print(type(x), "   value of x:", x)

x = str(False)
print(type(x), "   value of x:", x)

# String from NoneType
x = str(None)
print(type(x), "   value of x:", x)

# String from list
x = str(["apple", "banana", "cherry"])
print(type(x), "   value of x:", x)

# String from tuple
x = str(("apple", "banana", "cherry"))
print(type(x), "   value of x:", x)

# String from set
x = str({"apple", "banana", "cherry"})
print(type(x), "   value of x:", x)

# String from dictionary
x = str({"name": "John", "age": 30})
print(type(x), "   value of x:", x)

# String from complex number
x = str(2 + 3j)
print(type(x), "   value of x:", x)

# String from bytes
x = str(b"hello")
print(type(x), "   value of x:", x)

# String from bytearray
x = str(bytearray(b"hello"))
print(type(x), "   value of x:", x)

# String from memoryview
x = str(memoryview(b"hello"))
print(type(x), "   value of x:", x)

# String from empty input
x = str("")
print(type(x), "   value of x:", x)

print("--------------------------------------------------------------------------------------------------------------------")

