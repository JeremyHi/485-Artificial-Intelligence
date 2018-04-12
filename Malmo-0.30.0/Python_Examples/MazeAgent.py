# pylint: disable=C0321,C0103,C0111,C0301,R0902,I1101

import time
import json
from Queue import Queue
import numpy

# Agent constants
MOVE_DIRS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

class MazeAgent:

    def __init__(self, env):
        self.env = env
        self.malmo = env.malmo
        self.loc = env.playerPos
        self.facing = (0, 1)
        self.maze = env.agMaze
        self.plan = Queue()

        self.maze_width = len(self.maze[0])-1
        self.maze_height = len(self.maze)-1

        self.start = self.loc
        self.lava = []
        self.safe = [self.start]
        self.warning = []
        self.visited = []

    # [!] TODO! Agent currently just runs straight up
    def think(self, perception):
        print((self.loc[0], self.loc[1]))

        if self.loc[1]+1 < self.maze_height and (self.loc[0], self.loc[1]+1) not in self.visited:
            print("Up")
            self.plan.put("U")
            self.loc = (self.loc[0], self.loc[1]+1)
        elif self.loc[0]-1 < self.maze_width and (self.loc[0]-1, self.loc[1]) not in self.visited:
            print("Right")
            self.plan.put("R")
            self.loc = (self.loc[0]-1, self.loc[1])
        elif self.loc[1]-1 > 1 and (self.loc[0], self.loc[1]-1) not in self.visited:
            print("Down")
            self.plan.put("D")
            self.loc = (self.loc[0], self.loc[1]-1)
        else:
            print("Left")
            self.plan.put("L")
            self.loc = (self.loc[0]+1, self.loc[1])

        self.visited.append((self.loc[0], self.loc[1]))

    def act(self):
        # BlindBot perceives what it is standing on...
        perception = self.perceive()
        if perception == 'obsidian':
            self.warning.append((self.loc[0], self.loc[1]))
            print("obsidian found)" + str(self.warning))

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
        self.lava.append((self.loc[0], self.loc[1]))
        # we know that all four spots around are obsidian/barrier aka not visitable
        self.warning.append((self.loc[0]-1, self.loc[1]),
                            (self.loc[0]+1, self.loc[1]),
                            (self.loc[0], self.loc[1]+1),
                            (self.loc[0], self.loc[1]-1))
        # Reset player position back to start
        self.loc = self.env.playerPos

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
