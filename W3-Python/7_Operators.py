print("\n___________________________________Arithmetic operators___________________________________\n")
x = 10
y = 3

print(f"Addition (+)\t\t: {x} + {y} = ", x + y)        # 10 + 3 = 13
print(f"Subtraction (-)\t\t: {x} - {y} = ", x - y)        # 10 - 3 = 7
print(f"Multiplication (*)\t: {x} * {y} = ", x * y)      # 10 * 3 = 30
print(f"Exponentiation (**)\t: {x} ** {y} = ", x ** y)   # 10 ** 3 = 1000
print(f"Modulus (%)\t\t: {x} % {y} = ", x % y)          # 10 % 3 = 1 (remainder)
print(f"Division (/)\t\t: {x} / {y} = ", x / y)         # 10 / 3 = 3.333...
print(f"Floor Division (//)\t: {x} // {y} = ", x // y)   # 10 // 3 = 3 (int division)

print("\n___________________________________Assignment operators___________________________________\n")

# Basic assignment
print("# Basic assignment")
x = 5
print(f"=   (Assign)\t\t: {x} = 5 \t=>", x)

# Arithmetic assignment
print(f"\n# Arithmetic assignment")
x += 3  # x = x + 3
print(f"+=  (Add & assign)\t: {x} += 3 \t=>", x)

x -= 3  # x = x - 3
print(f"-=  (Subtract & assign)\t: {x} -= 3 \t=>", x)

x *= 3  # x = x * 3
print(f"*=  (Multiply & assign)\t: {x} *= 3 \t=>", x)

x /= 3  # x = x / 3
print(f"/=  (Divide & assign)\t: {x} /= 3 \t=>", x)

x %= 3  # x = x % 3
print(f"%=  (Modulus & assign)\t: {x} %= 3 \t=>", x)

x = 10
x //= 3  # x = x // 3
print(f"//= (FloorDiv & assign)\t: {x} //= 3 \t=>", x)

x = 2
x **= 3  # x = x ** 3
print(f"**= (Exponent & assign)\t: {x} **= 3 \t=>", x)

# Bitwise assignment
print(f"\n# Bitwise assignment")
x = 5
x &= 3  # x = x & 3
print(f"&=  (AND & assign)\t: {x} &= 3 \t=>", x)

x = 5
x |= 3  # x = x | 3
print(f"|=  (OR & assign)\t: {x} |= 3 \t=>", x)

x = 5
x ^= 3  # x = x ^ 3
print(f"^=  (XOR & assign)\t: {x} ^= 3 \t=>", x)

x = 8
x >>= 2  # x = x >> 2
print(f">>= (Right shift)\t: {x} >>= 2 \t=>", x)

x = 2
x <<= 2  # x = x << 2
print(f"<<= (Left shift)\t: {x} <<= 2 \t=>", x)

# Walrus operator (assignment expression, Python 3.8+)
print("\n:=  (Walrus operator)\t: print(x := 3) =>", (x := 3))  # Assigns and prints in one line
print("After := x is\t\t=>", x)

print("\n___________________________________Comparison operators___________________________________\n")

x = 10
y = 5
z = 10

print(f"==  (Equal to)\t\t: {x} == {z} =>", x == z)     # True
print(f"!=  (Not equal to)\t: {x} != {y} =>", x != y)   # True
print(f">   (Greater than)\t: {x} > {y}  =>", x > y)    # True
print(f"<   (Less than)\t\t: {y} < {x}  =>", y < x)    # True
print(f">=  (Greater or equal)\t: {x} >= {z} =>", x >= z) # True
print(f"<=  (Less or equal)\t: {x} <= {y} =>", x <= y)   # False

print("\n____________________________________Logical operators_____________________________________\n")

x = 7

# and: both conditions must be True
print(f"and\t(Both True)\t: {x} > 5 and {x} < 10\t=>", x > 5 and x < 10)   # True
print(f"and\t(One False)\t: {x} > 5 and {x} > 10\t=>", x > 5 and x > 10)   # False

# or: at least one condition must be True
print(f"or\t(One True)\t: {x} < 5 or {x} < 10\t=>", x < 5 or x < 10)       # True
print(f"or\t(Both False)\t: {x} < 5 or {x} < 4\t=>", x < 5 or x < 4)       # True
print(f"or\t(Both False)\t: {x} > 10 or {x} < 3\t=>", x > 10 or x < 3)     # False

# not: reverses the result of the expression
print(f"not\t(Reversed)\t: not(x < 5 and x < 10)\t=>", not(x < 5 and x < 10))  # True becomes False

print("\n____________________________________Identity operators____________________________________\n")

# Identity operators check if two variables point to the same object in memory

a = [1, 2, 3]
b = a       # b references the same object as a
c = [1, 2, 3]  # new object with same content

print("is\t(Same object)\t\t: a is b\t=>", a is b)         # True
print("is\t(Different object)\t: a is c\t=>", a is c)         # False

print("is not\t(Different object)\t: a is not c\t=>", a is not c)   # True
print("is not\t(Same object)\t\t: a is not b\t=>", a is not b)     # False

print("\n___________________________________Membership operators___________________________________\n")

# Membership operators check if a value exists in a sequence (like list, string, tuple, etc.)

# String example
txt = "Python is powerful"

print("'Python' in txt\t\t=>", "Python" in txt)      # True
print("'Java' not in txt\t=>", "Java" not in txt)    # True

# List example
items = [1, 2, 3, 4, 5]

print("3 in items\t\t=>", 3 in items)              # True
print("10 not in items\t\t=>", 10 not in items)      # True

# Tuple example
tup = ('apple', 'banana', 'cherry')

print("'banana' in tup\t\t=>", 'banana' in tup)      # True
print("'grape' not in tup\t=>", 'grape' not in tup)  # True

print("\n____________________________________Bitwise operators_____________________________________\n")

a = 5   # 0b0101
b = 3   # 0b0011

# Binary representations for reference
print(f"a = {a} -> {bin(a)}")
print(f"b = {b} -> {bin(b)}\n")

# & AND: Sets each bit to 1 if both bits are 1
print(f"a & b (AND)\t\t: {a} & {b} = {a & b}\t-> {bin(a & b)}")  # 0b0001

# | OR: Sets each bit to 1 if one of the bits is 1
print(f"a | b (OR)\t\t: {a} | {b} = {a | b}\t-> {bin(a | b)}")  # 0b0111

# ^ XOR: Sets each bit to 1 if only one of the bits is 1
print(f"a ^ b (XOR)\t\t: {a} ^ {b} = {a ^ b}\t-> {bin(a ^ b)}")  # 0b0110

# ~ NOT: Inverts all the bits (2's complement)
print(f"~a (NOT)\t\t: ~{a} = {~a}\t-> {bin(~a)}")               # Inverts all bits

# << Left Shift: Shifts bits to the left (multiplies by 2^n)
print(f"a << 2 (Left Shift)\t: {a} << 2 = {a << 2}\t-> {bin(a << 2)}")  # 0b10100

# >> Right Shift: Shifts bits to the right (divides by 2^n)
print(f"a >> 2 (Right Shift)\t: {a} >> 2 = {a >> 2}\t-> {bin(a >> 2)}")  # 0b0001

print("\n============================ Operator Precedence Demo ============================\n")

# 1. () Parentheses — Highest precedence
print("# 1. Parentheses")
print("(2 + 3) * 5\t\t= ", (2 + 3) * 5)                   # 25
print("2 + (3 * 5)\t\t= ", 2 + (3 * 5))                   # 17
print("((2 + 3) * (4 + 1)) = ", ((2 + 3) * (4 + 1)))       # 25

# 2. ** Exponentiation — Right to left
print("\n# 2. Exponentiation (**)")
print("2 ** 3 ** 2\t\t= ", 2 ** 3 ** 2)                   # 512
print("3 ** 2\t\t\t= ", 3 ** 2)                           # 9
print("2 ** (1 + 1)\t\t= ", 2 ** (1 + 1))                 # 4

# 3. Unary +x, -x, ~x — Unary plus, minus, bitwise NOT
print("\n# 3. Unary operators (+, -, ~)")
x = 5
print("x\t\t\t= ", x)
print("+x\t\t\t= ", +x)                                  # 5
print("-x\t\t\t= ", -x)                                  # -5
print("~x\t\t\t= ", ~x)                                  # -6

# 4. *, /, //, % — Multiplication, division, floor division, modulus
print("\n# 4. Multiplicative operators (*, /, //, %)")
print("5 * 3\t\t\t= ", 5 * 3)                             # 15
print("5 / 2\t\t\t= ", 5 / 2)                             # 2.5
print("5 // 2\t\t= ", 5 // 2)                             # 2
print("5 % 2\t\t\t= ", 5 % 2)                             # 1

# 5. +, - — Addition and subtraction
print("\n# 5. Additive operators (+, -)")
print("5 + 3\t\t\t= ", 5 + 3)                             # 8
print("5 - 3\t\t\t= ", 5 - 3)                             # 2
print("10 + -2\t\t= ", 10 + -2)                           # 8

# 6. <<, >> — Bitwise shifts
print("\n# 6. Bitwise shifts (<<, >>)")
print("2 << 2\t\t\t= ", 2 << 2)                           # 8
print("8 >> 2\t\t\t= ", 8 >> 2)                           # 2
print("5 << 1\t\t\t= ", 5 << 1)                           # 10

# 7. & — Bitwise AND
print("\n# 7. Bitwise AND (&)")
print("5 & 3\t\t\t= ", 5 & 3)                             # 1
print("6 & 2\t\t\t= ", 6 & 2)                             # 2
print("7 & 4\t\t\t= ", 7 & 4)                             # 4

# 8. ^ — Bitwise XOR
print("\n# 8. Bitwise XOR (^)")
print("5 ^ 3\t\t\t= ", 5 ^ 3)                             # 6
print("4 ^ 4\t\t\t= ", 4 ^ 4)                             # 0
print("7 ^ 2\t\t\t= ", 7 ^ 2)                             # 5

# 9. | — Bitwise OR
print("\n# 9. Bitwise OR (|)")
print("5 | 3\t\t\t= ", 5 | 3)                             # 7
print("4 | 1\t\t\t= ", 4 | 1)                             # 5
print("6 | 2\t\t\t= ", 6 | 2)                             # 6

# 10. Comparisons: ==, !=, >, >=, <, <=, is, is not, in, not in
print("\n# 10. Comparisons (==, !=, >, <, is, in, etc.)")
print("5 == 5\t\t\t= ", 5 == 5)                           # True
print("5 != 4\t\t\t= ", 5 != 4)                           # True
print("5 > 3\t\t\t= ", 5 > 3)                             # True
print("[1, 2] is [1, 2]\t= ", [1, 2] is [1, 2])            # False
print("'a' in 'apple'\t= ", 'a' in 'apple')               # True

# 11. not — Logical NOT
print("\n# 11. Logical NOT (not)")
print("not True\t\t= ", not True)                        # False
print("not (5 > 3)\t\t= ", not (5 > 3))                  # False
print("not False\t\t= ", not False)                      # True

# 12. and — Logical AND
print("\n# 12. Logical AND (and)")
print("True and True\t= ", True and True)                # True
print("True and False\t= ", True and False)              # False
print("5 > 3 and 3 > 1 = ", 5 > 3 and 3 > 1)              # True

# 13. or — Logical OR — Lowest precedence
print("\n# 13. Logical OR (or)")
print("True or False\t= ", True or False)                # True
print("False or False\t= ", False or False)              # False
print("5 < 3 or 3 < 10 = ", 5 < 3 or 3 < 10)              # True

