# pylint: disable=C0111,C0103

'''
JEREMY HITCHCOCK

MazeKnowledgeBase.py

Specifies a simple, Conjunctive Normal Form Propositional
Logic Knowledge Base for use in Grid Maze pathfinding problems
with side-information.
'''
import unittest
from MazeClause import MazeClause

class MazeKnowledgeBase:

    def __init__(self):
        self.clauses = set()

    # [!] Assumes that a clause is never added that causes the
    # KB to become inconsistent
    def tell(self, clause):
        return self.clauses.add(clause)

    # [!] Queries are always MazeClauses
    def ask(self, query):
        clauses = set(self.clauses)
        new = set()

        for clause1 in clauses:
            for clause2 in clauses:
                resolvents = query.resolve(clause1, clause2)
                if {} in resolvents:
                    return True
                new.union(resolvents)
            if new in clauses:
                return False
            clauses = clauses.union(new)

class MazeKnowledgeBaseTests(unittest.TestCase):
    def test_mazekb1(self):
        kb = MazeKnowledgeBase()
        kb.tell(MazeClause([(("X", (1, 1)), True)]))
        self.assertTrue(kb.ask(MazeClause([(("X", (1, 1)), True)])))

    # def test_mazekb2(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Y", (1, 1)), True)])))
    #
    # def test_mazekb3(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("Y", (1, 1)), False), (("Z", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), True), (("Z", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("W", (1, 1)), True)])))
    #     self.assertFalse(kb.ask(MazeClause([(("Y", (1, 1)), False)])))
    #
    # def test_mazekb4(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), False), (("Z", (1, 1)), False), (("S", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("S", (1, 1)), False), (("T", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True), (("T", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("T", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
    #
    # def test_mazekb5(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), False), (("Z", (1, 1)), False), (("S", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("S", (1, 1)), False), (("T", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True), (("T", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("W", (1, 1)), True)]))
    #     kb.tell(MazeClause([(("T", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), True), (("W", (1, 1)), True)])))
    #
    # def test_mazekb6(self):
    #     kb = MazeKnowledgeBase()
    #     kb.tell(MazeClause([(("X", (1, 1)), False),
    #                         (("Y", (1, 1)), False),
    #                         (("Z", (1, 1)), False)]))
    #     kb.tell(MazeClause([(("X", (1, 1)), True)]))
    #     self.assertFalse(kb.ask(MazeClause([(("Z", (1, 1)), False)])))
    #     kb.tell(MazeClause([(("Y", (1, 1)), True)]))
    #     self.assertTrue(kb.ask(MazeClause([(("Z", (1, 1)), False)])))


if __name__ == "__main__":
    unittest.main()
