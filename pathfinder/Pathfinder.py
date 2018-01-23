# pylint: disable=missing-docstring

'''
The Pathfinder class is responsible for finding a solution (i.e., a
sequence of actions) that takes the agent from the initial state to the
optimal goal state.

This task is done in the Pathfinder.solve method, as parameterized
by a maze pathfinding problem, and is aided by the SearchTreeNode DS.
'''

import unittest
from MazeProblem import MazeProblem
from SearchTreeNode import SearchTreeNode


class Pathfinder:

    # solve is parameterized by a maze pathfinding problem
    # (see MazeProblem.py and unit tests below), and will
    # return a list of actions that solves that problem. An
    # example returned list might look like:
    # ["U", "R", "R", "U"]
    def solve(self, problem):
        '''
        Problem = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
            - problem.initial = (1,3)
            - problem.goals = [(3, 1)]
        '''
        possibilities = MazeProblem.transitions(self, problem.initial)
        return []

class PathfinderTests(unittest.TestCase):

    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(self, problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(self, problem)
        solnTest = problem.solnTest(soln)
        self.assertTrue(solnTest[1])
        self.assertEqual(solnTest[0], 4)

if __name__ == '__main__':
    unittest.main()
