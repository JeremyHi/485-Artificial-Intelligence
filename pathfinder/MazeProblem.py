# pylint: disable=missing-docstring

'''
MazeProblem Formalization:
MazeProblems represent 2D pathfinding problems, as programmatically
formalized via:

=== Mazes ===
Represented as a list of strings in which:
  X = impassable wall
  * = the initial state
  . = open cells
  G = goal states
All valid mazes have:
  - At most 1 initial state
  - At least 1 goal state
  - A border of walls (plus possibly other walls)
  - A solution
(We'll ignore invalid maze states as possible inputs, for simplicity)

Maze elements are indexed starting at (0, 0) [top left of maze]. E.g.,
["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"] is interpretable as:

  01234
0 XXXXX
1 X..GX
2 X...X
3 X*..X
4 XXXXX

=== States ===
Representing the position of the agent, as tuples in which:
(x, y) = (col, row)
(0, 0) is located at the top left corner; Right is +x, and Down is +y

=== Actions ===
Representing the allowable Up, Down, Left, and Right movement capabilities
of the agent in the 2D Maze; we'll simply use string representations:
"U", "D", "L", "R"

=== Transitions ===
Given some state s, the transitions will be represented as a list of tuples
of the format:
[(action1, result(action1, s)), ...]
For example, if an agent is at state (1, 1), and can only move right and down,
then the transitions for that s = (1, 1) would be:
[("R", (2, 1)), ("D", (1, 2))]
'''
class MazeProblem:

    # MazeProblem Constructor:
    # Constructs a new pathfinding problem from a maze, described above
    def __init__(self, maze):
        self.maze = maze
        self.initial = ([(item.index('*'), idx) for idx, item in enumerate(maze) if '*' in item][0])
        self.goals = [(item.index('G'), idx) for idx, item in enumerate(maze) if 'G' in item]

    # goalTest is parameterized by a state, and
    # returns True if the given state is a goal, False otherwise
    def goalTest(self, state):
        if state in self.goals:
            return True
        return False

    # transitions returns a list of tuples in the format:
    # [(action1, result(action1, s), ...]
    # corresponding to allowable actions of the given state, as well
    # as the next state the action leads to
    def transitions(self, state):
        allowed_states = []

        # up
        if (state[1]-1 >= 0) and (self.maze[state[1]-1][state[0]] is not ('x' or 'X')):
            allowed_states.append((state[0], state[1]-1))
        # down
        if (state[1]+1 <= 4) and (self.maze[state[1]+1][state[0]] is not ('x' or 'X')):
            allowed_states.append((state[0], state[1]+1))
        # left
        if (state[0]-1 >= 0) and (self.maze[state[1]][state[0]-1] is not ('x' or 'X')):
            allowed_states.append((state[0], state[1]+1))
        # right
        if (state[0]+1 <= 4) and (self.maze[state[1]][state[0]+1] is not ('x' or 'X')):
            allowed_states.append((state[0], state[1]+1))

        return allowed_states

    # solnTest will return a tuple of the format (cost, isSoln) where:
    # cost = the total cost of the solution,
    # isSoln = true if the given sequence of actions of the format:
    # [a1, a2, ...] successfully navigates to a goal state from the initial state
    # If NOT a solution, return a cost of -1
    def solnTest(self, soln):
        trans = {"U": (0, -1), "D": (0, 1), "L": (-1, 0), "R": (1, 0)}
        s = self.initial
        for m in soln:
            s = (s[0] + trans[m][0], s[1] + trans[m][1])
            if self.maze[s[1]][s[0]] == "X":
                return (-1, False)
        return (len(soln), self.goalTest(s))
