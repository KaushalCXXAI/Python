# Get two integers from the user
x = int(input("What's x? "))
y = int(input("What's y? "))

# First approach: using multiple independent if statements
# This asks all three questions regardless of previous answers
if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")

# Second approach: using elif to make conditions mutually exclusive
# Only asks subsequent questions if previous ones were false
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")

# Third approach: using else as a catch-all
# Most efficient version - only asks necessary questions
if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")

# Fourth approach: using 'or' to combine conditions
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Fifth approach: using != operator for inequality
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")

# Sixth approach: alternative ordering of equality check
if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")