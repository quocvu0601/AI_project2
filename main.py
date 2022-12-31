'''
. : chưa check
_ : đã check và sai
+ : đã check và đúng
'''

import os
import numpy as np
import sys
from random import randint

from find_shortest_path import bfs
from move import *
from hints import choice_hint, hint_1

np.set_printoptions(linewidth=sys.maxsize)

def get_data(path_board):
    f = open(path_board, "r")
    lines = f.readlines()
    w = lines[0].split()[0]
    h = lines[0].split()[1].replace("\n", "")
    turn_pirate_reveals = int(lines[1])
    turn_pirate_free = int(lines[2])
    num_regions = int(lines[3])
    treasure_position = np.array([lines[4].replace("\n", "").split()[0], lines[4].replace("\n", "").split()[1]]).astype(
        int)
    broad = []
    for l in lines[5:]:
        broad_i = []
        for x in l.split(";"):
            x = x.replace("\n", "")
            if len(x) < 2:
                x = x + ' '
            broad_i.append(x)
        broad.append(broad_i)
    broad = np.array(broad)
    return w, h, turn_pirate_reveals, turn_pirate_free, num_regions, treasure_position, broad


def get_agent_position(board):
    h, w = np.array(board).shape
    while True:
        r = randint(0, h - 1)
        c = randint(0, w - 1)
        if board[r][c] != '0 ' and board[r][c][1] != 'P' and board[r][c][1] != 'M':
            agent_position = [r, c]
            break
    return agent_position


def add_agent_position(board):
    cp_board = assign_matrix(board)
    agent_position = get_agent_position(board)
    cp_board[agent_position[0]][agent_position[1]] = cp_board[agent_position[0]][agent_position[1]][0] + 'A'
    return np.array(cp_board), agent_position


def find_pirate_position(board):
    prison_positions = []
    for i in range(0, len(board)):
        for j in range(0, len(board[i])):
            if board[i][j][1] == 'P':
                prison_positions.append([i, j])
    num_prisions = len(prison_positions)
    rad_int = randint(0, num_prisions - 1)
    pirate_position = prison_positions[rad_int]
    pirate_position = np.array(pirate_position).astype(int)
    return pirate_position


def add_pirate_position(path_prison, board):
    cp_board = assign_matrix(board)
    pirate_position = find_pirate_position(path_prison, board)
    cp_board[pirate_position[0]][pirate_position[1]] = cp_board[pirate_position[0]][pirate_position[1]][0] + 'p'
    return np.array(cp_board)


def agent_action_scan(treasure_position, agent_position, size):
    check_box = []
    check_box.append([agent_position[0], agent_position[1]])
    check_box.append([agent_position[0] - 1, agent_position[1]])
    check_box.append([agent_position[0] + 1, agent_position[1]])
    check_box.append([agent_position[0], agent_position[1] - 1])
    check_box.append([agent_position[0], agent_position[1] + 1])
    if size == 2:
        check_box.append([agent_position[0] - 2, agent_position[1]])
        check_box.append([agent_position[0] + 2, agent_position[1]])
        check_box.append([agent_position[0], agent_position[1] - 2])
        check_box.append([agent_position[0], agent_position[1] + 2])
    if [treasure_position[0], treasure_position[1]] in check_box:
        result_scan = "Phát hiện kho báu"
        print("********BẠN ĐÃ THẮNG*********")
    else:
        result_scan = "Xung quanh không có kho báu"
    return result_scan




def treasure_island(path_board, output_name):
    running = True
    flag_win = -1
    # Tải file txt
    w, h, turn_pirate_reveals, turn_pirate_free, num_regions, treasure_position, board = get_data(path_board)
    # Vị trí tên cướp biển
    pirate_position = find_pirate_position(board)
    # Tải bản đồ có agent
    board, agent_position = add_agent_position(board)
    # Đường đi của tên cướp từ nhà tù tới kho báu
    path_pirate_go = np.asarray(bfs(board, pirate_position, [treasure_position[0], treasure_position[1]]))
    path_pirate_go = path_pirate_go.tolist()
    print("**********Chào mừng bạn đến với Treasure Island**************")
    print(f"Kích thước bản đồ là {int(h)}x{int(w)}, thứ tự các ô được đánh từ 0 tới {int(h) - 1}")
    print(
        f"Vị trí bạn được sinh ra là: hàng {agent_position[0]}, cột {agent_position[1]}: {board[agent_position[0]][agent_position[1]]}")
    print(np.array(board))
    num_turn = 0
    truth_recommnet = []
    liar_recomment = []
    while running:
        if num_turn == 0:
            print("Gợi ý:")
            recomment, flag = hint_1(board)
            truth_recommnet.append(recomment)
            print(recomment)
        elif num_turn > 0 and num_turn < turn_pirate_reveals:
            print("Gợi ý:")
            recomment, flag = choice_hint(w, h, pirate_position, agent_position, num_regions, treasure_position, board)
            print(recomment)
        elif num_turn == turn_pirate_reveals:
            print(
                f"Nhà tù mà tên cướp biển đang ở là: hàng {pirate_position[0]}, cột {pirate_position[1]}: {board[pirate_position[0]][pirate_position[1]]}")
            print("Gợi ý:")
            recomment, flag = choice_hint(w, h, pirate_position, agent_position, num_regions, treasure_position, board)
            print(recomment)
        elif num_turn > turn_pirate_reveals and num_turn < turn_pirate_free:
            print("Gợi ý:")
            recomment, flag = choice_hint(w, h, pirate_position, agent_position, num_regions, treasure_position, board)
            print(recomment)
        else:
            board[pirate_position[0]][pirate_position[1]] = board[pirate_position[0]][pirate_position[1]][0] + 'p'
            if num_turn == turn_pirate_free:
                print("Tên tù nhân đã thoát và đang di chuyển tới kho báu")
            for i in range(0, 1):
                if len(path_pirate_go) == 1:
                    print("Tên cướp đã đến")
                    break
                target_move = path_pirate_go[1]
                if target_move[0] > pirate_position[0]:
                    board = move_down(board, pirate_position)
                elif target_move[0] < pirate_position[0]:
                    board = move_up(board, pirate_position)
                elif target_move[1] < pirate_position[1]:
                    board = move_left(board, pirate_position)
                elif target_move[1] > pirate_position[1]:
                    board = move_right(board, pirate_position)
                print(np.array(board))
                pirate_position = target_move
                path_pirate_go.remove(target_move)
            if len(path_pirate_go) == 1:
                print("$$$$$$$$$$ BẠN ĐÃ THUA $$$$$$$$$")
                flag_win = 0
                list_recomment = truth_recommnet + liar_recomment
                num_lines = len(list_recomment)
                with open(output_name, "w", encoding='utf8') as txt_file:
                    txt_file.write(str(num_lines))
                    txt_file.write(("\n"))
                    txt_file.write("LOSE")
                    txt_file.write(("\n"))
                    for recomment in list_recomment:
                        txt_file.write(str(recomment) + "\n")

                running = False
                break
            print("Gợi ý:")
            recomment, flag = choice_hint(w, h, pirate_position, agent_position, num_regions, treasure_position, board)
            print(recomment)
        ## Cướp biển xong ====================
        print("\n")
        print("\n")
        print("____________Vui lòng chọn hành động của bạn____________")
        while True:
            action = input(
                "Xác minh thông tin (1), Di chuyển ngắn & Scan (2), Di chuển dài (3), Đứng yên và Scan rộng (4): ")
            if action.lower() == 'q':
                running = False
                break
            try:
                action_indx = int(action)
            except:
                print("Vui lòng nhập lại lựa chọn của bạn!")
                continue
            if action_indx not in [1, 2, 3, 4]:
                print("Vui lòng nhập lại lựa chọn của bạn!")
                continue
            else:
                break
        print("\n")
        print("++++++Danh sách gợi ý đúng+++++++")
        print('\n'.join(truth_recommnet))
        print("++++++++++++++++++++++++++++++++++")
        print("------Danh sách gợi ý sai---------")
        print('\n'.join(liar_recomment))
        print("-----------------------------------")
        if action_indx == 1:
            print(f"{recomment} là {flag}")
            if flag == "Đúng":
                truth_recommnet.append(recomment)
            else:
                liar_recomment.append(recomment)
        elif action_indx == 2:
            print("Chọn hướng di chuyển")
            while True:
                direct_move = input("Lên (w), xuống (s), trái (a), phải (d): ")
                if direct_move.lower() == 'q':
                    running = False
                    break
                if direct_move.lower() in ['w', 's', 'a', 'd']:
                    break
                else:
                    print("Vui lòng nhập lại lựa chọn của bạn!")
                    continue
            direct_move = direct_move.lower()
            if direct_move == 'w':
                board = move_up(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0] - 1, agent_position[1]]
            elif direct_move == 's':
                board = move_down(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0] + 1, agent_position[1]]
            elif direct_move == 'a':
                board = move_left(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0], agent_position[1] - 1]
            elif direct_move == 'd':
                board = move_right(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0], agent_position[1] + 1]
            print(np.array(board))
            result_scan = agent_action_scan(treasure_position, agent_position, 1)
            print(result_scan)
            if result_scan == "Phát hiện kho báu":
                flag_win = 1
                list_recomment = truth_recommnet + liar_recomment
                num_lines = len(list_recomment)
                with open(output_name, "w", encoding='utf8') as txt_file:
                    txt_file.write(str(num_lines))
                    txt_file.write(("\n"))
                    txt_file.write("WIN")
                    txt_file.write(("\n"))
                    for recomment in list_recomment:
                        txt_file.write(str(recomment) + "\n")
                running = False
        elif action_indx == 3:
            print("Chọn hướng di chuyển")
            while True:
                direct_move = input("Lên (w), xuống (s), trái (a), phải (d): ")
                if direct_move.lower() == 'q':
                    running = False
                    break
                if direct_move.lower() in ['w', 's', 'a', 'd']:
                    break
                else:
                    print("Vui lòng nhập lại lựa chọn của bạn!")
                    continue
            direct_move = direct_move.lower()
            if direct_move == 'w':
                board = move_up(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0] - 1, agent_position[1]]
                board = move_up(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0] - 1, agent_position[1]]
            elif direct_move == 's':
                board = move_down(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0] + 1, agent_position[1]]
                board = move_down(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0] + 1, agent_position[1]]
            elif direct_move == 'a':
                board = move_left(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0], agent_position[1] - 1]
                board = move_left(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0], agent_position[1] - 1]
            elif direct_move == 'd':
                board = move_right(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0], agent_position[1] + 1]
                board = move_right(board, [agent_position[0], agent_position[1]])
                agent_position = [agent_position[0], agent_position[1] + 1]
            print(np.array(board))
        elif action_indx == 4:
            result_scan = agent_action_scan(treasure_position, agent_position, 2)
            print(result_scan)
            if result_scan == "Phát hiện kho báu":
                flag_win = 1
                list_recomment = truth_recommnet + liar_recomment
                num_lines = len(list_recomment)
                with open(output_name, "w", encoding='utf8') as txt_file:
                    txt_file.write(str(num_lines))
                    txt_file.write(("\n"))
                    txt_file.write("WIN")
                    txt_file.write(("\n"))
                    for recomment in list_recomment:
                        txt_file.write(str(recomment) + "\n")
                running = False
        num_turn += 1



if __name__ == '__main__':
    # Config link khai báo bản đồ
    path_board = 'map/MAP1.txt'
    path_log = 'log/LOG1.txt'
    treasure_island(path_board, path_log)
