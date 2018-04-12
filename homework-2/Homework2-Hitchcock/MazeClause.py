# pylint: disable=C0111,C0103

'''
JEREMY HITCHCOCK

MazeClause.py

Specifies a Propositional Logic Clause formatted specifically
for Grid Maze Pathfinding problems. Clauses are a disjunction of
GridPropositions (2-tuples of (symbol, location)) mapped to
their negated status in the sentence.
'''
import unittest

class MazeClause:

    def __init__(self, props):
        self.props = {}
        self.valid = False

        all_props = {prop for prop in props}
        props_tuples = [p[0] for p in all_props]

        for prop in all_props:
            if props_tuples.count(prop[0]) > 1:
                self.valid = True
            else:
                self.props.update({prop})

    def get_prop(self, prop):
        props_locations = list(self.props.keys())
        if prop in props_locations:
            return self.props[prop]
        return None

    def is_valid(self):
        return self.valid

    def is_empty(self):
        return True if not self.props else False

    def __eq__(self, other):
        return self.props == other.props and self.valid == other.valid

    def __hash__(self):
        # Hashes an immutable set of the stored props for ease of
        # lookup in a set
        return hash(frozenset(self.props.items()))

    # Hint: Specify a __str__ method for ease of debugging (this
    # will allow you to "print" a MazeClause directly to inspect
    # its composite literals)
    def __str__(self):
        return self.props

    @staticmethod
    def resolve(c_1, c_2):
        final_set = {**c_1.props, **c_2.props}
        if c_1.__eq__(c_2):
            return set()

        c1_keys = list(c_1.props.keys())
        c2_keys = list(c_2.props.keys())
        for c1_key in c1_keys:
            if c1_key in c2_keys:
                if c_1.props[c1_key] != c_2.props[c1_key]:
                    del final_set[c1_key]

        if final_set:
            response = [((item), final_set[item]) for item in final_set]
            res = MazeClause(response)
            return {res}
        return {MazeClause([])}


class MazeClauseTests(unittest.TestCase):
    def test_mazeprops1(self):
        m_c = MazeClause([(("X", (1, 1)), True), (("X", (2, 1)), True), (("Y", (1, 2)), False)])
        self.assertTrue(m_c.get_prop(("X", (1, 1))))
        self.assertTrue(m_c.get_prop(("X", (2, 1))))
        self.assertFalse(m_c.get_prop(("Y", (1, 2))))
        self.assertTrue(m_c.get_prop(("X", (2, 2))) is None)
        self.assertFalse(m_c.is_empty())

    def test_mazeprops2(self):
        mc = MazeClause([(("X", (1, 1)), True), (("X", (1, 1)), True)])
        self.assertTrue(mc.get_prop(("X", (1, 1))))
        self.assertFalse(mc.is_empty())

    def test_mazeprops3(self):
        mc = MazeClause([(("X", (1, 1)), True), (("Y", (2, 1)), True), (("X", (1, 1)), False)])
        self.assertTrue(mc.is_valid())
        self.assertTrue(mc.get_prop(("X", (1, 1))) is None)
        self.assertFalse(mc.is_empty())

    def test_mazeprops4(self):
        mc = MazeClause([])
        self.assertFalse(mc.is_valid())
        self.assertTrue(mc.is_empty())

    def test_mazeprops5(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    def test_mazeprops6(self):
        mc1 = MazeClause([(("X", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([]) in res)

    def test_mazeprops7(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (2, 2)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), True), (("Y", (2, 2)), True)]) in res)

    def test_mazeprops8(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    def test_mazeprops9(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), True), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 0)

    # returns a set with a MazeClause as its element
    def test_mazeprops10(self):
        mc1 = MazeClause([(("X", (1, 1)), True), (("Y", (1, 1)), False), (("Z", (1, 1)), True)])
        mc2 = MazeClause([(("X", (1, 1)), False), (("Y", (1, 1)), False), (("W", (1, 1)), False)])
        res = MazeClause.resolve(mc1, mc2)
        self.assertEqual(len(res), 1)
        self.assertTrue(MazeClause([(("Y", (1, 1)), False),
                                    (("Z", (1, 1)), True),
                                    (("W", (1, 1)), False)]) in res)

if __name__ == "__main__":
    unittest.main()
