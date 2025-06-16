# Built-in Data Types

# Text Type:	    str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	    dict
# Set Types:	    set, frozenset
# Boolean Type:	    bool
# Binary Types:	    bytes, bytearray, memoryview
# None Type:	    NoneType

print("--------------------------------------------------------------------------------------------------------------------")

# we can use the type() function to get data type ofamy value 

x = 5
print(type(x))

print("--------------------------------------------------------------------------------------------------------------------")

# String
x = "Hello World"
print(type(x), "   value of x:", x)

# Integer
x = 20
print(type(x), "   value of x:", x)

# Float
x = 20.5
print(type(x), "   value of x:", x)

# Complex number
x = 1j
print(type(x), "   value of x:", x)

# List (mutable, ordered, allows duplicates)
x = ["apple", "banana", "cherry"]
print(type(x), "   value of x:", x)

# Tuple (immutable, ordered, allows duplicates)
x = ("apple", "banana", "cherry")
print(type(x), "   value of x:", x)

# Range (used for generating a sequence of numbers)
x = range(6)
print(type(x), "   value of x:", x)

# Dictionary (key-value pairs, unordered in < Python 3.7)
x = {"name": "John", "age": 36}
print(type(x), "   value of x:", x)

# Set (unordered, no duplicate elements)
x = {"apple", "banana", "cherry"}
print(type(x), "   value of x:", x)

# set is mutable — you can add, remove elements.
# frozenset is immutable — once created, cannot be modified.


# Frozenset (immutable version of set)
x = frozenset({"apple", "banana", "cherry"})
print(type(x), "   value of x:", x)

# Boolean
x = True
print(type(x), "   value of x:", x)

# Bytes (immutable sequence of bytes)
x = b"Hello"
print(type(x), "   value of x:", x)

# Bytearray (mutable sequence of bytes)
x = bytearray(5)
print(type(x), "   value of x:", x)

# Memoryview (gives memory access to the internal data of an object)
x = memoryview(bytes(5))
print(type(x), "   value of x:", x)

# NoneType (represents the absence of a value)
x = None
print(type(x), "   value of x:", x)

print("--------------------------------------------------------------------------------------------------------------------")
