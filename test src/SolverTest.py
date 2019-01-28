import unittest
from Solver import Solver


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.solver = Solver()

    def test_is_face_solved(self):
        self.assertEqual(True, self.solver.is_face_solved(self.solver.Frontface))

    def test_is_cube_solved(self):
        self.assertTrue(self.solver.is_cube_solved())

    def test_is_cross_solved(self):
        self.assertTrue(self.solver.is_cross_solved(self.solver.Frontface))



if __name__ == '__main__':
    unittest.main()
