from CubeFaces import CubeFaces
import Cube

FRONT, BACK, UP, DOWN, RIGHT, LEFT = "FRONT", "BACK", "UP", "DOWN", "RIGHT", "LEFT"


class Solver:

    def __init__(self):
        cubeface = CubeFaces()
        cubeface.init_all_faces()
        self.cube = Cube.Cube(cubeface.faces)
        self.Upface = cubeface.faces[0]
        self.Frontface = cubeface.faces[1]
        self.Rightface = cubeface.faces[2]
        self.Backface = cubeface.faces[3]
        self.Leftface = cubeface.faces[4]
        self.Downface = cubeface.faces[5]
        self.graph = {UP: [FRONT, LEFT, RIGHT, BACK],
                      FRONT: [RIGHT, LEFT, UP, DOWN],
                      RIGHT: [FRONT, BACK, UP, DOWN],
                      BACK: [RIGHT, LEFT, UP, DOWN],
                      LEFT: [FRONT, BACK, UP, DOWN],
                      DOWN: [FRONT, LEFT, RIGHT, BACK]}

    def is_face_solved(self, face):
        if (len(set(face[0])) == 1)\
                & (len(set(face[1])) == 1)\
                & (len(set(face[2])) == 1):
            return True
        return False

    def is_cube_solved(self):
        if (self.is_face_solved(self.Upface) is True) & \
                (self.is_face_solved(self.Frontface) is True) & \
                (self.is_face_solved(self.Rightface) is True) & \
                (self.is_face_solved(self.Backface) is True) & \
                (self.is_face_solved(self.Leftface) is True) & \
                (self.is_face_solved(self.Downface) is True):
            return True
        return False

    def is_cross_solved(self, face):
        center = face[1][1]
        if face[0][1] == face[1][0] == face[2][1] == face[1][2] == center:
            return True
        return False





