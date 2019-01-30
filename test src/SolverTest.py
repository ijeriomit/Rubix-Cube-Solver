import unittest
from Solver import Solver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = Solver()

    def test_is_face_solved(self):
        self.assertEqual(True, self.solver.is_face_solved(self.solver.grids[0]))

    def test_is_cube_solved(self):
        self.assertTrue(self.solver.is_cube_solved())

    def test_is_cross_solved(self):
        self.assertTrue(self.solver.is_cross_solved(self.solver.grids[0]))

    def test_color__pos_grid(self):
        self.assertEqual(
            [[[(-1 + j, 1, -1 + i) for j in range(3)] for i in range(3)],
             [[(-1+j, 1-i, 1) for j in range(3)] for i in range(3)],
             [[(1, 1-i, 1-j) for j in range(3)] for i in range(3)],
             [[(1-j, 1-i, -1) for j in range(3)] for i in range(3)],
             [[(-1, 1-i, -1+j) for j in range(3)] for i in range(3)],
             [[(-1+j, -1, -1+i) for j in range(3)] for i in range(3)]],
            [self.solver.grids[0].colorposgrid,
                self.solver.grids[1].colorposgrid,
                self.solver.grids[2].colorposgrid,
                self.solver.grids[3].colorposgrid,
                self.solver.grids[4].colorposgrid,
                self.solver.grids[5].colorposgrid])

if __name__ == '__main__':
    unittest.main()
