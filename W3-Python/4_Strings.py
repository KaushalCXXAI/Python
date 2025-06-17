print("\n===================== Multiline Strings ======================\n")

# Using triple double quotes to create a multiline string
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Using triple single quotes to create a multiline string (equivalent to triple double quotes)
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


print("\n=============== String Indexing and Iteration ================\n")

# Accessing individual characters in a string using indexing
a = "Hello, World!"
print(a[6])  # prints the character at index 6 ('W')

# Iterating over each character in the string using a for-loop
for x in a:
  print(x)

# Using len() function to get the length (number of characters) of the string
a = "Hello, World!"
print(len(a))  # prints 13


print("\n========================= in & not in ========================\n")

# Using 'in' keyword to check if a substring exists within a string
txt = "The best things in life are free!"
print("free" in txt)  # prints True

# Using 'in' with if statement to perform conditional logic
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")

# Using 'not in' to check if a substring is NOT in the string
txt = "The best things in life are free!"
print("expensive" not in txt)  # prints True

# Using 'not in' with if statement for conditional checks
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


print("\n=========================== Slicing ==========================\n")

# Get characters from position 2 to 5 (5 is not included, so only characters at index 2, 3, and 4)
b = "Hello, World!"
print(b[2:5])  # prints "llo"

# Get characters from the beginning up to position 5 (excluding 5)
b = "Hello, World!"
print(b[:5])  # prints "Hello"

# Get characters starting from position 2 all the way to the end of the string
b = "Hello, World!"
print(b[2:])  # prints "llo, World!"

# Slicing with negative indexes: from -5 ("o") to -2 ("d", not included), so it gives 'orl'
b = "Hello, World!"
print(b[-5:-2])  # prints "orl"

# When slicing from a higher index (-5) to a lower index (1) with a positive step (default),
# Python returns an empty string because the slice goes "forward" but the start is after the end.
b = "Hello, World!"
print(b[-5:1])  # prints an empty string


print("\n======================= Modify Strings =======================\n")

# Convert the string to uppercase using .upper()
a = "Hello, World!"
print(a.upper())  # prints "HELLO, WORLD!"

# Convert the string to lowercase using .lower()
print(a.lower())  # prints "hello, world!"

# Remove leading and trailing whitespace using .strip()
a = " Hello, World! "
print(a.strip())  # prints "Hello, World!" (spaces removed from both ends)

# Replace a specific character or substring using .replace()
a = "Hello, World!"
print(a.replace("H", "J"))  # prints "Jello, World!"

# Split the string into a list using a delimiter (in this case, a comma)
a = "Hello, World!"
print(a.split(","))  # prints ['Hello', ' World!']

print("\n==================== String Concatenation ====================\n")

a = "Hello"
b = "World"
c = a + b  # Concatenates without space: HelloWorld
print(c)

a = "Hello"
b = "World"
c = a + " " + b  # Concatenates with space: Hello World
print(c)

print("\n====================== Format - Strings ======================\n")

# age = 36
# txt = "My name is John, I am " + age  # This will cause an error because age is an int, not a string
# print(txt)

age = 36
txt = f"My name is John, I am {age}"  # Using f-string for formatted output
print(txt)

price = 59
txt = f"The price is {price} dollars"  # Insert variable price as integer
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"  # Format price to 2 decimal places
print(txt)

txt = f"The price is {20 * 59} dollars"  # Insert expression result directly in f-string
print(txt)

print("\n====================== Escape Characters =====================\n")

# Escape characters allow you to include special characters in strings
# Here are some common escape sequences with examples:

print("Single Quote: \'")         # Output: Single Quote: '
print("Backslash: \\")            # Output: Backslash: \
print("New Line:\nSecond Line")  # Output: New Line:
                                #Second Line
print("Carriage Return:\rCR")    # Output may overwrite start of line depending on environment
print("Tab:\tTabbed Text")       # Output: Tab:    Tabbed Text
print("Backspace: Helloo\b!")    # Output: Backspace: Hello!
print("Form Feed:\fNext Page")   # Output may vary, form feed is rarely used

print("Octal value: \101\102\103")  # Output: Octal value: ABC (ASCII codes in octal)
print("Hex value: \x41\x42\x43")    # Output: Hex value: ABC (ASCII codes in hex)
