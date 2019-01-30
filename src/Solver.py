from CubeFaces import CubeFaces
import Cube
from Images import Cube_1


UP, FRONT, RIGHT, BACK, LEFT, DOWN = 0, 1, 2, 3, 4, 5

class Grid:

    # Constructor to create  a new node
    def __init__(self, name, color, pos):
        self.colorgrid = color
        self.colorposgrid = pos
        self.FaceName = name


class Solver:

    pos_grid = list()
    pos_grid.append([[(-1 + j, 1, -1 + i) for j in range(3)] for i in range(3)])
    pos_grid.append([[(-1 + j, 1 - i, 1) for j in range(3)] for i in range(3)])
    pos_grid.append([[(1, 1 - i, 1 - j) for j in range(3)] for i in range(3)])
    pos_grid.append([[(1 - j, 1 - i, -1) for j in range(3)] for i in range(3)])
    pos_grid.append([[(-1, 1 - i, -1 + j) for j in range(3)] for i in range(3)])
    pos_grid.append([[(-1 + j, -1, -1 + i) for j in range(3)] for i in range(3)])

    def __init__(self):
        cubeface = CubeFaces(Cube_1)
        cubeface.init_all_faces()
        self.cube = Cube.Cube(cubeface.faces)
        self.grids = [Grid("UP", cubeface.faces[UP], self.pos_grid[UP]),
                      Grid("FRONT", cubeface.faces[FRONT], self.pos_grid[FRONT]),
                      Grid("RIGHT", cubeface.faces[RIGHT], self.pos_grid[RIGHT]),
                      Grid("BACK", cubeface.faces[BACK], self.pos_grid[BACK]),
                      Grid("LEFT", cubeface.faces[LEFT], self.pos_grid[LEFT]),
                      Grid("DOWN", cubeface.faces[DOWN], self.pos_grid[DOWN])]

    def is_face_solved(self, face):
        if (len(set(face[0])) == 1)\
                & (len(set(face[1])) == 1)\
                & (len(set(face[2])) == 1):
            return True
        return False

    def is_cube_solved(self):
        if (self.is_face_solved(self.grids[UP].colorgrid) is True) & \
                (self.is_face_solved(self.grids[FRONT].colorgrid) is True) & \
                (self.is_face_solved(self.grids[RIGHT].colorgrid) is True) & \
                (self.is_face_solved(self.grids[BACK].colorgrid) is True) & \
                (self.is_face_solved(self.grids[LEFT].colorgrid) is True) & \
                (self.is_face_solved(self.grids[DOWN].colorgrid) is True):
            return True
        return False

    def is_cross_solved(self, face):
        center = face[1][1]
        if face[0][1] == face[1][0] == face[2][1] == face[1][2] == center:
            return True
        return False





