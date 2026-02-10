# List is a collection which is ordered and changeable. Allows duplicate members.
print("\n==================== Basic List Creation ====================\n")
thislist = ["apple", "banana", "cherry"]
print("Initial list:", thislist)

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print("List with duplicates:", thislist)

list1 = [1, 5, 7, 9, 3]
print("List of integers:", list1)

list2 = [True, False, False]
print("List of booleans:", list2)

list1 = ["abc", 34, True, 40, "male"]
print("Mixed data types:", list1)

thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print("Using list constructor:", thislist)

print("\n==================== Access Items ====================\n")
thislist = ["apple", "banana", "cherry"]
print("Second item (index 1):", thislist[1])
print("Last item (index -1):", thislist[-1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print("Items from index 2 to 4:", thislist[2:5])
print("Items from start to index 3:", thislist[:4])
print("Items from index 2 to end:", thislist[2:])
print("Negative indexing (last 4 to last 1):", thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

print("\n==================== Modify List ====================\n")
li = [0,1,2,3,4,5,6,7,8,9]
li[1] = "changed"
print("Change single value:", li)

li = [0,1,2,3,4,5,6,7,8,9]
li[3:6] = ["changed"]
print("Change slice with one item:", li)

li = [0,1,2,3,4,5,6,7,8,9]
li[3:6] = [1,2,3,4,5,6,7,8,9]
print("Change slice with more items:", li)

print("\n==================== Insert and Append ====================\n")
li = [1,2,3,4,5,6,7,8,9]
li.insert(0,0)  # Insert at beginning
li.insert(len(li),10)  # Insert at end
li.insert(20,20)  # Index beyond range adds at end
print("Insert items:", li)

li = [0,1,2,3,4,5,6,7,8,9]
li.append(10)
print("Append item:", li)

print("\n==================== Extend with List and Tuple ====================\n")
li1 = [0,1,2,3,4]
li2 = [5,6,7,8,9]
tu1 = (10,11,12,13,0)
li1.extend(li2)
li1.extend(tu1)
print("After extend:", li1)

li1.remove(13)
li1.remove(0)
print("After remove:", li1)

print("\n==================== Pop and Delete ====================\n")
li = [0,1,2,3,4,5,6,7,8,9,10]
li.pop(1)  # Remove by index
li.pop()  # Remove last
li.pop(2)  # Remove specific index
print("After pop:", li)

li = [0,1,2,3,4,5,6,7,8,9]
del li[1]
print("After del by index:", li)

li = [0,1,2,3,4,5,6,7,8,9]
del li
try:
    print(li)
except NameError:
    print("Error: 'li' is deleted")

li = [0,1,2,3,4,5,6,7,8,9]
li.clear()
print("After clear:", li)

print("\n==================== Looping Through List ====================\n")
li = [0,1,2,3,4,5,6,7,8,9]
i = 0
print("Using while loop:", end=" ")
while i < len(li):
    print(li[i], end=", ")
    i+=1
print("\nUsing list comprehension:", end=" ")
[print(i, end=", ") for i in li]

print("\n\n==================== List Comprehension (Filter) ====================\n")
li1 = [0,1,2,3,4,5,6,7,8,9]
li2 = [i for i in li1 if 3 == i]  # Only includes 3
print("Filtered list (only 3):", li2)

print("\n==================== Conditional Expression in List Comprehension ====================\n")
# [<expression_if_true> if <condition> else <expression_if_false> for <variable> in <iterable>]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print("Replaced 'banana' with 'orange':", newlist)

# ============================================
# Python List Sorting Examples with Explanations
# ============================================

# 1. Default sort - Strings (ASCII order)
thislist = ["orange", "2mango", "kiwi", "1pineapple", "banana"]
# Sorts lexicographically: strings starting with digits come before letters
thislist.sort()
print("1. Default string sort:", thislist)

# 2. Default sort - Numbers
thislist = [100, 50, 65, 82, 23]
# Sorts in ascending numeric order
thislist.sort()
print("2. Default number sort:", thislist)

# 3. Reverse sort - Strings
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# Sorts in reverse (Z to A)
thislist.sort(reverse=True)
print("3. Reverse string sort:", thislist)

# 4. Reverse sort - Numbers
thislist = [100, 50, 65, 82, 23]
# Sorts in descending order
thislist.sort(reverse=True)
print("4. Reverse number sort:", thislist)

# 5. Custom sort using key function
def myfunc(n):
    return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
# Sorts based on distance from 50
thislist.sort(key=myfunc)
print("5. Sort by closeness to 50:", thislist)

# 6. Case-insensitive sort using str.lower
thislist = ["banana", "Orange", "Kiwi", "cherry"]
# Treats all items as lowercase while sorting
thislist.sort(key=str.lower)
print("6. Case-insensitive sort:", thislist)

# 7. Reverse only - does NOT sort
thislist = ["banana", "Orange", "Kiwi", "cherry"]
# Just reverses current list order
thislist.reverse()
print("7. Reverse list (no sort):", thislist)

# 8. Default sort with mixed cases
thislist = ["banana", "Orange", "Kiwi", "cherry"]
# Uppercase letters come before lowercase in ASCII
thislist.sort()
print("8. Default sort with mixed case:", thislist)

# 9. Case-insensitive sort again for clarity
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key=str.lower)
print("9. Case-insensitive sort (again):", thislist)

# ============================================
# Python List Copy Methods and Mutability Test
# ============================================

# Method 1: Using list.copy()
li1 = [1, 2, 3, 4, 5, 6, 7]
li2 = li1.copy()  # Shallow copy of li1
li2.pop()         # Removes the last element from li2

print("1. Original list after li2.copy() and pop():", li1)
print("1. Copied list:", li2)

# Method 2: Using list() constructor
li1 = [1, 2, 3, 4, 5, 6, 7]
li2 = list(li1)   # Creates a new list with the same elements
li2.pop()

print("2. Original list after list(li1) and pop():", li1)
print("2. Copied list:", li2)

# Method 3: Using slicing [:]
li1 = [1, 2, 3, 4, 5, 6, 7]
li2 = li1[:]      # Creates a shallow copy using slicing
li2.pop()

print("3. Original list after li1[:] and pop():", li1)
print("3. Copied list:", li2)

# ============================================
#       IMP topic for copying the list        
# ============================================

li1 = [1, 2, 3]
li2 = li1
li2.pop()
print(li1)  # This will also be modified!

a = [[1, 2], [3, 4]]
b = a.copy()  # shallow copy

b[0][0] = 999  # modify inner list element

print("a =", a)  # → [[999, 2], [3, 4]]
print("b =", b)  # → [[999, 2], [3, 4]]


original = [[1, 2], [3, 4], [5, 6],3]

# Deep copy only lists, leave other types untouched
copied = [x[:] if isinstance(x, list) else x for x in original]  # each inner list is sliced (copied)

# Now let's mutate copied
copied[0][0] = 999

print("Original:", original)  # → [[1, 2], [3, 4], [5, 6]]
print("Copied:  ", copied)    # → [[999, 2], [3, 4], [5, 6]]

# =====================================
# Python List Merging Methods Explained
# =====================================

# 1. Using the + operator (creates a new list)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2  # Creates a new list combining both
print("1. Using + operator:", list3)
# Output: ['a', 'b', 'c', 1, 2, 3]


# 2. Using append() in a loop (adds elements one-by-one)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)  # Adds each item from list2 individually
print("2. Using append in loop:", list1)
# Output: ['a', 'b', 'c', 1, 2, 3]


# 3. Using extend() (adds all elements at once)
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)  # Adds all elements from list2 to list1
print("3. Using extend:", list1)
# Output: ['a', 'b', 'c', 1, 2, 3]
a = [1, 2]
b = [3, 4]

a.append(b)
print("append:", a)  # [1, 2, [3, 4]]

a = [1, 2]
a.extend(b)
print("extend:", a)  # [1, 2, 3, 4]

# Python List Methods Cheat Sheet

# append(): Adds an element at the end of the list
# clear(): Removes all elements from the list
# copy(): Returns a shallow copy of the list
# count(): Returns the number of occurrences of a specified value
# extend(): Adds elements from an iterable to the end of the list
# index(): Returns the index of the first element with a specified value
# insert(): Adds an element at a specified position
# pop(): Removes and returns the element at a specified position (default last)
# remove(): Removes the first item with a specified value
# reverse(): Reverses the order of the list
# sort(): Sorts the list in ascending order (can use key and reverse parameters)

# Example usage:
lst = [3, 1, 4, 1, 5]

lst.append(9)           # [3, 1, 4, 1, 5, 9]
print(lst)
lst.extend([2, 6])      # [3, 1, 4, 1, 5, 9, 2, 6]
print(lst)
lst.insert(0, 7)        # [7, 3, 1, 4, 1, 5, 9, 2, 6]
print(lst.count(1))     # 2
print(lst.index(4))     # 3
lst.remove(9)           # removes 9
print(lst.pop())        # removes and prints last element (6)
lst.sort()              # sorts the list
print(lst)
lst.reverse()           # reverses the list
print(lst)
lst.clear()             # empties the list
print(lst)
