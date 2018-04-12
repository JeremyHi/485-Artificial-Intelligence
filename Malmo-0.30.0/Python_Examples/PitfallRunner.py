# pylint: disable=C0321,C0103,C0111,C0301,R0902,I1101

import time
from Environment import Environment

if __name__ == "__main__":
    mazes = [\
        # Easy difficulty: Needs only 1 life to solve
        ["XXXXXX",
         "X...GX",\
         "X..P.X",\
         "X....X",\
         "X..P.X",\
         "X*...X",\
         "XXXXXX"],

        # Medium difficulty: Needs at most 2 lives
        ["XXXXXXXXX",
         "X..PGP..X",\
         "X.......X",\
         "X..P.P..X",\
         "X.......X",\
         "X*......X",\
         "XXXXXXXXX"],

        # Hard difficulty: Needs a good heuristic and 2-3 lives
        ["XXXXXXXXXXXX",
         "XP.....G...X",\
         "XP.........X",\
         "X...PP..P..X",\
         "X....PPPPPPX",\
         "X......P.P.X",\
         "X..........X",\
         "XPPP.....*.X",\
         "X..P.......X",\
         "XXXXXXXXXXXX"]
    ]

    # Pick your difficulty!
    env = Environment(mazes[0])
    env.startMission()
