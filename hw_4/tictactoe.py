def count_marks(board):
    count_x = sum(row.count('X') for row in board)
    count_o = sum(row.count('O') for row in board)
    return count_x, count_o

def is_winner(board, mark):
    # check horizontal win
    for row in board:
        if all(cell == mark for cell in row):
            return True
    # check vertical win
    for col in range(3):
        if all(board[row][col] == mark for row in range(3)):
            return True
        
    # check diagonal win
    if all(board[i][i] == mark for i in range(3)) or all(board[i][2-i] == mark for i in range(3)):
        return True
    return False

def is_draw(board):
    return '#' not in ''.join(''.join(row) for row in board)

def minimax(board, turn, memo):
    board_str = ''.join(''.join(row) for row in board)

    # check memoized
    if board_str in memo:
        return memo[board_str]

    if is_winner(board, 'X'):
        memo[board_str] = 'Crosses win'
        return 'Crosses win'
    elif is_winner(board, 'O'):
        memo[board_str] = 'Noughts win'
        return 'Noughts win'
    elif is_draw(board):
        memo[board_str] = 'Draw'
        return 'Draw'

    if turn == 'O':
        best_result = 'Crosses win' # worst case scenario
        for i in range(3):
            for j in range(3):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                    result = minimax(board, 'X', memo)
                    if result == 'Noughts win':
                        memo[board_str] = 'Noughts win'
                        board[i][j] = '#'
                        return 'Noughts win'
                    elif result == 'Draw':
                        best_result = 'Draw'
                    board[i][j] = '#'
        memo[board_str] = best_result
        return best_result
    elif turn == 'X':
        best_result = 'Noughts win' # worst case scenario
        for i in range(3):
            for j in range(3):
                if board[i][j] == '#':
                    board[i][j] = 'X'
                    result = minimax(board, 'O', memo)
                    if result == 'Crosses win':
                        memo[board_str] = 'Crosses win'
                        board[i][j] = '#'
                        return 'Crosses win'
                    elif result == 'Draw':
                        best_result = 'Draw'
                    board[i][j] = '#'
        memo[board_str] = best_result
        return best_result

board = []
for _ in range(3):
    row = list(input().strip())
    board.append(row)

# whose turn?
count_x, count_o = count_marks(board)
if count_x > count_o:
    turn = 'O'
else:
    turn = 'X'

memo = {}
result = minimax(board, turn, memo)
print(result)
