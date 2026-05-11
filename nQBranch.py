
N = 4

board = [[0 for _ in range(N)] for _ in range(N)]


left_row = [False] * N
upper_diagonal = [False] * (2 * N - 1)
lower_diagonal = [False] * (2 * N - 1)



def print_board():

    for row in board:
        print(" ".join("Q" if x else "." for x in row))

    print()

def solve(col):

    if col >= N:
        print_board()
        return True

    for row in range(N):

        
        if (left_row[row] == False and
            lower_diagonal[row + col] == False and
            upper_diagonal[N - 1 + col - row] == False):

            
            board[row][col] = 1

            left_row[row] = True
            lower_diagonal[row + col] = True
            upper_diagonal[N - 1 + col - row] = True

            if solve(col + 1):
                return True

            
            board[row][col] = 0

            left_row[row] = False
            lower_diagonal[row + col] = False
            upper_diagonal[N - 1 + col - row] = False

    return False



if solve(0) == False:
    print("No Solution")