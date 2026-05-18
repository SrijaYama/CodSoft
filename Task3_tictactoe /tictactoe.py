board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]

def show():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

def check(p):
    win = [
        [0,1,2],
        [3,4,5],
        [6,7,8],
        [0,3,6],
        [1,4,7],
        [2,5,8],
        [0,4,8],
        [2,4,6]
    ]

    for i in win:
        if board[i[0]] == p and board[i[1]] == p and board[i[2]] == p:
            return True

    return False

def full():
    return " " not in board

def player():
    while True:

        move = input("Enter position (1-9): ")

        if move.isdigit():

            move = int(move) - 1

            if move >= 0 and move <= 8:

                if board[move] == " ":
                    board[move] = "X"
                    break

                else:
                    print("Position already filled")

            else:
                print("Enter number from 1 to 9")

        else:
            print("Enter only numbers")

def minimax(ai):

    if check("O"):
        return 1

    if check("X"):
        return -1

    if full():
        return 0

    if ai:

        best = -100

        for i in range(9):

            if board[i] == " ":
                board[i] = "O"

                score = minimax(False)

                board[i] = " "

                if score > best:
                    best = score

        return best

    else:

        best = 100

        for i in range(9):

            if board[i] == " ":
                board[i] = "X"

                score = minimax(True)

                board[i] = " "

                if score < best:
                    best = score

        return best

def computer():

    best = -100
    move = 0

    for i in range(9):

        if board[i] == " ":
            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best:
                best = score
                move = i

    board[move] = "O"

print("TIC TAC TOE")
print("You = X")
print("Computer = O")

while True:

    show()

    player()

    if check("X"):
        show()
        print("You Win")
        break

    if full():
        show()
        print("Match Draw")
        break

    computer()

    if check("O"):
        show()
        print("Computer Wins")
        break

    if full():
        show()
        print("Match Draw")
        break
