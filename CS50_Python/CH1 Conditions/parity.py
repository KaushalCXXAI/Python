def main():

    x = int(input("What's x? "))
    
    # Alternative conditional approach:
    # if x % 2 == 0:
    #     print("even")
    # else:
    #     print("odd")
    
    # Use the is_even function to check parity and print result
    if is_even(x):
        print("even")
    else:
        print("odd")

# Define a function to check if a number is even using modulo operator
def is_even(n):
    # Most Pythonic version: directly return the boolean result of the condition
    return (n % 2 == 0)
    
    # Alternative versions:
    # return True if n % 2 == 0 else False  # Pythonic conditional expression
    # if n % 2 == 0:                        # Traditional if-else approach
    #     return True
    # else:
    #     return False

main()