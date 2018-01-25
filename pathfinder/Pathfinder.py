# pylint: disable=missing-docstring
'''
Group Memebers:
- Jeremy Hitchcock
- David Parks
- Nick Le Gorric
- Tyler Colson




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
        already_visited = set()
        nodes = [[SearchTreeNode(state=problem.initial, action=None, parent=None)]]
        already_visited.add(nodes[0][0].state)
        while nodes:
            current_level = nodes.pop()
            for node in current_level:
                if problem.goalTest(node.state):
                    solution = []
                    while node.parent is not None:
                        solution.append(node.action)
                        node = node.parent
                    return list(reversed(solution))
                else:
                    already_visited.add((node.state))

            next_level = []
            for node in current_level:
                transitions = problem.transitions(node.state)
                for transition in transitions:
                    if transition[1] not in already_visited:
                        new_node = SearchTreeNode(transition[1], transition[0], node)
                        next_level.append(new_node)
            nodes.append(next_level)

class PathfinderTests(unittest.TestCase):

    def test_maze1(self):
        maze = [
            "XXXXX",
            "X..GX",
            "X...X",
            "X*..X",
            "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(self, problem)
        soln_test = problem.solnTest(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze2(self):
        maze = [
            "XXXXX",
            "XG..X",
            "XX..X",
            "X*..X",
            "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(self, problem)
        soln_test = problem.solnTest(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze3(self):
        maze = [
            "XXXXXXX",
            "XG....X",
            "XX...XX",
            "X*..XXX",
            "XXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(self, problem)
        soln_test = problem.solnTest(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze4(self):
        maze = [
            "XXXXXXXXX",
            "XXXG..XXX",
            "XXXXX.XXX",
            "XX*...XXX",
            "XXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(self, problem)
        soln_test = problem.solnTest(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 7)

if __name__ == '__main__':
    unittest.main()
