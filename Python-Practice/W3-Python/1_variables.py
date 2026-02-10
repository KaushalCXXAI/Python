print("--------------------------------------------------------------------------------------------------------------------")

# variables can ber reassigned ansy type of data 

x = 5 
print(x)
x = 4
x = "Sally"
print(x)

print("--------------------------------------------------------------------------------------------------------------------")

# casting variable value in to some datatype

x = str(2)
y = int(3)
z = float(5)
print(x, y, z,sep="\n")

print("--------------------------------------------------------------------------------------------------------------------")

# Get the Type fo the data or variable's value

print(type(x)) 
print(type(y)) 
print(type(z)) 

print("--------------------------------------------------------------------------------------------------------------------")

x = "John"
# both are same '' / ""
x = 'John'

print("--------------------------------------------------------------------------------------------------------------------")

a = 4
A = "sally"
print("a:", a)
print("A:", A)

print("--------------------------------------------------------------------------------------------------------------------")

# assign many valuse to many variable

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("--------------------------------------------------------------------------------------------------------------------")

# one value to many variables

x = y = z = "Orange"
print(x)
print(y)
print(z)

print("--------------------------------------------------------------------------------------------------------------------")

# unpacking a list

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("--------------------------------------------------------------------------------------------------------------------")

# Global variables

x = "global"

def func():
  print("value of x is from : " + x)
func()
print("value of x outside of function:", x)

print("--------------------------------------------------------------------------------------------------------------------")

x = "global"

def MyFunc():
  x = "local"
  print("value of x in function locally:", x)
MyFunc()
print("value of x outside of function:", x)

print("--------------------------------------------------------------------------------------------------------------------")

# use the global keyword if you want to change a global variable inside a function

x = "global"

def MyFunc():
    # Tell Python that we want to use the global variable 'x', not a new local one
    global x
    print("value of x in function before modifying:", x)
    # Modify the global variable
    x = "local"
    print("value of x in function after modifying:", x)

MyFunc()
print("value of x outside of function:", x)

print("--------------------------------------------------------------------------------------------------------------------")
