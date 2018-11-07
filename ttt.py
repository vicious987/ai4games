
# pylint: disable=locally-disabled, multiple-statements, fixme, line-too-long, missing-docstring, trailing-whitespace, bad-whitespace, bad-continuation, pointless-string-statement, too-few-public-methods, invalid-name, no-self-use

import time
import math
from operator import itemgetter
from random import  choice

MAX_VALUE = 999
MIN_VALUE = -MAX_VALUE
WIN_SCORE = 10

PLAYER_1 = 1
PLAYER_2 = -1
ONGOING = 0
DRAW = 2

RESPONSE_TIME = 10
SAFETY_TIME = 1

def current_time():
    return int(round(time.time() * 1000))


class Tboard:

    def __init__(self):
        self.board = [ 
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]]
        self.status = ONGOING
        self.last_move = (-1, -1)

    def sum_of_rows(self):
        return [sum(row) for row in self.board]

    def sum_of_cols(self):
        return [sum(col) for col in zip(*self.board)]

    def sum_of_diag(self):
        return [self.board[0][0] + self.board[1][1] + self.board[2][2], 
                self.board[2][0] + self.board[1][1] + self.board[0][2]]

    def possible_moves_left(self):
        return [(ix, iy) for ix, row in enumerate(self.board) for iy, i in enumerate(row) if i == 0]

    def check_status(self):
        if not self.possible_moves_left() and self.status == ONGOING:
            self.status = DRAW
        else:
            for x in (3, -3):
                if (x in self.sum_of_rows()) or (x in self.sum_of_cols()) or (x in self.sum_of_diag()):
                    self.status = PLAYER_1 if x == 3 else PLAYER_2
        return self.status

    def make_move_on_board(self, position, player_id):
        self.last_move = position
        self.board[position[0]][position[1]] = player_id


class State:

    def __init__(self, b, pid):
        self.board = b
        self.player_id = pid
        self.visit_count = 0
        self.score = 0.0

    def add_score(self, sc):
        self.score += sc

    def incr_visit_count(self):
        self.visit_count += 1

    def make_move(self, pos):
        self.board.make_move_on_board(pos, self.player_id)


    def all_possible_states(self):
        aps = []
        for move in self.board.possible_moves_left():
            new_state = State(self.board, self.player_id)
            new_state.make_move(move)
            aps.append(new_state)
        return aps

    def random_play(self):
        pml = self.board.possible_moves_left()
        if pml:
            self.make_move(choice(pml))
            return True
        return False

    def switch_player(self):
        self.player_id *= -1

        



class Node:

    def __init__(self, st, pr):
        self.state = st
        self.parent = pr
        self.children = []

class Tree:

    def __init__(self, r):
        self.root = r

"""
def calc_uct_value(total_visit, node_score, node_visit):
    return (node_score / node_visit) + 1.41 * math.sqrt(math.log(total_visit) / node_visit) if node_visit == 0 else MAX_VALUE

def calc_uct_value():
    return 13
    """

def find_best_child(node):
    parent_visit = node.state.visit_count
    #return max(
    #        [(calc_utc_value(parent_visit, child.score, child.visit_count), child) 
    #            for child in node.children], key=itemgetter(0))[1]
    lst = [(child, calc_utc_value(parent_visit, child.score, child.visit_count)) for child in node.children]
    return max(lst, key=itemgetter(1))[0]

class MTCS:
    def __init__(self, pid):
        self.win_score = WIN_SCORE
        self.enemy_id = -pid

    #X
    #???
    def select_promising_node(self, root_node):
        node = root_node
        while node.children: #while list not empty
            node = find_best_child(node)
        return node
    
    #V
    #add nodes with all possible states to the given parent node 
    def expand_node(self, node):
        for st in node.state.get_all_possible_states():
            node.children.append(Node(st, node))
            

    #V
    #adds win_score to score to itself and every ancestor
    def back_propagation(self, node_to_explore, player_id):
        temp_node = node_to_explore
        while not temp_node is None:
            temp_node.state.incr_visit()
            if temp_node.state.player_id == player_id:
                temp_node.state.add_score(WIN_SCORE)
            temp_node = temp_node.parent

    def update_scores(self, node, player_id):
        if not node is None:
            node.state.incr_visit()
            if node.state.player_id == player_id:
                node.state.add_score(WIN_SCORE)
        self.update_scores(node.parent, player_id)

    #V
    #take a node, if its a losing state, set parent score as minimal
    #otherwise make a random play on a board
    def simulate_random_playout(self, node):
        temp_state, board_status, node_parent = node.state, node.board.status, node.parent
        if board_status == self.enemy_id:
            node_parent.state.score = MIN_VALUE
        elif board_status == ONGOING:
            temp_state.toggle_player()
            temp_state.random_play()
            board_status = temp_state.board.status
        return board_status

    #X
    def find_next_move(self, board, player_id):
        end_time = current_time() + RESPONSE_TIME - SAFETY_TIME
        enemy = -player_id
        tree = Tree()
        root_node = tree.root
        root_node.state.board, root_node.state.player_id = board, enemy

        while current_time() < end_time:
            #Select
            promising_node = self.select_promising_node(root_node)
            #Expand
            if promising_node.state.board.status == ONGOING:
                self.expand_node(promising_node)
            #Simulate
            node_to_explore = promising_node
            if promising_node.children:
                node_to_explore = choice(promising_node.children)
            playout_result = self.simulate_random_playout(node_to_explore)
            #Update
            self.back_propagation(node_to_explore, playout_result)

        winner_node = find_best_child(root_node)
        tree.root = winner_node
        return winner_node.state.board

# game loop
while True:
    opponent_row, opponent_col = [int(i) for i in input().split()]
    valid_action_count = int(input())
    for i in range(valid_action_count):
        row, col = [int(j) for j in input().split()]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    print("0 0")
