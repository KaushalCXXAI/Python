"""
Exercise Description 
    Write a drawRectangle() function with two integer parameters: width and height. The 
function doesn't return any values but rather prints a rectangle with the given number of hashtags in 
the horizontal and vertical directions. 
There are no Python assert statements to check the correctness of your program. Instead, you 
can visually inspect the output yourself. For example, calling drawRectangle(10, 4) should 
produce the following output: 
########## 
########## 
########## 
########## 
If either the width or height parameter is 0 or a negative number, the function should print 
nothing.
"""

def drawRectangle(width, height):
    if width < 1 or height < 1: 
        return 
    for i in range(height):
        for j in range(width):
            print('#', end="")
        print()

drawRectangle(10, 4)
print("---")
drawRectangle(5, 0)   # Should print nothing
print("---")
drawRectangle(-2, 3)  # Should print nothing
print("---")
drawRectangle(3, 2)


# the gpt's version is so clever when will i beat it

def drawRectangle(width, height):
    # Check for invalid sizes; if width or height is <= 0, do nothing
    if width <= 0 or height <= 0:
        return

    # Loop for each row
    for _ in range(height):
        print('#' * width)

drawRectangle(10, 4)
print("---")
drawRectangle(5, 0)   # Should print nothing
print("---")
drawRectangle(-2, 3)  # Should print nothing
print("---")
drawRectangle(3, 2)

