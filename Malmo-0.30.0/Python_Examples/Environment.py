# pylint: disable=C0321,C0103,C0111,C0301,R0902,I1101

import sys
import time
import os
import MalmoPython
from MazeAgent import MazeAgent

# Environment Configuration Constants:
FLOOR_LEVEL = 5
MISSION_TIME = 120000
MAX_RETRIES = 3
TICK_LENGTH = 1 # seconds

class Environment:

    # Problem-specific constants
    GOAL_BLOCK = "diamond_block"
    WARN_BLOCK = "obsidian"
    SAFE_BLOCK = "cobblestone"

    def __init__(self, maze):
        self.maze = maze
        self.agMaze = [r.replace('P', '.') for r in maze]
        self.mission_xml = self.getMissionXML(maze)
        self.mission = MalmoPython.MissionSpec(self.mission_xml, True)
        self.mission_record = MalmoPython.MissionRecordSpec()
        self.malmo = MalmoPython.AgentHost()
        self.agent = MazeAgent(self)
        self.attempt = 1
        self.goalReached = False

    def __translateCoord(self, c, r):
        return(len(self.maze[0]) -1 - c, len(self.maze) - 1 - r)

    def __generatePit(self, c, r):
        maze = self.maze

        # Generate pit
        result = '<DrawBlock x="{}" y="5" z="{}" type="lava"/>'.format(c, r)

        # Generate obsidian warning blocks, as long as there isn't another tile already
        # there, and the tile would not be generated outside of the maze's bounds
        #(probably a better way to do this, but meh)
        obsidians = list(filter(lambda b: b[0] != 0 and b[1] != 0 and b[0] < len(maze[0]) and b[1] < len(maze) and maze[len(maze) - b[1] - 1][len(maze[0]) - b[0] - 1] == ".",\
            [(c-1, r), (c+1, r), (c, r-1), (c, r+1)]))
        for coord in obsidians:
            result = result + '<DrawBlock x="{}" y="{}" z="{}" type="{}"/>'.format(
                coord[0], FLOOR_LEVEL, coord[1], Environment.WARN_BLOCK)

        return result

    def __generateMaze(self):
        # maze grid is symmetrical
        maze = self.maze
        rows = len(maze)
        cols = len(maze[0])

        # Base grid at 0,0
        result = '<DrawCuboid x1="0" y1="{}" z1="0" x2="{}" y2="{}" z2="{}" type="{}"/>'.format(FLOOR_LEVEL, cols-1, FLOOR_LEVEL, rows-1, Environment.SAFE_BLOCK)

        # Parse special cell contents
        for r, row in enumerate(maze):
            for c, cell in enumerate(row):
                tcoord = self.__translateCoord(c, r)
                if cell == "*":
                    self.playerPos = tcoord
                elif cell == "X":
                    result = result + '<DrawBlock x="{}" y="{}" z="{}" type="{}"/>'.format(tcoord[0], FLOOR_LEVEL + 1, tcoord[1], Environment.SAFE_BLOCK)
                elif cell == "G":
                    result = result + '<DrawBlock x="{}" y="{}" z="{}" type="{}"/>'.format(tcoord[0], FLOOR_LEVEL, tcoord[1], Environment.GOAL_BLOCK)
                elif cell == "P":
                    result = result + self.__generatePit(tcoord[0], tcoord[1])

        return result

    def getMissionXML(self, maze):
        mazeXML = self.__generateMaze()

        return '''<?xml version="1.0" encoding="UTF-8" standalone="no" ?>
            <Mission xmlns="http://ProjectMalmo.microsoft.com" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

                <About>
                    <Summary>Maze Pitfalls!</Summary>
                </About>

                <ServerSection>
                    <ServerInitialConditions>
                        <Time>
                            <StartTime>1000</StartTime>
                            <AllowPassageOfTime>false</AllowPassageOfTime>
                        </Time>
                        <Weather>clear</Weather>
                    </ServerInitialConditions>
                    <ServerHandlers>
                        <FlatWorldGenerator generatorString="3;7,2*3,11;8;village"/>
                        <DrawingDecorator>
                            <DrawCuboid x1="-50" y1="''' + str(FLOOR_LEVEL) + '''" z1="-50" x2="50" y2="''' + str(FLOOR_LEVEL) + '''" z2="50" type="air"/>
                            ''' + mazeXML + '''
                        </DrawingDecorator>
                        <ServerQuitFromTimeUp timeLimitMs="''' + str(MISSION_TIME) + '''"/>
                        <ServerQuitWhenAnyAgentFinishes/>
                    </ServerHandlers>
                </ServerSection>

                <AgentSection mode="Survival">
                    <Name>BlindBot</Name>
                    <AgentStart>
                        <Placement x="''' + str(self.playerPos[0] + 0.5) + '''" y="''' + str(FLOOR_LEVEL + 1.0) + '''" z="''' + str(self.playerPos[1] + 0.5) + '''"/>
                    </AgentStart>
                    <AgentHandlers>
                        <DiscreteMovementCommands/>
                        <AgentQuitFromTouchingBlockType>
                            <Block type="lava"/>
                        </AgentQuitFromTouchingBlockType>
                        <ObservationFromGrid>
                            <Grid name="floor3x3">
                                <min x="-1" y="-1" z="-1"/>
                                <max x="1" y="-1" z="1"/>
                            </Grid>
                        </ObservationFromGrid>
                    </AgentHandlers>
                </AgentSection>
            </Mission>'''

    def goalTest(self, block):
        if block == Environment.GOAL_BLOCK:
            self.goalReached = True
            print("[$] Mission Successful! Deaths: " + str(self.attempt - 1))

    def startMission(self):
        if self.attempt <= MAX_RETRIES:
            print("[~] Starting mission - Attempt #" + str(self.attempt))
            self.malmo.startMission(self.mission, self.mission_record)
            world_state = self.malmo.getWorldState()
            while not world_state.has_mission_begun:
                sys.stdout.write(".")
                time.sleep(0.1)
                world_state = self.malmo.getWorldState()

            print("[!] Mission started!")
            while world_state.is_mission_running and not self.goalReached:
                time.sleep(TICK_LENGTH)
                self.agent.act()
                world_state = self.malmo.getWorldState()

            if not self.goalReached:
                self.agent.die()
                self.attempt += 1
                self.startMission()
        else:
            print("[X] GAME OVER!")
