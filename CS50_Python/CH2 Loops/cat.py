# Simplest approach: print "meow" three times (not scalable)
print("meow")
print("meow")
print("meow")

# First while loop version: count down from 3 to 0
i = 3  # Initialize counter variable
while i != 0:  # Continue looping while i is not equal to 0
    print("meow")
    i = i - 1  # Decrement i by 1 each iteration (count down)

# Second while loop version: count up from 0 to 2 (more conventional)
i = 0  # Initialize counter variable starting at 0
while i < 3:  # Continue looping while i is less than 3
    print("meow")
    # i = i + 1  # Increment i by 1 each iteration (original version)
    i += 1  # More concise way to increment i (Pythonic version)