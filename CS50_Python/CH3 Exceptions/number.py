# # This causes an error when the user enters the wrong type of input,
# # like a string instead of an integer, and the program stops working.

# x = int(input("What's x?"))
# print(f"X is {x}")


# # This version uses a try-except block to catch errors when the user
# # enters a non-integer value. Instead of crashing, it shows a friendly message.

# try:
#     x = int(input("What's x?"))  
#     print(f"X is {x}")           
# except ValueError:
#     print("x is not a number")   


# # If the input can't be converted to an integer, `int(input(...))` raises a ValueError.
# # Python immediately jumps to the `except` block and skips the assignment to `x`.
# # As a result, `x` is never defined.
# # When we try to print `x` outside the try-except block, it throws a NameError 
# # because the variable `x` doesn't exist in that scope yet.

# try:
#     x = int(input("What's x?"))
# except ValueError:
#     print("x is not a number")

# print(f"X is {x}")  # This line causes a NameError if input was invalid


# # - The `try` block attempts to convert user input to an integer.
# # - If the conversion fails, a ValueError is raised, and the `except` block runs.
# # - If the conversion succeeds, Python skips the `except` and runs the `else` block.
# # - Since `print(f"X is {x}")` is inside the `else`, it only runs if `x` was successfully defined.
# # - This ensures `x` is always defined when we try to use it—no crash!

# try:
#     x = int(input("What's x?"))
# except ValueError:
#     print("x is not a number")
# else:
#     print(f"X is {x}")


# # - The `while True` creates an infinite loop.
# # - Inside the `try` block, it tries to convert the input to an integer.
# # - If the conversion fails, it throws a ValueError and prints "x is not a number".
# # - The `else` block only runs if no error occurs, which means the input was valid.
# # - The `break` inside `else` exits the loop, so the program moves on.
# # - After the loop, `x` is guaranteed to be a valid integer, so printing is safe.

# while True:
#     try:
#         x = int(input("What's x?"))
#     except ValueError:
#         print("x is not a number")
#     else:
#         break

# print(f"X is {x}")


# def main():
#     # Ask for x using a custom prompt
#     x = get_int("What's x? ")
#     print(f"x is {x}")

# def get_int(prompt):
#     # Keep prompting the user until a valid integer is entered
#     while True:
#         try:
#             return int(input(prompt))  # Try converting input to an integer
#         except ValueError:
#             # If input is invalid, silently retry
#             pass

# main()