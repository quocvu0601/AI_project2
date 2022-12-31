import numpy as np
from support_functions import assign_matrix


def move_up(board, current_position):
    cp_board = assign_matrix(board)
    new_position = [current_position[0] - 1, current_position[1]]
    if cp_board[new_position[0]][new_position[1]] == '0 ' or cp_board[new_position[0]][new_position[1]][1] == 'M' or \
            cp_board[new_position[0]][new_position[1]][1] == 'P':
        print("Không thể di chuyển lên")
    else:
        cp_board[new_position[0]][new_position[1]] = cp_board[current_position[0]][current_position[1]]
        cp_board[current_position[0]][current_position[1]] = cp_board[current_position[0]][current_position[1]][0] + ' '
        print(f"Vị trí di chuyển đến là: hàng {new_position[0]}, cột {new_position[1]}")
    return np.array(cp_board)


def move_down(board, current_position):
    cp_board = assign_matrix(board)
    new_position = [current_position[0] + 1, current_position[1]]
    if cp_board[new_position[0]][new_position[1]] == '0 ' or cp_board[new_position[0]][new_position[1]][1] == 'M' or \
            cp_board[new_position[0]][new_position[1]][1] == 'P':
        print("Không thể di chuyển xuống")
    else:
        cp_board[new_position[0]][new_position[1]] = cp_board[current_position[0]][current_position[1]]
        cp_board[current_position[0]][current_position[1]] = cp_board[current_position[0]][current_position[1]][0] + ' '
        print(f"Vị trí di chuyển đến là: hàng {new_position[0]}, cột {new_position[1]}")
    return np.array(cp_board)


def move_left(board, current_position):
    cp_board = assign_matrix(board)
    new_position = [current_position[0], current_position[1] - 1]
    if cp_board[new_position[0]][new_position[1]] == '0 ' or cp_board[new_position[0]][new_position[1]][1] == 'M' or \
            cp_board[new_position[0]][new_position[1]][1] == 'P':
        print("Không thể di chuyển sang trái")
    else:
        cp_board[new_position[0]][new_position[1]] = cp_board[current_position[0]][current_position[1]]
        cp_board[current_position[0]][current_position[1]] = cp_board[current_position[0]][current_position[1]][0] + ' '
        print(f"Vị trí di chuyển đến là: hàng {new_position[0]}, cột {new_position[1]}")
    return np.array(cp_board)


def move_right(board, current_position):
    cp_board = assign_matrix(board)
    new_position = [current_position[0], current_position[1] + 1]
    if cp_board[new_position[0]][new_position[1]] == '0 ' or cp_board[new_position[0]][new_position[1]][1] == 'M' or \
            cp_board[new_position[0]][new_position[1]][1] == 'P':
        print("Không thể di chuyển sang phải")
    else:
        cp_board[new_position[0]][new_position[1]] = cp_board[current_position[0]][current_position[1]]
        cp_board[current_position[0]][current_position[1]] = cp_board[current_position[0]][current_position[1]][0] + ' '
        print(f"Vị trí di chuyển đến là: hàng {new_position[0]}, cột {new_position[1]}")
    return np.array(cp_board)
