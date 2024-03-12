# This function checks the current state of the tic-tac-toe board and determines the outcome of the game.
# It first checks for a winning condition by comparing the values of the diagonals. If any diagonal has the same non-empty value, it returns the winner.
# Next, it checks for a winning condition by comparing the values of the anti-diagonals. If any anti-diagonal has the same non-empty value, it returns the winner.
# If there are no winning conditions, it checks if there are any empty spaces on the board. If there are, it returns 'Game not finished'.
# If none of the above conditions are met, it means the game is a draw and it returns 'Draw'.


def calcWinState(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0] + ' wins'

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col] + ' wins'

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0] + ' wins'
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2] + ' wins'

    # Check if the game has not finished
    if any(' ' in row for row in board):
        return 'Game not finished'

    # If none of the above conditions are met, it's a draw
    return 'Draw'
