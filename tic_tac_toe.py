""" Tic-Tac-Toe
Love is a game of tic-tac-toe,
Constantly waiting for the next x or o.

- Lang Leav - """


#from shutil import register_unpack_format


def build_board():
    board = []
    for space in range(9):
        board.append(space + 1)
    return board    
    
layout =  build_board()   

def display_board(layout):
    print()
    print(f"{layout[0]} |{layout[1]} | {layout[2]}") 
    print(" -+-+-")
    print(f"{layout[3]} |{layout[4]} | {layout[5]}") 
    print(" -+-+-")
    print(f"{layout[6]} |{layout[7]} | {layout[8]}") 

display_board(layout)

# Build afunction to know who´s turn is.
# Return player´s sign

def turn (current):
    if current == "" or current == "o":
        return "x"
    elif current == "x":
        return "o"
    
player = turn ("")   

# Let the player isert the square they want to sing down.
# Ask for input to the currend player
# Insert the input to the game.

def make_move (player, board):
    square = int(input(f"{player}s to chosse a squere (1 - 9): "))
    board [square -1] = player 

# Check for a winner
# Check if draw - all the ssquare are not numbers no winner

def is_a_draw (board):
    for square  in range(9): 
        if board [square] != "x" and board [square]:
            return False
    return True

# Check if 3 numbers( signs) are alligned

def has_winner (board):
    return (board[0] == board[1] == board[2] or
            board[3] == board[4] == board[5] or
            board[6] == board[7] == board[8] or
            board[0] == board[3] == board[6] or
            board[1] == board[4] == board[7] or
            board[2] == board[5] == board[8] or
            board[0] == board[4] == board[8] or
            board[2] == board[4] == board[6] )
    
# Start the gam
while not (has_winner(layout) or is_a_draw (layout)):
       
     display_board(layout)
     make_move(player, layout)
     player = turn (player)
     display_board(layout)
     if has_winner(layout):
         print(f"End of the game {player} you loosed")
     elif is_a_draw(layout): 
         print(" It a draw , try again")