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

# Simplest for loop iterating through a list of numbers
for i in [0, 1, 2]:
    print("meow")

# For loop using range() to iterate 10 times, printing the counter each time
for i in range(10):
    print(i)

# Using underscore convention when the loop variable isn't used
for _ in range(3):
    print("meow")

# Pythonic way to repeat a string using multiplication
# Note: adds newlines but needs end="" to avoid extra newline
print("meow\n" * 3, end="")

# Infinite loop to keep prompting user until positive number entered
while True:
    n = int(input("What's n? "))
    if n > 0:  # Only break if positive number entered
        break

# Print meow n times using for loop
for _ in range(n):
    print("meow")

# Main function that organizes the code better
def main():
    number = get_number()  # Get valid number from user
    meow(number)  # Meow that many times

# Function to get positive number from user
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n  # Return exits the function with the value

# Function to print meow n times
def meow(n):
    for _ in range(n):
        print("meow")

# Call main to start program execution
main()
