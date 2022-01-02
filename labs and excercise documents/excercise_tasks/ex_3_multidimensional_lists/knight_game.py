def read_matrix():
    board = []
    for _ in range(n):
        line = [x for x in input()]
        board.append(line)
    return board


def is_valid(pos,size):
    row = pos[0]
    col = pos[1]
    return  0 <= row < size and 0 <= col < size


def get_killed_knights(row,col,size,board):
    killed_knights = 0
    rows = [-2, -1, 1,2, 2, 1,-1,-2]
    cols = [1, 2, 2,1, -1, -2,-2,-1]
    for i in range(8):
        current_pos = [row + rows[i], col + cols[i]]
        if is_valid(current_pos, size) and board[current_pos[0]][current_pos[1]] == "K":
            killed_knights += 1
    return killed_knights


n = int(input())
board = read_matrix()
total_kills =0
while True:

    most_kills = 0
    to_be_killed = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                killed_knights = get_killed_knights(row,col,n, board)
                if killed_knights > most_kills:
                    most_kills = killed_knights
                    to_be_killed = [row,col]
    if most_kills == 0:
        break
    to_be_killed_row = to_be_killed[0]
    to_be_killed_col = to_be_killed[1]
    board[to_be_killed_row][to_be_killed_col] = "0"
    total_kills += 1


print(total_kills)
