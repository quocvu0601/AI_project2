import collections
import numpy as np


def bfs(board, start, goal):
    h, w = np.array(board).shape
    queue = collections.deque([[start]])
    seen = set(start)
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if [x, y] == goal:
            return path
        for x2, y2 in ((x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)):
            if 0 <= x2 < w and 0 <= y2 < h and board[y2][x2][1] != 'P' and board[y2][x2][1] != 'M' and board[y2][
                x2] != '0 ' and (x2, y2) not in seen:
                queue.append(path + [(x2, y2)])
                seen.add((x2, y2))
