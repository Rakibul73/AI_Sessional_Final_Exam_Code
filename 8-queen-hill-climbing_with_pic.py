import copy
import numpy as np
import chess
import sys
from chess import svg


def exists(i, j):
    # Checks if square exists within boundary

    return (i >= 0 and i < 8 and j >= 0 and j < 8)


def contains(i, j, l, m, queen_pairs):
    # Check if the two pair of queens have already been included in count

    if ((i, j, l, m) in queen_pairs) or ((l, m, i, j) in queen_pairs):
        return True
    return False


def save_board_as_png(fen):
    # Converts the FEN format notation to an SVG chess board

    board = chess.Board(fen)
    boardsvg = chess.svg.board(board=board)
    filetowriteto = open("output.SVG", "w")
    filetowriteto.write(boardsvg)
    filetowriteto.close()
    print("SVG File created successfully")


def create_board(board):
    # Creates a python-chess board for the matrix board

    chess_board = chess.Board()
    chess_board.clear()

    for i in range(8):
        for j in range(8):
            if board[i][j]:
                chess_board.set_piece_at(chess.square(
                    i, j), chess.Piece(5, chess.WHITE))

    return chess_board.fen()


def position_queens_row_wise(board):
    """Place a single queen on every row. If there are more than
    two quueens in one row, it places them on other rows"""

    for row in board:
        while row.count(1) > 1:
            # More than one 1s so distribute to other rows

            for i in range(8):
                if board[i].count(1) == 0:
                    j = row.index(1)
                    board[i][j] = 1
                    row[j] = 0
                    break

    return board


def heuristic_value(board):
    # Calculates the heuristic value h of the current state of board
    # Number of pairs of queens attacking each other directly or indirectly

    h = 0
    queen_pairs = []
    for i in range(8):
        for j in range(8):

            if board[i][j]:

                # Calculate horizontal attacks
                for k in range(8):
                    if board[i][k] == 1 and k != j and not contains(i, j, i, k, queen_pairs):
                        queen_pairs.append((i, j, i, k))
                        h += 1

                # Calculate vertical attacks
                for k in range(8):
                    if board[k][j] == 1 and i != k and not contains(i, j, k, j, queen_pairs):
                        queen_pairs.append((i, j, k, j))
                        h += 1

                # Calculate / diagonal attacks
                # First go up the diagonal
                l, m = i-1, j+1
                while exists(l, m):
                    if board[l][m] == 1 and not contains(i, j, l, m, queen_pairs):
                        queen_pairs.append((i, j, l, m))
                        h += 1
                    l, m = l-1, m+1

                # Now go down the diagonal
                l, m = i+1, j-1
                while exists(l, m):
                    if board[l][m] == 1 and not contains(i, j, l, m, queen_pairs):
                        queen_pairs.append((i, j, l, m))
                        h += 1
                    l, m = l+1, m-1

                # Calculate \ diagonal attacks
                # First go up the diagonal
                l, m = i-1, j-1
                while exists(l, m):
                    if board[l][m] == 1 and not contains(i, j, l, m, queen_pairs):
                        queen_pairs.append((i, j, l, m))
                        h += 1
                    l, m = l-1, m-1

                # Now go down the diagonal
                l, m = i+1, j+1
                while exists(l, m):
                    if board[l][m] == 1 and not contains(i, j, l, m, queen_pairs):
                        queen_pairs.append((i, j, l, m))
                        h += 1
                    l, m = l+1, m+1

    return h


def hill_climbing(board):
    # Find the least cost successor for the given board state

    min_board = board
    min_h = 999999
    global n_side_moves, n_steps

    n_steps += 1

    # Check if number of side moves has reached a limit
    if n_side_moves == 100:
        return -1

    sideway_move = False

    for i in range(8):
        # Find index of queen in current row
        queen = board[i].index(1)

        board[i][queen] = 0

        for k in range(8):
            # Place queen at different positions and calculate new score

            if k != queen:
                board[i][k] = 1

                h = heuristic_value(board)

                if h < min_h:
                    min_h = h
                    min_board = copy.deepcopy(board)
                if h == min_h:
                    min_h = h
                    min_board = copy.deepcopy(board)
                    sideway_move = True

                board[i][k] = 0

        board[i][queen] = 1

    if sideway_move:
        n_side_moves += 1

    if min_h == 0:
        print("Number of steps required: {}".format(n_steps))
        return min_board

    return hill_climbing(min_board)


if __name__ == "__main__":
    # 8x8 chess board
    board = []
    n_side_moves = 0
    n_steps = 0

    for i in range(8):
        row = list(map(int, input().split()))
        board.append(row)

    print("Current position's heuristic value: ", heuristic_value(board))

    board = position_queens_row_wise(board)
    min_board = hill_climbing(board)

    if min_board != -1:
        fen = create_board(min_board)
        save_board_as_png(fen)
    else:
        print("Could not solve")


'''
paste this in input 

1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0
0 0 0 0 0 0 0 0
0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 1
0 0 0 0 0 1 0 0
1 0 0 0 0 0 0 1
0 0 0 0 0 0 0 0



'''