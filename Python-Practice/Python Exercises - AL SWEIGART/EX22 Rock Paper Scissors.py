"""
Exercise Description
    Write a rpsWinner() function with parameters player1 and player2. These parameters are
passed one of the strings 'rock', 'paper', or 'scissors' representing that player's move. If
this results in player 1 winning, the function returns 'player one'. If this results in player 2
winning, the function returns 'player two'. Otherwise, the function returns 'tie'.
These Python assert statements stop the program if their condition is False. Copy them to
the bottom of your solution program. Your solution is correct if the following assert statements'
conditions are all True:
assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'
"""

# Oh Man i can't belive my OG code is that best version already approved by chatgpt and
# the auther had even more dumb version if chaining elif conditions

def rpsWinner(player1, player2):
    rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if player1 == player2:
        return 'tie'
    elif rules[player1] == player2:
        return 'player one'
    else:
        return 'player two'

assert rpsWinner('rock', 'paper') == 'player two'
assert rpsWinner('rock', 'scissors') == 'player one'
assert rpsWinner('paper', 'scissors') == 'player two'
assert rpsWinner('paper', 'rock') == 'player one'
assert rpsWinner('scissors', 'rock') == 'player two'
assert rpsWinner('scissors', 'paper') == 'player one'
assert rpsWinner('rock', 'rock') == 'tie'
assert rpsWinner('paper', 'paper') == 'tie'
assert rpsWinner('scissors', 'scissors') == 'tie'