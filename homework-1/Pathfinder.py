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

        def lowest_cost(o_list):
            lowest_cost = o_list[0]
            for node in o_list:
                node_cost = node.total_cost + node.heuristic_cost
                lowest = lowest_cost.total_cost + lowest_cost.heuristic_cost
                if node_cost < lowest:
                    lowest_cost = node
            return lowest_cost

        def in_list(oc_list, transition):
            for node in oc_list:
                if transition.state == node.state and transition.total_cost < node.total_cost:
                    return True
            return False

        def repeated_node(oc_list, transition):
            for node in oc_list:
                if transition.state == node.state and transition.total_cost < node.total_cost:
                    return node
            return False

        initial_position = problem.initial
        cost_to_goal = problem.heuristic(initial_position)

        start = SearchTreeNode(initial_position, None, None, 0, cost_to_goal)
        start.children = problem.transitions(start.state)
        goals = problem.goals

        open_list = [start]
        closed_list = []

        # pylint: disable=E0602
        while open_list:
            q = lowest_cost(open_list)
            open_list.remove(q)
            transitions = problem.transitions(q.state)
            for transition in transitions:
                transition = SearchTreeNode(transition[1], transition[0], q, 0, 0)
                transition.parent = q
                if problem.goal_test(transition):
                    transition.total_cost = q.total_cost + problem.cost(transition.state)
                    transition.heuristic_cost = problem.heuristic(transition.state)
                    transition.total_cost = transition.total_cost + transition.heuristic_cost
                if not in_list(open_list, transition) or in_list(closed_list, transition):
                    open_list.append(repeated_node(closed_list, transition))
            closed_list.append(q)
        print(closed_list)
        return closed_list


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


if __name__ == '__main__':
    unittest.main()
