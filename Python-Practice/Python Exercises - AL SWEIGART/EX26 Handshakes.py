"""
Exercise Description 
    Write a function named printHandshakes() with a list parameter named people which will 
be a list of strings of people's names. The function prints out 'X shakes hands with Y', where 
X and Y are every possible pair of handshakes between the people in the list. No duplicates are 
permitted: if "Alice shakes hands with Bob" appears in the output, then "Bob shakes hands with 
Alice" should not appear. 
For example, printHandshakes(['Alice', 'Bob', 'Carol', 'David']) should 
print: 
Alice shakes hands with Bob 
Alice shakes hands with Carol 
Alice shakes hands with David 
Bob shakes hands with Carol 
Bob shakes hands with David 
Carol shakes hands with David 
The printHandshakes() function must also return an integer of the number of handshakes. 
These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the output displays all possible 
handshakes and the following assert statements' conditions are all True: 
assert printHandshakes(['Alice', 'Bob']) == 1 
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3 
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
"""

def printHandshakes(people):
    total_shakes = 0
    for X in people:
        shake_with = people[people.index(X)+1:]
        for Y in shake_with:
            print(f"{X} shakes hands with {Y}")
            total_shakes += 1
    return total_shakes

assert printHandshakes(['Alice', 'Bob']) == 1 
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3 
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

# My solution works and is quite clever (according to gpt) because it uses slicing to skip earlier people ,
# so it only prints each unique handshake once.
# BUT there's one bug: people.index(X) always returns the index of the first occurrence of X.
# So if the list has duplicate names, the output will be wrong or miss some handshakes.
# Below is GPT's alternative solution, which is more robust because it uses indices directly
# and works correctly even when there are duplicate names.

def printHandshakes(people):
    handshakes = 0
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            print(f"{people[i]} shakes hands with {people[j]}")
            handshakes += 1
    return handshakes


# Add the assert statements to verify correctness
assert printHandshakes(['Alice', 'Bob']) == 1
assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6

