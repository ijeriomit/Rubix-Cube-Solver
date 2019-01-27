import Piece


ROT_XY_CW = [[0, 1, 0],
             [-1, 0, 0],
             [0, 0, 1]]

ROT_XY_CC = [[0, -1, 0],
             [1, 0, 0],
             [0, 0, 1]]

# 90 degree rotations in the XZ plane (around the y-axis when viewed pointing toward you).
ROT_XZ_CW = [[0, 0, -1],
             [0, 1, 0],
             [1, 0, 0]]

ROT_XZ_CC = [[0, 0, 1],
             [0, 1, 0],
             [-1, 0, 0]]

# 90 degree rotations in the YZ plane (around the x-axis when viewed pointing toward you).
ROT_YZ_CW = [[1, 0, 0],
             [0, 0, 1],
             [0, -1, 0]]

ROT_YZ_CC = [[1, 0, 0],
             [0, 0, -1],
             [0, 1, 0]]


class Cube:

    def __init__(self, faces):
        self.centers = (
            Piece.Piece(Piece.Piece.CENTER, (0, 0, 1)),   # Front
            Piece.Piece(Piece.Piece.CENTER, (0, 0, -1)),  # Back
            Piece.Piece(Piece.Piece.CENTER, (0, 1, 0)),   # Up
            Piece.Piece(Piece.Piece.CENTER, (0, -1, 0)),  # Down
            Piece.Piece(Piece.Piece.CENTER, (1, 0, 0)),   # Right
            Piece.Piece(Piece.Piece.CENTER, (-1, 0, 0)))  # Left

        self.sides = (
            Piece.Piece(Piece.Piece.SIDE, (0, 1, 1)),     # Top-South
            Piece.Piece(Piece.Piece.SIDE, (0, 1, -1)),    # Top-North
            Piece.Piece(Piece.Piece.SIDE, (1, 1, 0)),     # Top-East
            Piece.Piece(Piece.Piece.SIDE, (-1, 1, 0)),    # Top-West
            Piece.Piece(Piece.Piece.SIDE, (0, -1, 1)),    # Bottom-South
            Piece.Piece(Piece.Piece.SIDE, (0, -1, -1)),   # Bottom-North
            Piece.Piece(Piece.Piece.SIDE, (1, -1, 0)),    # Bottom-East
            Piece.Piece(Piece.Piece.SIDE, (-1, -1, 0)),   # Bottom-West
            Piece.Piece(Piece.Piece.SIDE, (1, 0, -1)),    # Middle-NorthEast
            Piece.Piece(Piece.Piece.SIDE, (1, 0, 1)),     # Middle-SouthEast
            Piece.Piece(Piece.Piece.SIDE, (-1, 0, -1)),   # Middle-NorthWest
            Piece.Piece(Piece.Piece.SIDE, (-1, 0, 1)))   # Middle-SouthWest

        self.edges = (
            Piece.Piece(Piece.Piece.EDGE, (1, 1, 1)),     # Top-SouthEast
            Piece.Piece(Piece.Piece.EDGE, (-1, 1, 1)),    # Top-SouthWest
            Piece.Piece(Piece.Piece.EDGE, (1, 1, -1)),    # Top-NorthEast
            Piece.Piece(Piece.Piece.EDGE, (-1, 1, -1)),   # Top-NorthWest
            Piece.Piece(Piece.Piece.EDGE, (1, -1, 1)),    # Bottom-SouthEast
            Piece.Piece(Piece.Piece.EDGE, (-1, -1, 1)),   # Bottom-SouthWest
            Piece.Piece(Piece.Piece.EDGE, (1, -1, -1)),   # Bottom-NorthEast
            Piece.Piece(Piece.Piece.EDGE, (-1, -1, -1)))  # Bottom-NorthWest
        self.cubepieces = self.sides + self.edges + self.centers
        self.set_piece_colors(faces)

    def set_piece_colors(self, faces):
        for i in range(0, 3):
            for j in range(0, 3):
                self.get_piece((-1+j, 1, -1+i)).set_color(faces[0][i][j], Piece.UP)
                self.get_piece((-1+j, 1-i, 1)).set_color(faces[1][i][j], Piece.FRONT)
                self.get_piece((1, 1-i, 1-j)).set_color(faces[2][i][j], Piece.RIGHT)
                self.get_piece((1-j, 1-i, -1)).set_color(faces[3][i][j], Piece.BACK)
                self.get_piece((-1, 1-i, -1+j)).set_color(faces[4][i][j], Piece.LEFT)
                self.get_piece((-1+j, -1, -1+i)).set_color(faces[5][i][j], Piece.DOWN)

    def get_piece(self, position):
        for piece in self.cubepieces:
            if piece.pos == position:
                return piece

    def get_face_by_xpos(self, x):
        newlist = list()
        for piece in self.cubepieces:
            if piece.pos[0] == x:
                newlist.append(piece)
        return newlist

    def get_face_by_ypos(self, y):
        newlist = list()
        for piece in self.cubepieces:
            if piece.pos[1] == y:
                newlist.append(piece)
        return newlist

    def get_face_by_zpos(self, z):
        newlist = list()
        for piece in self.cubepieces:
            if piece.pos[2] == z:
                newlist.append(piece)
        return newlist

    def rotate_face(self, axis, pos, rotation, name):
        face = None
        if axis == "x":
            face = self.get_face_by_xpos(pos)
        elif axis == "y":
            face = self.get_face_by_ypos(pos)
        elif axis == "z":
            face = self.get_face_by_zpos(pos)
        for piece in face:
            piece.rotate(rotation, name)
        return face

    def R(self):
        return self.rotate_face("x", 1, ROT_YZ_CW, "R")

    def Ri(self):
        return self.rotate_face("x", 1, ROT_YZ_CC, "Ri")

    def M(self):
        return self.rotate_face("x", 0, ROT_YZ_CC, "M")

    def Mi(self):
        return self.rotate_face("x", 0, ROT_YZ_CW, "Mi")

    def L(self):
        return self.rotate_face("x", -1, ROT_YZ_CC, "L")

    def Li(self):
        return self.rotate_face("x", -1, ROT_YZ_CW, "Li")

    def U(self):
        return self.rotate_face("y", 1, ROT_XZ_CW, "U")

    def Ui(self):
        return self.rotate_face("y", 1, ROT_XZ_CC, "Ui")

    def E(self):
        return self.rotate_face("y", 0, ROT_XZ_CC, "E")

    def Ei(self):
        return self.rotate_face("y", 0, ROT_XZ_CW, "Ei")

    def D(self):
        return self.rotate_face("y", -1, ROT_XZ_CC, "D")

    def Di(self):
        return self.rotate_face("y", -1, ROT_XZ_CW, "Di")

    def F(self):
        return self.rotate_face("z", 1, ROT_XY_CW, "F")

    def Fi(self):
        return self.rotate_face("z", 1, ROT_XY_CC, "Fi")

    def S(self):
        return self.rotate_face("z", 0, ROT_XY_CW, "S")

    def Si(self):
        return self.rotate_face("z", 0, ROT_XY_CC, "Si")

    def B(self):
        return self.rotate_face("z", -1, ROT_XY_CC, "B")

    def Bi(self):
        return self.rotate_face("z", -1, ROT_XY_CW, "Bi")















