import sys
import math

class Status(Enum):
    ongoing = 0
    done = 1
    draw = 2

class Tboard:

    __init__(self):
        self.board = [ 
                [0,0,0],
                [0,0,0],
                [0,0,0]]
        self.game_status = Status.ongoing 
        self.winner = 0

    def check_win_rows(self):
        r = [sum(row) for row in self.board]
        if 3 in r:
            return 1 
        elif -3 in r:
            return -1
        else:
            return 0

    def check_win_cols(self):
        r = [sum(col) for col in zip(*self.board)]
        if 3 in r:
            return 1
        elif -3 in r:
            return -1
        else:
            return 0

    def check_diag(self):
        r = [   self.board[0][0] + self.board[1][1] + self.board [2][2], 
                self.board[2][0] + self.board[1][1] + self.board[0][2]]
        if 3 in r:
            return 1
        elif -3 in r:
            return -1
        else:
            return 0

    def check_win(self):
        if self.check_win_rows() != 0:
            winner = self.check_win_rows()
            self.status = Status.done
        elif self.check_win_cols() != 0:
            winner = self.check_win_cols()
            self.status = Status.done
        else self.check_win_diag() != 0:
            winner = self.check_win_diag()
            self.status = Status.done
        return winner

    def make_move_on_board(self, row, col, player_id):
        board[row][col] = played_id


class State:

    __init__(b, pid):
        self.board = b
        self.player_id = pid
        self.visit_count = 0
        self.score = 0.0

    def incr_visit_count(self):
        self.visit_count += 1

    def make_move(self, row, col):
        board.make_move_on_board(row, col, self.played_id)

class Node:

    __init__(self, st, pr):
        self.state = st
        self.parent = pr
        self.children = []

class Tree:

    __init__(self, r):
        self.root = r



# game loop
while True:
    opponent_row, opponent_col = [int(i) for i in raw_input().split()]
    valid_action_count = int(raw_input())
    for i in xrange(valid_action_count):
        row, col = [int(j) for j in raw_input().split()]

    # Write an action using print
    # To debug: print >> sys.stderr, "Debug messages..."

    print "0 0"
