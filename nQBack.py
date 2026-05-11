N = 25

board = [[0 for _ in range(N)] for _ in range(N)]



def print_board():

    for row in board:
        print(" ".join("Q" if x else "." for x in row))

    print()



def is_safe(row, col):

   
    for i in range(col):
        if board[row][i] == 1:
            return False

    i, j = row, col

    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False

        i -= 1
        j -= 1

    
    i, j = row, col

    while i < N and j >= 0:
        if board[i][j] == 1:
            return False

        i += 1
        j -= 1

    return True



def solve(col):

    # Base case
    if col >= N:
        print_board()
        return True

    for row in range(N):

        if is_safe(row, col):

            board[row][col] = 1

            if solve(col + 1):
                return True

            
            board[row][col] = 0

    return False



if solve(0) == False:
    print("No Solution")