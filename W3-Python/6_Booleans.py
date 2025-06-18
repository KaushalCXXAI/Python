# Comparison operations result in boolean values
print("10 > 9\t\t:", 10 > 9)      # True
print("10 == 9\t\t:", 10 == 9)    # False
print("10 < 9\t\t:", 10 < 9)      # False

print("\n# Non-empty values evaluate to True")
print("bool(\"Hello\")\t:", bool("Hello"))   # True
print("bool(15)\t:", bool(15))               # True
print("(\"\",\"\") tuple\t:",bool(("","")))  # True
print("[\"\",\"\"] list\t:", bool(["",""]))  # True
print("{\"\":\"\"} dict\t:", bool({"":""}))  # True

# Assign and evaluate variables
x = "Hello"
y = 15

print("bool(x)\t\t:", bool(x))    # True
print("bool(y)\t\t:", bool(y))    # True

print("\n# Values that evaluate to False in Python")
print("False\t\t:", bool(False))         # Literal False
print("None\t\t:", bool(None))           # NoneType
print("0\t\t:", bool(0))                 # Zero (int)
print("Empty str\t:", bool(""))          # Empty string
print("Empty () tuple\t:",bool(()))      # Empty tuple
print("Empty [] list\t:", bool([]))      # Empty list
print("Empty {} dict\t:", bool({}))      # Empty dictionary

x = 200
print(isinstance(x, int))