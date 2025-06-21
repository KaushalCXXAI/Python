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



