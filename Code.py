import random


def getEmpty(board):
    return [idx for idx, value in enumerate(board) if (value != 'X' and value != 'O')]


def winCheck(board, currPlayer):
    if (
        (board[0] == board[1] == board[2] == currPlayer) or
        (board[3] == board[4] == board[5] == currPlayer) or
        (board[6] == board[7] == board[8] == currPlayer) or
        (board[0] == board[3] == board[6] == currPlayer) or
        (board[1] == board[4] == board[7] == currPlayer) or
        (board[2] == board[5] == board[8] == currPlayer) or
        (board[0] == board[4] == board[8] == currPlayer) or
        (board[2] == board[4] == board[6] == currPlayer)
    ):
        return True
    else:
        return False


def minimax(board, currPlayer):
    emptyBoard = getEmpty(board)
    if (winCheck(board, hu)):
        return 0, -1
    elif (winCheck(board, ai)):
        return 0, 1
    elif (len(emptyBoard) == 0):
        return 0, 0
    allTestPos = []
    allTestScore = []
    for i in range(len(emptyBoard)):
        currTestPos = emptyBoard[i]
        board[emptyBoard[i]] = currPlayer
        if (currPlayer == ai):
            null, result = minimax(board, hu)
            currTestScore = result
        else:
            null, result = minimax(board, ai)
            currTestScore = result
        board[emptyBoard[i]] = currTestPos
        allTestPos.append(currTestPos)
        allTestScore.append(currTestScore)
    if (currPlayer == ai):
        maxScore = -10
        for i in range(len(allTestPos)):
            if (allTestScore[i] > maxScore):
                maxScore = allTestScore[i]
                bestPlayPos = allTestPos[i]
                bestPlayScore = allTestScore[i]
    else:
        minScore = 10
        for i in range(len(allTestPos)):
            if (allTestScore[i] <= minScore):
                minScore = allTestScore[i]
                bestPlayPos = allTestPos[i]
                bestPlayScore = allTestScore[i]
    return bestPlayPos, bestPlayScore


def change(board, currPlayer, pos):
    board[pos] = currPlayer


def show(board):
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])
    print()


board = [0, 1, 2,
         3, 4, 5,
         6, 7, 8]
hu = input("Enter which player you want to be(X/O): ")
if (hu == 'x' or hu == 'X'):
    hu = 'X'
    ai = 'O'
elif (hu == 'o' or hu == 'O'):
    ai = 'X'
    hu = 'O'
else:
    print("Wrong input try again.")
print("Starting board: ")
show(board)
x = input("Do you want to play first(Y/N): ")
if (x == 'N' or x == 'n'):
    change(board, ai, random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    show(board)
while (len(getEmpty(board)) != 0 and winCheck(board,hu) != True and winCheck(board,ai) !=True):
    pos = int(input("Enter the position: "))
    change(board, hu, pos)
    m, n = minimax(board, ai)
    change(board, ai, m)
    show(board)
print("GAME ENDED.")
if (winCheck(board, hu)):
    print("You have won.")
elif (winCheck(board, ai)):
    print("Computer has won.")
else:
    print("Game Tied.")
