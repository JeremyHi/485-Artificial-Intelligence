# pylint: disable=C0321,C0103,C0111,C0301,R0902,I1101

import time
import json
from Queue import Queue
import numpy

# Agent constants
MOVE_DIRS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}
MOVE_DIRS_ADJUSTED = {"U": (0, 1), "D": (0, -1), "L": (1, 0), "R": (-1, 0)}

class MazeAgent:

    def __init__(self, env):
        self.env = env
        self.malmo = env.malmo
        self.loc = env.playerPos
        self.facing = (0, 1)
        self.maze = env.agMaze
        self.plan = Queue()

        self.maze_width = len(self.maze[0])
        self.maze_height = len(self.maze)

        self.start = self.loc
        self.goals = []

        for row in list(enumerate(self.maze)):
            for column in list(enumerate(row[1])):
                state = (column[0]+2, row[0]-2)
                if column[1] == "G":
                    self.goals.append((self.maze_height - state[0], self.maze_width + state[1]))

        self.lava = []
        self.safe = [self.start]
        self.warning = []
        self.visited = []

    def think(self, perception):
        current_location = (self.loc[0], self.loc[1])

        moves = self.available_moves(current_location)
        next_move = []
        for move in moves:
            adjusted_move = (current_location[0] + MOVE_DIRS_ADJUSTED[move][0],
                             current_location[1] + MOVE_DIRS_ADJUSTED[move][1])
            move_weight = 3 if adjusted_move in self.warning else 1

            if adjusted_move not in self.visited:
                next_move.append(move_weight + self.manhattan_distance(adjusted_move, self.goals))

        next_move = moves[next_move.index(min(next_move))]

        self.plan.put(next_move)
        self.loc = (self.loc[0] + MOVE_DIRS_ADJUSTED[next_move][0], self.loc[1] + MOVE_DIRS_ADJUSTED[next_move][1])
        print((self.loc, next_move))

        self.visited.append(current_location)

    def act(self):
        current_location = (self.loc[0], self.loc[1])
        # BlindBot perceives what it is standing on...
        perception = self.perceive()
        print(str(current_location) + ": " + perception)
        if perception == 'obsidian':
            current_location = (self.loc[0], self.loc[1])
            self.warning.append(current_location)

        # ...BlindBot thinks...
        self.think(perception)

        # ...and then moves according to its plan, if it has one
        if self.plan.empty():
            return
        self.move(self.plan.get())
        return

    # [!] TODO: Any record-keeping when bot dies
    def die(self):
        # add the current location (lava) to unsafe space
        current_location = (self.loc[0], self.loc[1])
        self.lava.append(current_location)
        # we know that all four spots around are obsidian/barrier aka not visitable
        self.warning.extend(((current_location[0]-1, current_location[1]),
                             (current_location[0]+1, current_location[1]),
                             (current_location[0], current_location[1]+1),
                             (current_location[0], current_location[1]-1)))
        print(self.warning)
        # Reset player position back to start
        self.loc = self.env.playerPos

    def manhattan_distance(self, start, end):
        ret = []
        for goal in end:
            sx, sy = start
            ex, ey = goal
            ret.append(abs(ex - sx) + abs(ey - sy))
        return min(ret)

    def available_moves(self, current_location):
        moves = []

        if current_location[1]+1 < self.maze_height-1 and (current_location[0], current_location[1]+1) not in self.visited:
            moves.append("U")
        if current_location[0]-1 > 0 and (current_location[0]-1, current_location[1]) not in self.visited:
            moves.append("R")
        if current_location[1]-1 > 0 and (current_location[0], current_location[1]-1) not in self.visited:
            moves.append("D")
        if current_location[0]+1 < self.maze_width-1 and (current_location[0]+1, current_location[1]) not in self.visited:
            moves.append("L")

        return moves


    # -----------------------------------------------------------------------
    # YOU MAY NOT MODIFY ANYTHING BELOW THIS LINE
    # -----------------------------------------------------------------------
    def move(self, dir):
        moveDir = MOVE_DIRS[dir]
        faceDir = tuple(numpy.subtract(self.facing, moveDir))
        turnVal = -0.5

        if (abs(faceDir[0]) == 2 or abs(faceDir[1]) == 2):
            turnVal = 1
        else:
            turnVal = turnVal * faceDir[0] * faceDir[1]

        self.facing = moveDir
        self.loc = self.loc + moveDir
        self.malmo.sendCommand("turn " + str(turnVal))
        self.malmo.sendCommand("move 1")

    def perceive(self):
        # Information comes in as a TimestampedString
        msg = self.malmo.getWorldState().observations[-1].text
        observations = json.loads(msg)
        grid = observations.get(u'floor3x3', 0)
        # Since our agent is blind, it only knows what it's standing on:
        standingOn = grid[4]
        # If we're standing on a goal, huzzah! We win!
        self.env.goalTest(standingOn)
        return standingOn
