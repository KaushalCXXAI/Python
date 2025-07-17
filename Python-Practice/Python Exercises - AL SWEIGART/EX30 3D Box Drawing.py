"""
Exercise Description 
    Write a drawBox() function with a size parameter. The size parameter contains an integer 
for the width, length, and height of the box. The horizontal lines are drawn with - dash characters, 
the vertical lines with | pipe characters, and the diagonal lines with / forward slash characters. The 
corners of the box are drawn with + plus signs. 
There are no Python assert statements to check the correctness of your program. Instead, you 
can visually inspect the output yourself. For example, calling drawBox(1) through drawBox(5) 
would output the following boxes, respectively: 
                                                        +----------+ 
                                                       /          /| 
                                      +--------+      /          / | 
                                     /        /|     /          /  | 
                       +------+     /        / |    /          /   | 
                      /      /|    /        /  |   /          /    | 
           +----+    /      / |   /        /   |  +----------+     + 
          /    /|   /      /  |  +--------+    +  |          |    /  
  +--+   /    / |  +------+   +  |        |   /   |          |   /   
 /  /|  +----+  +  |      |  /   |        |  /    |          |  /    
+--+ +  |    | /   |      | /    |        | /     |          | /     
|  |/   |    |/    |      |/     |        |/      |          |/      
+--+    +----+     +------+      +--------+       +----------+ 
 
Size 1  Size 2      Size 3         Size 4            Size 5 

"""

def drawBox(size):
    total_height = 5
    height = 3
    breadth = 4
    in_space = 0
    out_space = 2

    # Adjust dimensions based on size
    for i in range(1, size):
        total_height += 2
        height += 1
        breadth += 2
        out_space += 1

    # Top edge
    print(f"{' ' * out_space}+{'-' * (breadth - 2)}+")
    out_space -= 1

    # Upper diagonal faces
    for th in range(total_height):
        if th < (total_height // 2 - 1):
            print(f"{' ' * out_space}/{' ' * (breadth - 2)}/{' ' * in_space}|")
            out_space -= 1
            in_space += 1

        # Middle horizontal edge
        elif th == height:
            print(f"+{'-' * (breadth - 2)}+{' ' * in_space}+")
            in_space -= 1

        # Lower diagonal faces
        elif th > (height - 1):
            print(f"|{' ' * (breadth - 2)}|{' ' * in_space}/")
            in_space -= 1

    # Bottom edge
    print(f"+{'-' * (breadth - 2)}+")

    
print("--- drawBox(1) ---")
drawBox(1)
print("\n--- drawBox(2) ---")
drawBox(2)
print("\n--- drawBox(3) ---")
drawBox(3)
print("\n--- drawBox(4) ---")
drawBox(4)
print("\n--- drawBox(5) ---")
drawBox(5)

# Since the answers from ChatGPT and Gemini were not entirely accurate, I referred to the author's solution. It uses a clever approach, which is provided below. 

def drawBox(size):
    # Special case: Draw nothing if size is less than 1:
    if size < 1:
        return

    # Draw back line on top surface:
    print(' ' * (size + 1) + '+' + '-' * (size * 2) + '+')

    # Draw top surface:
    for i in range(size):
        print(' ' * (size - i) + '/' + ' ' * (size * 2) + '/' + ' ' * i + '|')

    # Draw top line on top surface:
    print('+' + '-' * (size * 2) + '+' + ' ' * size + '+')

    # Draw front surface:
    for i in range(size - 1, -1, -1):
        print('|' + ' ' * (size * 2) + '|' + ' ' * i + '/')

    # Draw bottom lie on front surface:
    print('+' + '-' * (size * 2) + '+')

# In a loop, call drawBox() with arguments 1 to 5:
for i in range(1, 6):
    drawBox(i)

