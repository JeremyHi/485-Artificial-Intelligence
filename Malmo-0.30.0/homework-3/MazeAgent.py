import numpy
import time
import json
from Queue import Queue

# Agent constants
MOVE_DIRS = {"U": (0, 1), "D": (0, -1), "L": (-1, 0), "R": (1, 0)}

class MazeAgent:
    
    def __init__ (self, env):
        self.env = env
        self.malmo = env.malmo
        self.loc = env.playerPos
        self.facing = (0, 1)
        self.maze = env.agMaze
        self.plan = Queue()
        # [!] TODO: Initialize any other knowledge-related attributes for
        # agent here
    
    # [!] TODO! Agent currently just runs straight up
    def think (self, perception):
        # Agent simply plans to move forward at the moment
        # Do something that thinks about the perception!
        self.plan.put("U")
    
    def act (self):
        # BlindBot perceives what it is standing on...
        perception = self.perceive()
        # ...BlindBot thinks...
        self.think(perception)
        # ...and then moves according to its plan, if it has one
        if (self.plan.empty()):
            return
        self.move(self.plan.get())
        return
    
    # [!] TODO: Any record-keeping when bot dies
    def die (self):
        # Reset player position back to start
        self.loc = self.env.playerPos
    
    # -----------------------------------------------------------------------
    # YOU MAY NOT MODIFY ANYTHING BELOW THIS LINE
    # -----------------------------------------------------------------------
    def move (self, dir):
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
    
    def perceive (self):
        # Information comes in as a TimestampedString
        msg = self.malmo.getWorldState().observations[-1].text
        observations = json.loads(msg)
        grid = observations.get(u'floor3x3', 0)
        # Since our agent is blind, it only knows what it's standing on:
        standingOn = grid[4]
        # If we're standing on a goal, huzzah! We win!
        self.env.goalTest(standingOn)
        return standingOn
    