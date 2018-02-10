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

    @staticmethod
    def solve(problem):
        counter = 0
        def lowestf(open_list):
            lowF = open_list[0]

            for n in open_list:
                fNode = n.total_cost + n.heuristic_cost
                cNode = lowF.total_cost + lowF.heuristic_cost

                if fNode < cNode:
                    lowF = n

            open_list.remove(lowF)
            return lowF

        def solution(node):
            solution = []
            while node.parent is not None:
                solution.append(node.action)
                node = node.parent
            solution = list(reversed(solution))
            return solution

        initial_position = problem.initial
        cost_to_goal = problem.heuristic(initial_position)

        start = SearchTreeNode(initial_position, None, None, 0, 0)

        open_list = [start]
        closed_list = []

        while open_list:
            n = lowestf(open_list)
            transitions = []
            children = []
            for t in problem.transitions(n.state):
                if t[2] not in closed_list:
                    transitions.append(t)

            for t in transitions:
                state = t[2]
                action = t[0]
                parent = n
                total_cost = n.total_cost + t[1]
                heuristic_cost = problem.heuristic(state)
                child = SearchTreeNode(state, action, parent, total_cost, heuristic_cost)
                counter += 1
                n.children.append(child)

                if problem.goal_test(child.state):
                    print(counter)
                    return solution(child)
                if child.state not in closed_list:
                    open_list.append(child)

            closed_list.append(n.state)

        return None


class PathfinderTests(unittest.TestCase):
    def test_maze1(self):
        maze = ["XXXXX", "X..GX", "X...X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze2(self):
        maze = ["XXXXX", "XG..X", "XX..X", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze3(self):
        maze = ["XXXXX", "X..GX", "X.MMX", "X*..X", "XXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 4)

    def test_maze4(self):
        maze = ["XXXXXX", "X....X", "X*.XXX", "X..XGX", "XXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        self.assertFalse(soln)

    def test_uniform_cost_maze(self):
        maze = ["XXXXXXXXXXXX",
                "X*.........X",
                "X........XXX",
                "X........XXX",
                "X........XXX",
                "X.........GX",
                "XXXXXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        self.assertTrue(soln)


if __name__ == '__main__':
    unittest.main()
