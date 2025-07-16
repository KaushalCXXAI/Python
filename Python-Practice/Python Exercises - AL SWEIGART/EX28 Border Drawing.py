"""
Exercise Description 
    Write a drawBorder() function with parameters width and height. The function draws the 
border of a rectangle with the given integer sizes. There are no Python assert statements to check 
the correctness of your program. Instead, you can visually inspect the output yourself. For example, 
calling drawBorder(16, 4) would output the following: 
+--------------+ 
|              | 
|              | 
+--------------+ 
The interior of the rectangle requires printing spaces. The sizes given include the space required 
for the corners. If the width or height parameter is less than 2, the function should print nothing.
"""

def drawBorder(width, height):
    if width < 2 or height < 2: 
        return 
    for h in range(height):
        if h == 0 or h == height-1:
            print("+" + "-" * (width-2) + "+")
        else:
            print("|" + " " * (width-2) + "|")

drawBorder(16, 4)
print("---")
drawBorder(2, 2)
print("---")
drawBorder(10, 1)  # Should print nothing
print("---")
drawBorder(3, 3)
print("---")
drawBorder(1, 1)


# Again this mf chatgpt beat me when ever i feel like i did better that mf pull even crazier comman sense like given bellow

def drawBorder(width, height):
    if width < 2 or height < 2:
        return
    
    # Top border
    print('+' + '-' * (width - 2) + '+')
    
    # Middle rows
    for _ in range(height - 2):
        print('|' + ' ' * (width - 2) + '|')
    
    # Bottom border
    print('+' + '-' * (width - 2) + '+')
drawBorder(16, 4)
print("---")
drawBorder(2, 2)
print("---")
drawBorder(10, 1)  # Should print nothing
print("---")
drawBorder(3, 3)
print("---")
drawBorder(1, 1)