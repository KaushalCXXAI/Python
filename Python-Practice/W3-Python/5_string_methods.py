print("\n===================== string.capitalize() ======================\n")

# Capitalizes the first character of the string
txt = "hello, and welcome to my world."
print(txt.capitalize())

txt = "1ython is FUN!"
print(txt.capitalize())

txt = "36 Is my age."
print(txt.capitalize())

print("\n====================== string.casefold() =======================\n")

# Converts string to lowercase – more aggressive than .lower()
txt = "Hello, And Welcome To My World!"
print(txt.casefold())

txt = "36 Is my age."
print(txt.casefold())

print("\n=================== string.center(width, fill) ==================\n")

# Centers the string within a given width, filling with specified char
txt = "banana"
print(txt.center(20, "O"))

txt = "banana hello"
print(txt.center(20, '+'))

print("\n================ string.count(sub[, start[, end]]) ==============\n")

# Returns number of occurrences of substring
txt = "I love apples, apple are my favorite fruit"
print(txt.count("apple"))

# Count with range
print(txt.count("apple", 10, 24))

print("\n================= string.encode(encoding, errors) ===============\n")

# Encode string to bytes using different error handlers
txt = "My name is Ståle"
print(txt.encode())

print(txt.encode(encoding="ascii", errors="backslashreplace"))
print(txt.encode(encoding="ascii", errors="ignore"))
print(txt.encode(encoding="ascii", errors="namereplace"))
print(txt.encode(encoding="ascii", errors="replace"))
print(txt.encode(encoding="ascii", errors="xmlcharrefreplace"))

print("\n=================== string.endswith(suffix[, start, end]) ==========\n")

# Checks if string ends with a specified suffix
txt = "Hello, welcome to my world."
print(txt.endswith("."))

print(txt.endswith("my world."))

# Checking within range
print(txt.endswith("my world.", 5, 11))

# Tuple of suffixes
txt = "Hello, welcome to my castle."
print(txt.endswith(("world.", "castle.")))

print("\n====================== string.expandtabs(tabsize) ==================\n")

# Replaces tab characters with spaces
txt = "H\te\tl\tl\to"
print(txt.expandtabs(5).center(29, "+"))  # centered after expandtabs

print(txt)
print(txt.expandtabs())     # default = 8
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

print("\n=================== string.find(sub[, start, end]) =================\n")

# Returns index of first occurrence, -1 if not found
txt = "Hello, welcome to my world."
print(txt.find("welcome"))

print(txt.find("e"))

print(txt.find("e", 5, 10))

print(txt.find("q"))  # returns -1 if not found

print("\n========================= string.format() ==========================\n")

# Replaces {} placeholders with values
txt = "For only {price:.2f} dollars!"
print(txt.format(price=49))

txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
print(txt1)

txt2 = "My name is {0}, I'm {1}".format("John", 36)
print(txt2)

txt3 = "My name is {}, I'm {}".format("John", 36)
print(txt3)

print("\n================= string.index(sub[, start, end]) ==================\n")

# Like find(), but raises ValueError if not found
txt = "Hello, welcome to my world."
print(txt.index("e"))

print(txt.index("e", 5, 10))

# print(txt.index("q"))  # This will raise ValueError

print("\n========================= string.isalnum() =========================\n")

# True if all characters are alphanumeric
txt = "Company12"
print(txt.isalnum())

txt = "Company 12"
print(txt.isalnum())

print("\n========================= string.isalpha() =========================\n")

# True if all characters are alphabetic
txt = "CompanyX"
print(txt.isalpha())

txt = "Company10"
print(txt.isalpha())

print("\n======================= string.isdecimal() =========================\n")

# True if all characters are decimals
txt = "1234"
print(txt.isdecimal())

a = "\u0030"  # unicode for 0
b = "\u0047"  # unicode for G
print(a.isdecimal())
print(b.isdecimal())

print("\n======================== string.isdigit() ==========================\n")

# True if all characters are digits (includes unicode digits like ²)
txt = "50800"
print(txt.isdigit())

a = "\u0030"  # unicode for 0
b = "\u00B2"  # unicode for ²
print(a.isdigit())
print(b.isdigit())

print("\n==================== string.isidentifier() =========================\n")

# A string is considered a valid identifier if it only contains alphanumeric letters (a-z) and (0-9), or underscores (_). A valid identifier cannot start with a number, or contain any spaces.
txt = "Demo"
print(txt.isidentifier())

a = "MyFolder"
b = "Demo002"
c = "2bring"
d = "my demo"

print(a.isidentifier())
print(b.isidentifier())
print(c.isidentifier())
print(d.isidentifier())

print("\n==============================islower()==============================\n")

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())

print("\n=============================isnumeric()=============================\n")

a = "\u0030" #unicode for 0
b = "\u00B2" #unicode for &sup2;
c = "10km2"
d = "-1"
e = "1.5"
f = "565543"

print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
print(f.isnumeric())

print("\n============================isprintable()============================\n")

# Checks if all characters in the string are printable (excluding things like \n, \t, etc.)
txt = "Hello!\nAre you #1?"
x = txt.isprintable()
print(x, ":\t", txt)

txt = "Hello! Are you #1?"
x = txt.isprintable()
print(x, ":\t", txt)

print("\n==============================isspace()==============================\n")

# Checks if the string only contains whitespace characters (spaces, tabs, etc.)
txt = "   "
x = txt.isspace()
print(x, ":\t", txt)

txt = "   s   "
x = txt.isspace()
print(x, ":\t", txt)

print("\n==============================istitle()==============================\n")

# Returns True if each word starts with a capital letter followed by lowercase letters
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
print(x, ":\t", txt)

a = "HELLO, AND WELCOME TO MY WORLD"
b = "Hello"
c = "22 Names"
d = "This Is %'!?"
e = "My name is kaushal"
f = "my Name Is Kushal"

print(a.istitle(), ":\t", a)
print(b.istitle(), ":\t", b)
print(c.istitle(), ":\t", c)
print(d.istitle(), ":\t", d)
print(e.istitle(), ":\t", e)
print(f.istitle(), ":\t", f)

print("\n==============================isupper()==============================\n")

# Returns True if all characters are uppercase
txt = "THIS IS NOW!"
x = txt.isupper()
print(x, ":\t", txt)

a = "Hello World!"
b = "hello 123"
c = "   "
d = "MY NAME IS PETER"

print(a.isupper(), ":\t", a)
print(b.isupper(), ":\t", b)
print(c.isupper(), ":\t", c)
print(d.isupper(), ":\t", d)

print("\n============================join(iterable)===========================\n")

# Joins elements in an iterable with a string separator
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)  # joins keys only
print(x)

print("\n=======================ljust(length, character)======================\n")

# Left-justifies the string and pads the remaining space
txt = "banana"
x = txt.ljust(20)
print(x, "is my favorite fruit.")

x = txt.ljust(20, "O")
print(x)

print("\n=============================maketrans()=============================\n")

# Creates a translation table and applies it using translate()
txt = "Hello Sam!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(mytable)
print(txt.translate(mytable))

txt = "Good night Sam!"
z = "odight "
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

print(str.maketrans(x, y, z))

print("\n===========================partition(value)==========================\n")

# Splits the string into 3 parts: before, match, and after
txt = "I would not eat bananas i hate  bananas are not ment to be eaten by man"
x = txt.partition("bananas")
print(x)

txt = "I could eat bananas all day"
x = txt.partition("apples")  # partition not found, middle is ''
print(x)

print("\n==================replace(oldvalue, newvalue, count)=================\n")

# Replaces occurrences of a substring with another
txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three")
print(x)

x = txt.replace("one", "three", 2)
print(x)

print("\n===============================rfind()===============================\n")

# Returns the last index of the substring, or -1 if not found
txt = "Mi casa, su casa."
x = txt.rfind("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rfind("e")
print(x)

x = txt.rfind("e", 5, 10)
print(x)

print(txt.rfind("q"))
# print(txt.rindex("q")) # would raise ValueError

print("\n===============================rindex()==============================\n")

# Returns the last index of the substring, raises error if not found
txt = "Mi casa, su casa."
x = txt.rindex("casa")
print(x)

txt = "Hello, welcome to my world."
x = txt.rindex("e")
print(x)

print(txt.rfind("q"))
# print(txt.rindex("q")) # would raise ValueError

print("\n=======================rjust(length, character)======================\n")

# Right-justifies the string and pads the remaining space
txt = "banana"
x = txt.rjust(20)
print(x, "is my favorite fruit.")

x = txt.rjust(20, "O")
print(x)

print("\n=============================rpartition()============================\n")

# Splits string from the right at first occurrence of separator
txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("bananas")
print(x)

txt = "I could eat bananas all day, bananas are my favorite fruit"
x = txt.rpartition("apples")  # partition not found
print(x)

print("\n===============================rsplit()==============================\n")

# Splits the string from the right using the separator
txt = "apple, banana, cherry"
x = txt.rsplit(", ")
print(x)

# Split with maxsplit=1 (only one splits from right)
x = txt.rsplit(", ", 1)
print(x)

print("\n===============================rstrip()==============================\n")

# Remove the trailing characters if they are commas, periods, s, q, or w
txt = "banana,,,,,ssqqqww....."

x = txt.rstrip(",.qsw")

print(x)

print("\n===============================lstrip()==============================\n")

# Remove the trailing characters if they are commas, periods, a , s or w
txt = ",,,,,ssaaww.....banana"

x = txt.lstrip(",.asw")

print(x)

print("\n=============================splitlines()============================\n")

# Splits at line breaks (\n, \r, \r\n). By default, it removes them.
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)

# With True: keeps the line breaks in the result
txt = "Thank you for the music\nWelcome to \t the jungle"
x = txt.splitlines(True)
print(x)

print("\n=============================startswith()============================\n")

# Checks if the string starts with a given substring
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
print(x)

# With start and end parameters: checks within the range
x = txt.startswith("wel", 7, 20)
print(x)

txt = "Hi, welcome to my world."
# Can also check against a tuple of prefixes
x = txt.startswith(("Hello", "Hi"))
print(x)

print("\n===============================strip()===============================\n")

# Removes leading and trailing whitespace by default
txt = "     banana     "
x = txt.strip()
print("of all fruits", x, "is what I hate")

# Can also remove specific characters
txt = ",,,,,rrttgg.....banana....rrr"
x = txt.strip(".,grt")
print(x)

print("\n==============================swapcase()=============================\n")

# Swaps uppercase to lowercase and vice versa
txt = "Hello My Name Is PETER"
x = txt.swapcase()
print(x)

print("\n===============================title()===============================\n")

# Capitalizes the first character of each word
txt = "Welcome to my world"
x = txt.title()
print(x)

txt = "Welcome to my 2nd world"
x = txt.title()
print(x)

txt = "hello b2b2b2 and 3g3g3g"
x = txt.title()
print(x)

print("\n=============================translate()=============================\n")

# Replace characters using a translation table
# Replace ASCII code 83 ('S') with 80 ('P')
mydict = {83: 80}
txt = "Hello Sam!"
print(txt.translate(mydict))

# Using maketrans with single char mappings
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))

# More complex map: multiple characters
txt = "Hi Sam!"
x = "mSa"
y = "eJo"
mytable = str.maketrans(x, y)
print(txt.translate(mytable))

# maketrans with delete characters
txt = "Good night Sam!"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

# Same using direct ASCII codes in dictionary
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))

print("\n===============================zfill()===============================\n")

# Pads string on the left with zeros until it reaches the specified length
txt = "50"
x = txt.zfill(10)
print(x)

a = "hello"
b = "welcome to the jungle"
c = "10.000"

print(a.zfill(10))
print(b.zfill(10))
print(c.zfill(10))
