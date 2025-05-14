name = input("What's your name? ")

# Traditional if-elif-else approach to determine Hogwarts house
if name == "Harry" or name == "Ron" or name == "Hermione":
    print("Griffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")

# Alternative approach using match-case (Python 3.10+ feature)
match name:
    case "Harry":
        print("Griffindor")
    case "Hermione":
        print("Griffindor")
    case "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:  # Default case (equivalent to else)
        print("Who?")

# More concise match-case version using pattern matching with |
match name:
    case "Harry" | "Hermione" | "Ron":  # Combined patterns
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:  # Default case
        print("Who?")