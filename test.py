#!/usr/bin/env python3
import sys
import math

team_size= int(input())
ghost_count = int(input())
me = int(input())

enemy = 1 if me == 0 else 0
ghost = -1

if me == 0:
    my_base, enemy_base = (0,0), (16000, 9000)
else:
    my_base, enemy_base = (16000, 9000), (0,0)

shortwall_dest = (3500, 7500) if me == 0 else (12000, 2000)
longwall_dest = (10000, 3000) if me == 0 else (5000, 6000)

ghost_dict = defaultdict(lambda: (-1, -1, -1))
enemy_dict = defaultdict(lambda: (-1, -1, -1, -1))
friend_dict = defaultdict(lambda: (-1, -1, -1, -1))

#def distance (x1, y1, x2, y2):
#    return int(math.sqrt(pow(x1 - x2,2)+ pow(y1 - y2,2)))

def distance (pos_1, pos_2):
    return int(math.sqrt(pow(pos_1[0] - pos_2[0], 2) + pow(pos_2[0] - pos_2[1], 2)))

def line (x1, y1, x2, y2):
    a =  (y2 - y1)/(x2 - x1)
    return (a, y1 - a) 

def belowline (x, y, a, b):
    return (a * x + -1 * y + b) < 0

def move_to_home():
    return f"MOVE {my_base[0]} {my_base[1]}" 

def move_to(destination):
    return f"MOVE {destination[0]} {destination[1]}"

def bust_ghost(g_id):
    return f"BUST {g_id}"

def release_ghost():
    return f"RELASE" 

def bustable(buster_pos, ghost_pos):
    if distance(buster_pos[0], buster_pos[1], 
class Agent_shepherd:

    def __init__(self, init_e_id, init_dest_x, init_dest_y, init_pos_x, init_pos_y,init_team):
        self.e_id = init_e_id
        self.target_queue = []
        self.destination = (init_dest_x, init_dest_y)
        self.dest_reached = False
        self.wall_reached = False
        self.base_reached = False
        self.position = (init_pos_x, init_pos_y)
        self.team = init_team
        #self.base_pos = (0,0) if self.team == 0 else (16000,9000)
        #self.wall_pos = (0, init_dest_y) if self.team == 0 else (16000, init_dest_y)

    def update_position(x, y):
        self.position = (x, y)
        dest_reached = True if self.position == destination
        wall_reached = True if self.position == wall_pos and dest_reached
        base_reached = True if self.position == my_base and dest_reached and wall_reached

    def gameloop_str(self):
        if self.dest_reached:
            if wall_reached:
                return move_to(my_base)
            else:
                return move_to(wall)
        elif not self.target_queue: #move along the path
            move_to(destination)      
        #else:
            #push the target

class Agent_normal:

    def __init__(self, init_e_id, init_dest_x, init_dest_y, init_pos_x, init_pos_y,init_team):
        self.e_id = init_e_id
        self.destination = (init_dest_x, init_dest_y)
        self.dest_reached = False
        self.base_reached = False
        self.gather_done = False
        self.position = (init_pos_x, init_pos_y)
        self.team = init_team
        #self.base_pos = (0,0) if self.team == 0 else (16000,9000)

    def update_position(self, x, y):
        self.position = (x, y)
        self.home_reached = True if self.position == my_base else False
        self.dest_reached = True if self.position == destination else False

    def set_destination(self, new_dest):
        self.destination = new_dest

    def gather_ghost(self, ghost_id, ghost_pos):
        if carrying:
            if not home_reached:
                return release_ghost()
            else:
                move_to(my_base)
        elif within_bustin_range(ghost pos):
            bust_ghost(ghost_id)
        else:
            move_to(ghost_pos)


    def gameloop(self):
        #if not targeted,
            #if possible target a ghost
            #else explore
        #else
            #if ghost not reached
                #go to ghost
            #else (ghost reached)
                #and not busted
                    #bust him
                #(busted)
                    #if not at home
                        #go go to home




#'''



shepherd = Agent_shepherd(0
# game loop
while True:
    entities = int(input())  # the number of busters and ghosts visible to you
    for i in range(entities):
        # entity_id: buster id or ghost id
        # y: position of this buster / ghost
        # entity_type: the team id if it is a buster, -1 if it is a ghost.
        # state: For busters: 0=idle, 1=carrying a ghost.
        # value: For busters: Ghost id being carried. For ghosts: number of busters attempting to trap this ghost.
        e_id, x, y, e_type, is_carrying, value = [int(j) for j in input().split()]
        ## write down the knowledge
        if e_type == ghost:
            ghost_dict[e_id] = (x, y, value))
        elif e_type ==  enemy:
            enemy_dict[e_id] = (x, y, is_carrying, value)
        elif e_type == me:
            friend_dict[e_id] = (x, y, is_carrying, value)
    for i in range(team_size):

        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr)

        # MOVE x y | BUST id | RELEASE
        print("MOVE 8000 4500")

#'''
