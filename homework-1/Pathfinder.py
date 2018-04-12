# pylint: disable=missing-docstring

'''
NAME: Jeremy Hitchcock

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

    # have goal_test(state), heuristic(state), transitions(state), and cost(state) function
    # SearchTreeNode(state, action, parent, total_cost, heuristic_cost) children = []

    @staticmethod
    def solve(problem):
        def lowest_f(open_list):
            lowest_cost = open_list[0]
            for node in open_list:
                f_node = node.total_cost + node.heuristic_cost
                c_node = lowest_cost.total_cost + lowest_cost.heuristic_cost
                if f_node < c_node:
                    lowest_cost = node
            return lowest_cost

        initial_position = problem.initial

        start = SearchTreeNode(initial_position, None, None, 0, 0)

        open_list = [start]
        closed_list = set()

        counter = 0
        while open_list:
            current_node = lowest_f(open_list)
            open_list.remove(current_node)

            transitions_current_node = []
            for transition in problem.transitions(current_node.state):
                if transition[2] not in closed_list:
                    transitions_current_node.append(transition)

            for transition in transitions_current_node:
                transition = SearchTreeNode(transition[2], transition[0],
                                            current_node, transition[1],
                                            problem.heuristic(transition[2]))
                current_node.children.append(transition)

                if problem.goal_test(transition.state):
                    solution = []
                    while transition.parent is not None:
                        solution.append(transition.action)
                        transition = transition.parent
                    print(counter)
                    return list(reversed(solution))

                if transition.state not in closed_list:
                    counter += 1
                    open_list.append(transition)

            closed_list.add(current_node.state)
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

    def test_maze5(self):
        maze = ["XXXXXXXXXX", "X..X.....X", "X*.....XXX",
                "XXX..X.XGX", "X...XX.X.X", "X.X.X.X...X",
                "X...X.XX.X", "X..G.XXX.X", "X........X",
                "XXXXXXXXXX"]
        problem = MazeProblem(maze)
        soln = Pathfinder.solve(problem)
        soln_test = problem.soln_test(soln)
        self.assertTrue(soln_test[1])
        self.assertEqual(soln_test[0], 7)


if __name__ == '__main__':
    unittest.main()
