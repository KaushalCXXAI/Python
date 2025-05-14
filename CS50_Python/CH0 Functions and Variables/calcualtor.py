# # int means integer — int() converts the value inside the parentheses to an integer
# # input() takes input from the user and always returns a string

# x = input("What's x? ")
# y = input("What's y? ")

# z = int(x) + int(y)

# print(z)

# # A better way to write this using direct conversion:
# x = int(input("What's x? "))
# y = int(input("What's y? "))

# print(f"{x + y}")

# # float means floating-point number — float() converts the input to a decimal number

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# print(f"{x + y}")

# # Now, if we want to round the result to the nearest whole number, we can use round()

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# z = round(x + y)  # round() rounds the floating-point result to the nearest integer

# # The :, in the format string adds a comma as a thousands separator (e.g., 1,000)
# print(f"{z:,}")

# x = float(input("What's x? "))
# y = float(input("What's y? "))

# # round(x / y, 2) rounds the division result to 2 decimal places
# z = round(x / y, 2)
# print(z)

# # Or we can achieve the same output using string formatting:
# z = x / y
# # The .2f format specifier means "floating-point number with 2 digits after the decimal point"
# print(f"{z:.2f}")

# # The return keyword in Python is used to send the result of a function back to the caller.
# # It effectively ends the function and provides the calculated value.

# def main():
#     x = int(input("What's x? "))
#     print("x squared is", square(x))

# def square(n):
#     # Return the square of n
#     return n * n  # we can also use n ** 2 | pow(n, 2)

# main()