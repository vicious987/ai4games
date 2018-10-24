#!/usr/bin/env python3

# pylint: disable=missing-docstring
import sys
import math

team_size= int(input())
ghost_count = int(input())
me = int(input())

enemy = 1 if me == 0 else 0
ghost = -1

if me == 0:
    my_team_ids = range(0, team_size)
else:
    my_team_ids = range(team_size, 2*team_size)

    #places
if me == 0:
    my_base, enemy_base = (0,0), (16000, 9000)
else:
    my_base, enemy_base = (16000, 9000), (0,0)

shortwall_dest = (3500, 7500) if me == 0 else (12000, 2000)
longwall_dest = (10000, 3000) if me == 0 else (5000, 6000)
center = (8000, 4500)

#knowledge base
ghost_dict = {}
enemy_dict = {}
friend_dict = {}

#scouting stuff
x_sc = 16000 / (team_size + 1)
y_sc = 9000 / (team_size + 1)
scouting_dest = [(int(x_sc * i), int(y_sc * i)) for i in range(1, team_size + 1)]

def scout_pos(pos):
    return f"MOVE {pos[0]} {pos[1]}"


def distance (pos_1, pos_2):
    return int(math.sqrt(pow(pos_1[0] - pos_2[0], 2) + pow(pos_2[0] - pos_2[1], 2)))

def line (x1, y1, x2, y2):
    a =  (y2 - y1)/(x2 - x1)
    return (a, y1 - a) 

def below_line (x, y, a, b):
    return (a * x + -1 * y + b) < 0

'''
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

'''

class Agent_normal:

    def __init__(self, init_e_id, init_team):
        self.e_id = init_e_id
        self.position = (-1,-1)
        self.team = init_team
        self.carrying = False
        self.target = 0
        self.target_pos = (-1,-1)


    def move_to(self, destination):
        return f"MOVE {destination[0]} {destination[1]}"

    def bust_ghost(self, g_id):
        self.carrying = True
        return f"BUST {g_id}"

    def release_ghost(self):
        self.carrying = False
        self.target = 0
        return f"RELEASE" 

    def bustable(self, buster_pos, ghost_pos):
        return 900 < distance(buster_pos, ghost_pos) < 1760 

#fix for home
    def update_position(self, newpos):
        self.position = newpos
        self.home_reached = True if self.position == my_base else False
        self.dest_reached = True if self.position == destination else False

    def avaible_targets(self):
        return [(e_id, x["position"], x["score"]) for e_id, x in gd.items() if not x["targeted"]]

    def choose_new_target(self):
        nt = min(avaible_targets, key=lambda x:x[2])
        ghost_dict[nt[0]]["targeted"] = True
        return nt

    def set_destination(self, new_dest):
        self.destination = new_dest

    def gather_ghost(self, ghost_id, ghost_pos):
        if self.carrying:
            if self.home_reached:
                return self.release_ghost()
            else:
                self.move_to(my_base)
        elif self.bustable(self.position, ghost_pos):
            self.bust_ghost(ghost_id)
        else:
            self.move_to(ghost_pos)


    def gameloop(self):
        if self.target:
            self.gather_ghost(self.target, self.target_pos)
        elif any(self.avaible_targets()):
            self.target = self.choose_new_target()
        #else:
            #explore()




buster_team = {} 
for x in my_team_ids:
    buster_team[x] = Agent_normal(x, me)
    
 
def update_knowledge_base():
    entities = int(input())
    for i in range(entities):
        e_id, x, y, e_type, state, value = [int(j) for j in input().split()]

        if e_type == ghost:
            if e_id in ghost_dict:
                ghost_dict[e_id]["position"] = (x, y)
                ghost_dict[e_id]["score"] = distance(center, (x, y))
            else:
                ghost_dict[e_id] = {"position": (x, y), "score" : distance(center, (x, y)), "targeted" : False}
        elif e_type ==  enemy:
            enemy_dict[e_id] = {"pos" : (x, y), "is_carrying" : state, "ghost_carried" : value}
        else:
            friend_dict[e_id] = {"pos" : (x, y), "is_carrying" : state, "ghost_carried" : value}

def update_buster_position():
    for buster_id, buster_pos in friend_dict.items():
        buster_team[buster_id].update_position(buster_pos)
        

while True:
    update_knowledge_base()
    update_buster_position()
    while(scouting_phase):
        for current_buster in my_team_ids:

    for current_buster in my_team_ids:
        print(buster_team[current_buster].gameplay_loop())



#'''
