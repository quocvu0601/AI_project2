import os
import numpy as np
import sys
from support_functions import assign_matrix

np.set_printoptions(linewidth=sys.maxsize)


# Load map
def get_board(path_board):
    result = np.loadtxt(f"{path_board}", dtype=str, delimiter=',')
    return result


# Load all map
def get_boards(path_boards):
    os.chdir(path_boards)
    list_boards = []
    for file in os.listdir():
        if file.endswith(".txt"):
            file_path = f"{path_boards}/{file}"
            board = get_board(file_path)
            list_boards.append(board)
    return list_boards


def add_spaces(board):
    cp_board = assign_matrix(board)
    for i in range(0, len(cp_board)):
        for j in range(0, len(cp_board[i])):
            cp_board[i][j] = cp_board[i][j] + ' '
    return cp_board


def add_mountain(path_mountain, board):
    cp_board = assign_matrix(board)
    mountains = np.loadtxt(f"{path_mountain}", delimiter=',')
    for mountain in mountains:
        mountain = np.array(mountain).astype(int)
        if cp_board[mountain[0]][mountain[1]] != '0 ':
            cp_board[mountain[0]][mountain[1]] = str(cp_board[mountain[0]][mountain[1]][0]) + 'M'
    return np.array(cp_board)


def add_prison(path_prison, board):
    cp_board = assign_matrix(board)
    prisons = np.loadtxt(f"{path_prison}", delimiter=',')
    for prison in prisons:
        prison = np.array(prison).astype(int)
        if cp_board[prison[0]][prison[1]] != '0 ' and cp_board[prison[0]][prison[1]][1] != 'M':
            cp_board[prison[0]][prison[1]] = str(cp_board[prison[0]][prison[1]][0]) + 'P'
    return np.array(cp_board), prisons


def final_map(path_board, path_mountain, path_prison):
    # Tải bản đồ
    board = get_board(path_board)
    # Thêm khoảng trắng, mỗi phần tử 2 đơn vị
    cp_board = add_spaces(board)
    # Thêm núi vào bản đồ
    cp_board = add_mountain(path_mountain, cp_board)
    # Thêm nhà tù
    cp_board, _ = add_prison(path_prison, cp_board)

    return np.array(cp_board)
