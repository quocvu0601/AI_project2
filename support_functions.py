def assign_matrix(board):
    '''return board as same as input board'''
    return [[board[x][y] for y in range(len(board[0]))] for x in range(len(board))]