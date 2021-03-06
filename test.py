#!/usr/bin/env python3

# pylint: disable=missing-docstring
# pylint: disable=too-many-instance-attributes
# pylint: disable=invalid-name,locally-disabled
import math

team_size = int(input())
ghost_count = int(input())
me = int(input())

enemy = 1 if me == 0 else 0
ghost = -1

if me == 0:
    my_team_ids = range(0, team_size)
else:
    my_team_ids = range(team_size, 2*team_size)

    #places
sfd = 5 #safety distance
if me == 0:
    my_base, enemy_base = (0+sfd, 0+sfd), (16000-sfd, 9000-sfd)
else:
    my_base, enemy_base = (16000-sfd, 9000-sfd), (0+sfd, 0+sfd)

shortwall_dest = (3500, 7500) if me == 0 else (12000, 2000)
longwall_dest = (10000, 3000) if me == 0 else (5000, 6000)
center = (8000, 4500)


#knowledge base
ghost_dict = {}
enemy_dict = {}
friend_dict = {}

#scouting stuff
scouting_phase_turns = 10
mx = 16000
my = 9000
x_sc = 16000 / (team_size + 1)
y_sc = 9000 / (team_size + 1)

scouting_dest_list = [(int(x_sc * i), int(9000- y_sc * i)) for i in range(1, team_size + 1)]

def scout_pos(destination):
    return f"MOVE {destination[0]} {destination[1]}"

#misc
def distance(pos_1, pos_2):
    return int(math.sqrt(pow(pos_1[0] - pos_2[0], 2) + pow(pos_2[0] - pos_2[1], 2)))

def line(x1, y1, x2, y2):
    a = (y2 - y1)/(x2 - x1)
    return (a, y1 - a)

def below_line(x, y, a, b):
    return (a * x + -1 * y + b) < 0

class Agent_normal:

    def __init__(self, init_e_id, init_team):
        self.e_id, self.team = init_e_id, init_team

        self.target = 0
        self.position = self.destination = self.target_pos = (-1, -1)
        self.carrying = self.home_reached = False

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

    def avaible_targets(self):
        return [(e_id, x["position"], x["score"]) for e_id, x in ghost_dict.items() if not x["targeted"]]

    def choose_new_target(self):
        nt = min(self.avaible_targets(), key=lambda x: x[2])
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


#busters init
buster_team = {}
for j in my_team_ids:
    buster_team[j] = Agent_normal(j, me)



def update_knowledge_base():
    entities = int(input())
    for _ in range(entities):
        e_id, x, y, e_type, state, value = [int(j) for j in input().split()]

        if e_type == ghost:
            if e_id in ghost_dict:
                ghost_dict[e_id]["position"] = (x, y)
                ghost_dict[e_id]["score"] = distance(center, (x, y))
            else:
                ghost_dict[e_id] = {"position": (x, y), "score" : distance(center, (x, y)), "targeted" : False}
        elif e_type == enemy:
            enemy_dict[e_id] = {"pos" : (x, y), "is_carrying" : state, "ghost_carried" : value}
        else:
            friend_dict[e_id] = {"pos" : (x, y), "is_carrying" : state, "ghost_carried" : value}

def update_buster_position():
    for buster_id, buster_pos in friend_dict.items():
        buster_team[buster_id].update_position(buster_pos)

while True:
    update_knowledge_base()
    update_buster_position()
    if scouting_phase_turns:
        for scout_dest in scouting_dest_list:
            print(scout_pos(scout_dest))
        scouting_phase_turns -= 1
    else:
        for current_buster in my_team_ids:
            print(buster_team[current_buster].gameloop())



#'''
