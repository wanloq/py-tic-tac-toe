import random

board = []
box = 0
def cMove():
    random.choice(moves)


for column in range(3):
    # print("+", "-"*7, sep="", end="+")
    row = [box for column in range(3)]
    board.append(row)

board[0][0] = '1'
board[0][1] = '2'
board[0][2] = '3'
board[1][0] = '4'
board[1][1] = 'X'
board[1][2] = '6'
board[2][0] = '7'
board[2][1] = '8'
board[2][2] = '9'

moves = {1:'one',
         2:'two',
         3:'three',
         4:'four',
         5:'five',
         6:'six',
         7:'seven',
         8:'eight',
         9:'nine'
          }

for row in board:  
    print (row)

while True:
    uMove = int(input("Enter your move: "))
    if uMove in moves:
        print('good move amigo: ', moves[uMove])
        if uMove == 1:
            board[0][0] = '0'
        elif uMove == 2:
            board[0][1] = '0'
        elif uMove == 3:
            board[0][2] = '0'
        elif uMove == 4:
            board[1][0] = '0'
        elif uMove == 5:
            board[1][1] = 'O'
        elif uMove == 6:
            board[1][2] = '0'
        elif uMove == 7:
            board[2][0] = '0'
        elif uMove == 8:
            board[2][1] = '0'
        elif uMove == 9:
            board[2][2] = '0'

        moves.pop(uMove)
        cMove()

    for row in board:   
        print (row)
