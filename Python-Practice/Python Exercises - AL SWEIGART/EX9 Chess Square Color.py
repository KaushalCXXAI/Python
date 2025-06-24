"""
Exercise Description
    Write a getChessSquareColor() function that has parameters column and row. The
function either returns 'black' or 'white' depending on the color at the specified column and
row. Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and
end at 7 like in Figure 9-1. If the arguments for column or row are outside the 0 to 7 range, the
function returns a blank string.
Note that chess boards always have a white square in the top left corner.

  0 1 2 3 4 5 6 7
0 □ ■ □ ■ □ ■ □ ■ 
1 ■ □ ■ □ ■ □ ■ □ 
2 □ ■ □ ■ □ ■ □ ■ 
3 ■ □ ■ □ ■ □ ■ □ 
4 □ ■ □ ■ □ ■ □ ■ 
5 ■ □ ■ □ ■ □ ■ □ 
6 □ ■ □ ■ □ ■ □ ■ 
7 ■ □ ■ □ ■ □ ■ □ 

These Python assert statements stop the program if their condition is False. Copy them to 
the bottom of your solution program. Your solution is correct if the following assert statements’
conditions are all True:
assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == 'white'
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''

"""
def getChessSquareColor(column, row):
    if  0 <= column <= 7 and  0 <= row <= 7 :
        if column == row :
            return 'white'
        if (column % 2 == 0 and row % 2 == 0):
            return 'white'
        else:
            return 'black'
    else:
        return ''
    
assert getChessSquareColor(1, 1) == 'white'
assert getChessSquareColor(2, 1) == 'black'
assert getChessSquareColor(1, 2) == 'black'
assert getChessSquareColor(8, 8) == ''
assert getChessSquareColor(0, 8) == ''
assert getChessSquareColor(2, 9) == ''

# better varison than mine
def getChessSquareColor(column, row):
    if 0 <= column <= 7 and 0 <= row <= 7:
        return 'white' if (column + row) % 2 == 0 else 'black'
    else:
        return ''