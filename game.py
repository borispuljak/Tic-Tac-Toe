from IPython.display import clear_output
import random

print ("Tic-Tac-Toe")

def display_board(board):
    clear_output()
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " +board[9])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " +board[6])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " +board[3])
    print("   |   |   ")

def choose_first():

    first = random.randint(0,1)

    if first == 0:
        return "Player 1"
    elif first == 1:
        return "Player 2"
    else:
        return ""

def player_input():

    selection = ""

    while selection != "X" and selection != "O":
        selection = input ("Player 1: Choose X or O: ").upper()
    
    if selection == "X":
        return ("X","O")
    elif selection == "O":
        return ("O","X")
    else:
        return ("","")

def place_selection(board, selection, position):
    board[position] = selection

def player_choice(board):

    position = 0

    while position not in range (1,10) or not space_check(board, position):
        position = int (input ("Choose a position: (Enter: 1-9) "))

    return position

def space_check(board, position):
    return board[position] ==" "

def full_check(board):
    for i in range (1,10):
        if space_check(board, i):
            return False
    return True

def win_check(board, selection):
    return ((board[1]==selection and board[2]==selection and board[1]==selection) or
            (board[4]==selection and board[5]==selection and board[6]==selection) or
            (board[7]==selection and board[8]==selection and board[9]==selection) or
            (board[1]==selection and board[4]==selection and board[7]==selection) or
            (board[2]==selection and board[5]==selection and board[8]==selection) or
            (board[3]==selection and board[6]==selection and board[9]==selection) or
            (board[1]==selection and board[5]==selection and board[9]==selection) or
            (board[3]==selection and board[5]==selection and board[7]==selection))

def replay():
    return input ("Do you want to play again? (Enter: y or n) ").lower()

while True:
    board = [" "] *10

    player1_selection, player2_selection = player_input()

    turn = choose_first()
    print(turn + " will go first")

    play_game = input ("Ready to play? (Enter: y or n) ").lower()

    if play_game == "y":
        game_on = True
    elif play_game == "n":
        game_on = False
    else:
        game_on = ""

    while game_on:
        if turn == "Player 1":
            display_board(board)
            position = player_choice(board)
            place_selection(board, player1_selection, position)
            if win_check(board, player1_selection):
                display_board(board)
                print("Player 1 won the game")
                game_on = False
        
        elif turn == "Player 2":

        
        else:
