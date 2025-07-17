"""
Exercise Description 
    Write a drawPyramid() function with a height parameter. The top of the pyramid has one 
centered hashtag character, and the subsequent rows have two more hashtags than the previous row. 
The number of rows matches the height integer. There are no Python assert statements to check 
the correctness of your program. Instead, you can visually inspect the output yourself. For example, 
calling drawPyramid(8) would output the following: 
        #
       ###
      #####
     #######
    #########
   ###########
  #############
 ###############
"""

def drawPyramid(height):
    last = "#"
    print(f"{last}".center(height*2," "))
    for _ in range(1,height):
        last += f"{"#" * 2}"
        print(f"{last}".center(height*2 ," "))
drawPyramid(8)
drawPyramid(9)

# bro i’m losing my mind 💀💀 wtf is this??
# looked at chatgpt’s code and took the fattest L 😭

def drawPyramid(height):
    if height < 1:
        return
    
    for i in range(height):
        num_hashes = 2 * i + 1
        num_spaces = height - i - 1
        print(' ' * num_spaces + '#' * num_hashes)

drawPyramid(8)
drawPyramid(9)