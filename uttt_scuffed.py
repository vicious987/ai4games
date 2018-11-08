import sys
from random import choice

#pylint: disable=bad-whitespace, missing-docstring, invalid-name, bad-continuation, trailing-whitespace

class Tboard:
    def __init__(self):
        self.board = [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        self.edges = [(0,1), (1,0),(1,2),(2,1)]

    def is_move_winning(self, move_row, move_col, player):
        win_score = player * 3
        temp_board = self.board
        temp_board[move_row][move_col] = player
        row_sum = sum(temp_board[move_row])
        col_sum = sum([x[move_col] for x in temp_board])
        diag1_sum = sum([temp_board[0+i][0+i] for i in range(3)])
        diag2_sum = sum([temp_board[2-i][0+i] for i in range(3)])
        return win_score in [row_sum, col_sum, diag1_sum, diag2_sum]

    def make_move(self, r, c, player):
        self.board[r][c] = player



# game loop
ME = 1
ENEMY = -1
row1 = row2 = row3 = []
for x in range(3):
    row1.append(Tboard())
    row2.append(Tboard())
    row3.append(Tboard())
big_board = [row1, row2, row3]
current_small_board = big_board[1][1]

while True:
    current_board = big_board[1][1]
    #print(f"start of turn", file=sys.stderr)
    enemy_row, enemy_col = [int(i) for i in input().split()]
    #print(f"enemy move: {enemy_row} - {enemy_col}", file=sys.stderr)
    if (enemy_row, enemy_col) != (-1,-1):
        board_row, board_col = enemy_row // 3, enemy_col // 3
        enemy_move_row, enemy_move_col = enemy_row % 3, enemy_col % 3
        big_board[board_row][board_col].make_move(enemy_move_row, enemy_move_col, ENEMY)
    valid_action_count = int(input())
    #print(f"no of possible moves :{valid_action_count}", file=sys.stderr)
    possible_moves = []
    for i in range(valid_action_count):
        my_row, my_col = [int(j) for j in input().split()]
        board_row, board_col = my_row // 3, my_col // 3
        my_move_row, my_move_col = my_row % 3, my_col % 3
        possible_moves.append((board_row, board_col, my_move_row, my_move_col))
        #possible_moves.append({'board_row': board_row, 'board_col': board_col, 'my_move_row' : my_move_row, 'my_move_col' : my_move_col})
    #print(f"possible moves:\n", file=sys.stderr)
    #print(possible_moves, file=sys.stderr)
    winning_moves = [x for x in possible_moves if big_board[x[0]][x[1]].is_move_winning(x[2],x[3],ME)]
    #print(f"winning moves:\n", file=sys.stderr)
    #print(winning_moves, file=sys.stderr)
    blocking_moves = [x for x in possible_moves if big_board[x[0]][x[1]].is_move_winning(x[2],x[3],ENEMY)]
    #print(f"blocking moves:\n", file=sys.stderr)
    #print(blocking_moves, file=sys.stderr)
    if winning_moves:
        move = choice(winning_moves)
    elif blocking_moves:
        move = choice(blocking_moves)
    else:
        move = choice(possible_moves)
    big_board[move[0]][move[1]].make_move(move[2],move[3], ME)
    cc_move_row, cc_move_col = move[0] * 3 + move[2], move[1] * 3 + move[3]
    print(f"{cc_move_row} {cc_move_col}")
    #print(f"end of turn", file=sys.stderr)
