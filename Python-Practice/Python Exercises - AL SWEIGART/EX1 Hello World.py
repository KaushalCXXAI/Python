"""
Exercise Description
    Write a program that, when run, greets the user by printing "Hello, world!" on the screen. Then it
prints a message on the screen asking the user to enter their name. The program greets the user by
name by printing the "Hello," followed by the user's name.
Let's use "Alice" as the example name. Your program's output should look like this:
Hello, world!
What is your name?
Alice
Hello, Alice
"""

print("Hello, world!")
print("Hello,", input("What is your name?\n").strip())