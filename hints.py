from random import randint
import numpy as np

from find_shortest_path import bfs


# hint 1: A list of random tiles that doesn't contain the treasure (1 to 12) => always true
def hint_1(board):
    num_random = randint(1, 12)
    recomment = []
    flag = 'Đúng'
    while True:
        i = randint(0, len(board) - 1)
        j = randint(0, len(board) - 1)
        if board[i][j][1] != 'P' and board[i][j][1] != 'M' and board[i][j] != '0 ':
            if [i, j] not in recomment:
                recomment.append([i, j])
            if len(recomment) == num_random:
                break
    recomment = f"(Đúng) Danh sách {num_random} ô không chứa kho báu là: {recomment} "
    return recomment, flag


# 2-5 regions that 1 of them has the treasure
def hint_2(board, num_regions, treasure_position):
    num_random = randint(2, 5)
    recomment = []
    while True:
        rad = randint(1, num_regions)
        if rad not in recomment:
            recomment.append(rad)
        if len(recomment) == num_random:
            break
    # check
    treasure_position = np.array(treasure_position)
    true_regions = int(board[treasure_position[0]][treasure_position[1]][0])
    if true_regions in recomment:
        flag = 'Đúng'
    else:
        flag = 'Sai'
    recomment = f"(Kiểm tra) Các vùng có thể chứa kho báu là: {recomment}"
    return recomment, flag


# 3. 1-3 regions that do not contain the treasure
def hint_3(board, num_regions, treasure_position):
    num_random = randint(1, 3)
    recomment = []
    while True:
        rad = randint(1, num_regions)
        if rad not in recomment:
            recomment.append(rad)
        if len(recomment) == num_random:
            break
    # check
    treasure_position = np.array(treasure_position)
    true_regions = int(board[treasure_position[0]][treasure_position[1]])
    if true_regions not in recomment:
        flag = 'Đúng'
    else:
        flag = 'Sai'
    recomment = f"(Kiểm tra) Các vùng không chứa kho báu là: {recomment}"
    return recomment, flag


# 4. A large rectangle area that has the treasure.
def hint_4(w, h, treasure_position):
    size = 5
    recomment = []
    init_w = randint(0, int(w) - (size + 1))
    init_h = randint(0, int(h) - (size + 1))
    for i in range(init_w, init_w + size):
        for j in range(init_h, init_h + size):
            recomment.append([i, j])
    if [treasure_position[0], treasure_position[1]] in recomment:
        flag = 'Đúng'
    else:
        flag = 'Sai'
    recomment = f"(Kiểm tra) Hình chữ nhật có kho báu là: {recomment}"
    return recomment, flag


# 5.A small rectangle area that doesn't has the treasure
def hint_5(w, h, treasure_position):
    size = 3
    recomment = []
    init_w = randint(0, int(w) - (size + 1))
    init_h = randint(0, int(h) - (size + 1))
    for i in range(init_w, init_w + size):
        for j in range(init_h, init_h + size):
            recomment.append([i, j])
    if [treasure_position[0], treasure_position[1]] not in recomment:
        flag = 'Đúng'
    else:
        flag = 'Sai'
    recomment = f"(Kiểm tra) Hình chữ nhật không có kho báu là: {recomment}"
    return recomment, flag


# 6. He tells you that you are the nearest person to the treasure (between you and the prison he is staying).
def hint_6(board, treasure_position, pirate_position, current_position):
    recomment  = "(Kiểm tra) Bạn là người gần kho báu nhất"
    treasure_position = [treasure_position[0], treasure_position[1]]
    cur_2_treasure = bfs(board, current_position, treasure_position)
    pirate_2_treasure = bfs(board, pirate_position, treasure_position)

    if len(cur_2_treasure) < len(pirate_2_treasure):
        flag = 'Đúng'
    else:
        flag = 'Sai'
    return recomment, flag


# 7. A column and/or a row that contain the treasure (rare)
def hint_7(w, h, treasure_position):
    axis = randint(0, 1)
    if axis == 0:
        row = randint(0, int(h) - 1)
        recomment = f"(Kiểm tra) Hàng thứ {row + 1} chứa kho báu"
        if row == treasure_position[0]:
            flag = "Đúng"
        else:
            flag = "Sai"
    else:
        col = randint(0, int(w) - 1)
        recomment = f"(Kiểm tra) Cột thứ {col + 1} chứa kho báu"
        if col == treasure_position[1]:
            flag = "Đúng"
        else:
            flag = "Sai"
    return recomment, flag


# 8. A column and/or a row that do not contain the treasure.
def hint_8(w, h, treasure_position):
    axis = randint(0, 1)
    if axis == 0:
        row = randint(0, int(h) - 1)
        recomment = f"(Kiểm tra) Hàng thứ {row + 1} không chứa kho báu"
        if row != treasure_position[0]:
            flag = "Đúng"
        else:
            flag = "Sai"
    else:
        col = randint(0, int(w) - 1)
        recomment = f"(Kiểm tra) Cột thứ {col + 1} không chứa kho báu"
        if col != treasure_position[1]:
            flag = "Đúng"
        else:
            flag = "Sai"
    return recomment, flag


# 9. 2 regions that the treasure is somewhere in their boundary
def hint_9(board, num_regions, treasure_position, w):
    num_random = 2
    w = int(w)
    recomment = []
    all_boundary = []
    while True:
        rad = randint(1, num_regions)
        if rad not in recomment:
            recomment.append(rad)
        if len(recomment) == num_random:
            break
    for i in range(0, len(board)):
        for j in range(0, len(board[1])):
            if board[i][j][0] == recomment[0]:
                if i < (w - 1) and j < (w - 1):
                    if (board[i + 1][j][0] == recomment[1]):
                        all_boundary.append([i, j])
                        all_boundary.append([i + 1, j])
                    elif (board[i - 1][j][0] == recomment[1]):
                        all_boundary.append([i, j])
                        all_boundary.append([i - 1, j])
                    elif (board[i][j + 1][0] == recomment[1]):
                        all_boundary.append([i, j])
                        all_boundary.append([i, j + 1])
                    elif (board[i][j - 1][0] == recomment[1]):
                        all_boundary.append([i, j])
                        all_boundary.append([i, j - 1])
    if [treasure_position[0], treasure_position[1]] in all_boundary:
        flag = "Đúng"
    else:
        flag = "Sai"
    recomment = f"(Kiểm tra) Kho báu nằm ở trong vùng tiếp giáp ranh giới của 2 vùng: {recomment}"
    return recomment, flag

# 10. The treasure is somewhere in a boundary of 2 regions
def hint_10(board, num_regions, treasure_position, w):
    num_random = 2
    w = int(w)
    recomment = []
    all_boundary = []
    while True:
        rad = randint(1, num_regions)
        if rad not in recomment:
            recomment.append(rad)
        if len(recomment) == num_random:
            break
    for i in range(0, len(board)):
        for j in range(0, len(board[1])):
            for i in range(0, 2):
                if board[i][j][0] == recomment[i]:
                    if i < (w - 1) and j < (w - 1):
                        if (board[i + 1][j][0] != recomment[i]):
                            all_boundary.append([i, j])
                        elif (board[i - 1][j][0] != recomment[i]):
                            all_boundary.append([i, j])
                        elif (board[i][j + 1][0] != recomment[i]):
                            all_boundary.append([i, j])
                        elif (board[i][j - 1][0] != recomment[i]):
                            all_boundary.append([i, j])
    if [treasure_position[0], treasure_position[1]] in all_boundary:
        flag = "Đúng"
    else:
        flag = "Sai"
    recomment = f"(Kiểm tra) Kho báu nằm ở ranh giới của 2 vùng: {recomment}"
    return recomment, flag


# 11. The treasure is somewhere in an area bounded by 2-3 tiles from sea
def hint_11(board, treasure_position, w):
    w = int(w)
    recomment = []
    for i in range(0, len(board)):
        for j in range(0, len(board[1])):
            count = 0
            if (board[i][j][0] != '0'):
                if i < (w - 1) and j < (w - 1):
                    if (board[i + 1][j][0] == '0'):
                        count += 1
                    if (board[i - 1][j][0] == '0'):
                        count += 1
                    if (board[i][j + 1][0] == '0'):
                        count += 1
                    if (board[i][j - 1][0] == '0'):
                        count += 1
            if count == 2 or count == 3:
                recomment.append([i, j])
    if [treasure_position[0], treasure_position[1]] in recomment:
        flag = "Đúng"
    else:
        flag = "Sai"
    recomment = f"(Kiểm tra) Kho báu ở đâu đó trong khu vực được bao bọc bởi 2-3 ô từ biển: {recomment}"
    return recomment, flag

# 12. A half of the map without treasure
def hint_12(board, treasure_position,w, h):
    w = int(w)
    h = int(h)
    recomment = []
    half_inx = randint(0, 3)
    if half_inx == 0:
        cp_boad = board[:int(w/2)][:]
    elif half_inx == 1:
        cp_boad = board[:int(w/2)][:]
    elif half_inx == 2:
        cp_boad = board[:][:int(h/2)]
    elif half_inx == 3:
        cp_boad = board[:][int(h/2):]
    for i in range(0, len(cp_boad)):
        for j in range(0, len(cp_boad[1])):
            recomment.append([i, j])
    if [treasure_position[0], treasure_position[1]] not in recomment:
        flag = "Đúng"
    else:
        flag = "Sai"
    recomment = f"(Kiểm tra) Một nửa bản đồ không chứa kho báu là: {recomment}"
    return recomment, flag

# 13. From the center of the map/from the prison that he's staying, he tells you a direction that has the treasure
# (W, E, N, S or SE, SW, NE, NW) (The shape of area when the hints are either W, E, N or S is triangle) # Khó
def hint_13(pirate_position, treasure_position, agent_position):
    arr = ['W', 'E', 'N', 'S', 'SE', 'SW', 'NE', 'NW']
    indx = randint(0, 7)
    direction = arr[indx]
    recomment = f"(Kiểm tra) Từ cướp biển, hãy đi về phía {direction}"
    indx = randint(0,1)
    if indx == 0:
        flag = "Sai"
    else:
        flag = "Đúng"
    return recomment, flag


# 14. 2 squares that are different in size, the small one is placed inside the bigger one, the treasure is somewhere
# inside the gap between 2 squares
def hint_14(treasure_position, w):
    recomment = []
    small_size = randint(2, int(w) - 5)
    bigger_size = randint(small_size + 2, int(w))

    init_s = int((int(w) - small_size)/2)
    init_b = int((int(w) - bigger_size)/2)
    print(init_s)
    print(init_b)
    for i in range(init_b, init_s+1):
        for j in range(init_b, init_s+1):
            recomment.append([i, j])
    if [treasure_position[0], treasure_position[1]] in recomment:
        flag = "Đúng"
    else:
        flag = "Sai"
    recomment = f"(Kiểm tra) Kho báu nằm giữa 2 hình vuông, cụ thể: {recomment}"
    return recomment, flag


# 15. The treasure is in a region that has mountain
def hint_15(board, treasure_position):
    region_true = board[treasure_position[0], treasure_position[1]][0]
    flag = "Sai"
    for i in range(0, len(board)):
        for j in range(0, len(board[1])):
            if board[i][j][0] == region_true:
                if board[i][j][1] == 'M':
                    flag = "Đúng"
    recomment = "(Kiểm tra) Khu vực chứa kho báu có núi"
    return recomment, flag


## Tổng hợp
def choice_hint(w, h, pirate_position, agent_position, num_regions, treasure_position, board):
    rad_idx = randint(2, 15)
    # flag = "Sai"
    # recomment = ""
    if rad_idx == 2:
        recomment, flag = hint_2(board, num_regions, treasure_position)
    elif rad_idx == 3:
        recomment, flag = hint_3(board, num_regions, treasure_position)
    elif rad_idx == 4:
        recomment, flag = hint_4(w, h, treasure_position)
    elif rad_idx == 5:
        recomment, flag = hint_5(w, h, treasure_position)
    elif rad_idx == 6:
        recomment, flag = hint_6(board, treasure_position, pirate_position, agent_position)
    elif rad_idx == 7:
        recomment, flag = hint_7(w, h, treasure_position)
    elif rad_idx == 8:
        recomment, flag = hint_8(w, h, treasure_position)
    elif rad_idx == 9:
        recomment, flag = hint_9(board, num_regions, treasure_position, w)
    elif rad_idx == 10:
        recomment, flag = hint_10(board, num_regions, treasure_position, w)
    elif rad_idx == 11:
        recomment, flag = hint_11(board, treasure_position, w)
    elif rad_idx == 12:
        recomment, flag = hint_12(board, treasure_position,w, h)
    elif rad_idx == 13:
        recomment, flag = hint_13(pirate_position, treasure_position, agent_position)
    elif rad_idx == 14:
        recomment, flag = hint_14(treasure_position, w)
    elif rad_idx == 15:
        recomment, flag = hint_15(board, treasure_position)
    return recomment, flag
