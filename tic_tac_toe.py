import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

current_Player = "X"
winner = None
game_Running = True

#printing the game board
def printBoard(board) :
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#take player input
def playerInput(board) :
    data = int(input("Enter a number 1-9 : "))
    if data >= 1 and data <= 9 and board[data-1] == "-" :
        board[data-1] = current_Player
    else :
        print("Sorry! Player is already in that spot.")


#check for win or tie
def checkHorizontle(board) :
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-" :
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-" :
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-" :
        winner = board[6]
        return True
    
def checkRow(board) :
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-" :
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-" :
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-" :
        winner = board[2]
        return True
    

def checkDiagonal(board) :
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-" :
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-" :
        winner = board[2]
        return True
    

def checkTie(board) :
    global game_Running
    if "-" not in board :
        printBoard(board)
        print("It is a tie!")
        game_Running = False


def checkWin() :
    if checkDiagonal(board) or checkHorizontle(board) or checkRow(board) :
        print(f'The winner is {winner}')

#switch the player
def switchPlayer() :
    global current_Player
    if current_Player == "X" :
        current_Player = "O"

    else :
        current_Player = "X"


#computer
def computer(board) :
    while current_Player == "O" :
        position = random.randint(0, 8)
        if board[position] == "-" :
            board[position] = "O"
            switchPlayer()

#check for win or tie again

while game_Running :
    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)
    














