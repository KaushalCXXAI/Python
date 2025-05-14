# # print() is a function that prints the data given to it
# print("Hello, World!")
# print('Hello, Kaushal')

# # input() allows the user to provide input
# # it takes a string argument as a prompt or question
# name = input("What is your name? ")

# # Concatenation and comma usage in print()
# print("Hello, " + name)
# print("Hello,", name)

# # print() can take optional arguments: sep and end
# # print(*objects, sep=" ", end="\n") — these are the default arguments

# # sep="&" inserts '&' between objects
# print("Hello", name, sep="&")

# # end="||" ends the output with '||' instead of a newline
# print("Hello", name, end="||\n")

# # f-strings allow expressions inside strings
# print(f"Hello, {name}")

# # strip() removes whitespace from the beginning and end
# # Example: "   Kaushal   " → "Kaushal"
# name = name.strip()
# print(f"My name is {name}")

# # capitalize() capitalizes the first character
# # Example: "kaushal" → "Kaushal"
# name = name.capitalize()
# print(f"My name is {name}")

# # title() capitalizes the first letter of each word
# # Example: "kaushal rangani" → "Kaushal Rangani"
# name = name.title()
# print(f"My name is {name}")

# # Combine all string cleanup in one line
# name = input("What is your name? ").strip().title()
# print(f"My name is {name}")

# # split() can separate full name into first and last name
# # Example: "Kaushal Rangani" → ["Kaushal", "Rangani"]
# first, last = name.split(" ")
# print(f"Hello, {first}")

# # Define a function to avoid repeating print("Hello")
# # def defines a function in Python


# def hello(to):
#     print(f"Hello, {to}")

# name = input("What is your name? ").strip().title()
# hello(name)

# #we can also give default value to parament

# def hello(to="world"):
#     print("hello, ", to)

# hello()

# name = input("What is your name? ").strip().title()
# hello(name)


# # If we try to use (call) a function *before* it is defined,
# # Python throws a NameError because it doesn’t know what ‘hello’ is yet.

# hello()  # This will raise an error: NameError: name 'hello' is not defined

# def hello(to="world"):
#     print("hello,", to)

# # Correct way: define functions before you use them

# def main():
#     name = input("What is your name? ").strip().title()
#     hello(name)

# def hello(to="world"):
#     print("hello,", to)

# # We have defined everything, but nothing runs unless we call main()

# main()  # This kicks everything off

# # We define main(), where we get the user's name
# def main():
#     name = input("What is your name? ").strip().title()
#     hello()  # calling hello() without passing 'name'

# # This function tries to use 'name', but 'name' is not defined here
# # It exists only inside main(), not globally
# def hello():
#     print("hello,", name)  # causes NameError

# main()

