board = []
box = 0

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

    for row in board:   
        print (row)


# one     = board[0][0]
# two     = board[0][1]
# three   = board[0][2]
# four    = board[1][0]
# five    = board[1][1]
# six     = board[1][2]
# seven   = board[2][0]
# eight   = board[2][1]
# nine    = board[2][2]


# board[0][0] = " ROOK "
# board[0][7] = " ROOK "
# board[7][0] = " ROOK "
# board[7][7] = " ROOK "
# board[4][2] = "KNIGHT"
# board[3][4] = " PAWN "
