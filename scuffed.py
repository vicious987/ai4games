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
gameboard = Tboard()

while True:
    print(f"start of turn", file=sys.stderr)
    enemy_row, enemy_col = [int(i) for i in input().split()]
    print(f"enemy move: {enemy_row} - {enemy_col}", file=sys.stderr)
    if (enemy_row, enemy_col) != (-1,-1):
        gameboard.make_move(enemy_row, enemy_col, ENEMY)
    valid_action_count = int(input())
    printf(f"no of possible moves :{valid_action_count", file=sys.stderr)
    possible_moves = []
    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]
        possible_moves.append((row,col))
    printf(f"possible moves:\n", file=sys.stderr)
    printf(possible_moves, file=sys.stderr)
    winning_moves = [x for x in possible_moves if gameboard.is_move_winning(x[0],x[1],ME)]
    printf(f"winning moves:\n", file=sys.stderr)
    printf(winning_moves, file=sys.stderr)
    blocking_moves = [x for x in possible_moves if gameboard.is_move_winning(x[0],x[1],ENEMY)]
    printf(f"blocking moves:\n", file=sys.stderr)
    printf(blocking_moves, file=sys.stderr)
    if winning_moves:
        move = choice(winning_moves)
    elif blocking_moves:
        move = choice(blocking_moves)
    else:
        move = choice(possible_moves)
    gameboard.make_move(move[0], move[1], ME)
    print(f"{move[0]} {move[1]}")
    print(f"end of turn", file=sys.stderr)
