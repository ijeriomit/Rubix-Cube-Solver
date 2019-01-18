
class Node:

    # Constructor to create  a new node
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    # Constructor to create a empty circular linked list
    def __init__(self, start, second, third, last):
        self.head = None
        self.push(start)
        self.push(second)
        self.push(third)
        self.push(last)

    # Function to insert a node at the beginning of a
    # circular linked list
    def push(self, data):
        ptr1 = Node(data)
        temp = self.head

        ptr1.next = self.head

        # If linked list is not None then set the next of
        # last node
        if self.head is None:
            ptr1.next = ptr1
            self.head = ptr1
        else:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr1

    def findNext(self, val):
        temp = self.head
        while True:
            if temp.data == val:
                return temp.next.data
            temp = temp.next
            if temp == self.head:
                break


FRONT = "FRONT"
BACK = "BACK"
UP = "UP"
DOWN = "DOWN"
RIGHT = "RIGHT"
LEFT = "LEFT"


class Piece:

    CENTER = "center"
    SIDE = "side"
    EDGE = "edge"

    U_rotation = CircularLinkedList(FRONT, LEFT, BACK, RIGHT)
    Ui_rotation = CircularLinkedList(FRONT, RIGHT, BACK, LEFT)
    D_rotation = CircularLinkedList(FRONT, RIGHT, BACK, LEFT)
    Di_rotation = CircularLinkedList(FRONT, LEFT, BACK, RIGHT)
    L_rotation = CircularLinkedList(UP, FRONT, DOWN, BACK)
    Li_rotation = CircularLinkedList(UP, BACK, DOWN, FRONT)
    R_rotation = CircularLinkedList(UP, BACK, DOWN, FRONT)
    Ri_rotation = CircularLinkedList(UP, FRONT, DOWN, BACK)
    F_rotation = CircularLinkedList(UP, RIGHT, DOWN, LEFT)
    Fi_rotation = CircularLinkedList(UP, LEFT, DOWN, RIGHT)
    B_rotation = CircularLinkedList(UP, LEFT, DOWN, RIGHT)
    Bi_rotation = CircularLinkedList(UP, RIGHT, DOWN, LEFT)
    M_rotation = CircularLinkedList(UP, FRONT, DOWN, BACK)
    Mi_rotation = CircularLinkedList(UP, BACK, DOWN, FRONT)
    E_rotation = CircularLinkedList(FRONT, RIGHT, BACK, LEFT)
    Ei_rotation = CircularLinkedList(FRONT, LEFT, BACK, RIGHT)
    S_rotation = CircularLinkedList(UP, RIGHT, DOWN, LEFT)
    Si_rotation = CircularLinkedList(UP, LEFT, DOWN, RIGHT)

    def __init__(self, piecetype, pos):
        self.pos = pos
        self.colors = dict()
        self.numofsides = self.get_number_of_sides(piecetype)

    def get_number_of_sides(self, piecetype):

        if piecetype == self.CENTER:
            return 1
        elif piecetype == self.SIDE:
            return 2
        elif piecetype == self.EDGE:
            return 3
        else:
            return -1

    def set_color(self, color, direction):
        if len(self.colors.items()) < self.numofsides:
            if self.is_dupicate_color(color, direction) is False:
                self.colors[color] = direction
            else:
                raise ValueError("Duplicate color or direction found")

    def is_dupicate_color(self, color, direction):
        for k, v in self.colors.items():
            if (k == color) | (v == direction):
                return True
        return False

    def all_colors_are_set(self):
       return len(self.colors.items()) == self.numofsides

    def rotate(self, rotmatrix, rotationname):
        newpos = []
        for i in range(0, 3):
            newpos.append(self.vector_matrix_multiplication(self.pos, rotmatrix[i]))
        self.shift_piece_directions(rotationname)
        return newpos[0], newpos[1], newpos[2]

    def shift_piece_directions(self, rotationname):
        for k, v in self.colors.items():
            self.colors[k] = self.get_next_direction(rotationname, v)

    def get_next_direction(self, rotationname, curr_direction):
        if rotationname == "U":
            return self.U_rotation.findNext(curr_direction)
        elif rotationname == "Ui":
            return self.Ui_rotation.findNext(curr_direction)
        elif rotationname == "D":
            return self.D_rotation.findNext(curr_direction)
        elif rotationname == "Di":
            return self.Di_rotation.findNext(curr_direction)
        elif rotationname == "L":
            return self.L_rotation.findNext(curr_direction)
        elif rotationname == "Li":
            return self.Li_rotation.findNext(curr_direction)
        elif rotationname == "R":
            return self.R_rotation.findNext(curr_direction)
        elif rotationname == "Ri":
            return self.Ri_rotation.findNext(curr_direction)
        elif rotationname == "F":
            return self.F_rotation.findNext(curr_direction)
        elif rotationname == "Fi":
            return self.Fi_rotation.findNext(curr_direction)
        elif rotationname == "B":
            return self.B_rotation.findNext(curr_direction)
        elif rotationname == "Bi":
            return self.Bi_rotation.findNext(curr_direction)
        elif rotationname == "M":
            return self.M_rotation.findNext(curr_direction)
        elif rotationname == "Mi":
            return self.Mi_rotation.findNext(curr_direction)
        elif rotationname == "E":
            return self.E_rotation.findNext(curr_direction)
        elif rotationname == "Ei":
            return self.Ei_rotation.findNext(curr_direction)
        elif rotationname == "S":
            return self.S_rotation.findNext(curr_direction)
        elif rotationname == "Si":
            return self.Si_rotation.findNext(curr_direction)

    def vector_matrix_multiplication(self, vector, matrixcol):
        return vector[0] * matrixcol[0] + vector[1] * matrixcol[1] + vector[2] * matrixcol[2]



