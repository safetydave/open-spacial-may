import os
import sys
import unittest

sys.path.append(os.path.abspath('..'))
from src.solver import Solver
from src.officegraph import OfficeGraph


class TestSolver(unittest.TestCase):

    def test_can_haz_food(self):
        og3 = OfficeGraph(3)
        solver = Solver(og3)
        self.assertTrue(solver.can_haz_food(0))
        og3.apply_occupancy([3, 4])
        self.assertTrue(solver.can_haz_food(1))
        og3.apply_occupancy([5])
        self.assertFalse(solver.can_haz_food(2))