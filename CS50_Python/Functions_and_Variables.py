# print is a function that prints the data given to it
print("Hello, World!")

print('Hello, Kaushal')

# input is a function that allows the user to provide input
# it takes a string argument as a prompt or question
# name = input("What is your name? ")
name = "kaushal"
print("Hello, " + name)
print("Hello,", name)

# print() can take optional arguments: (sep), (end)
# print(*objects, sep=" ", end="\n") — these are the default arguments

# sep means "separator", used between multiple objects
# Example: sep="&" will print "Hello&Kaushal"
print("Hello", name, sep="&")

# end determines how the output should end
# Example: end="||" will output "Hello Kaushal||"
print("Hello", name, end="||")

# format string
# f-string is a way to format strings in Python
# it allows you to embed expressions inside string literals
# Example: f"Hello, {name}" will output "Hello, Kaushal"
print(f"Hello, {name}")


