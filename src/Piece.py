
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
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
            temp.next = ptr1

        else:
            ptr1.next = ptr1  # For the first node

        self.head = ptr1


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

    U_directions = CircularLinkedList(FRONT, LEFT, BACK, RIGHT)
    Ui_directions = CircularLinkedList(FRONT, RIGHT, BACK, LEFT)
    D_directions = CircularLinkedList(FRONT, RIGHT, BACK, LEFT)
    Di_directions = CircularLinkedList(FRONT, LEFT, BACK, RIGHT)
    L_directions = CircularLinkedList(UP, FRONT, DOWN, BACK)
    Li_directions = CircularLinkedList(UP, BACK, DOWN, FRONT)
    R_directions = CircularLinkedList(UP, BACK, DOWN, FRONT)
    Ri_directions = CircularLinkedList(UP, FRONT, DOWN, BACK)
    F_directions = CircularLinkedList(UP, RIGHT, DOWN, LEFT)
    Fi_directions = CircularLinkedList(UP, LEFT, DOWN, RIGHT)
    B_directions = CircularLinkedList(UP, LEFT, DOWN, RIGHT)
    Bi_directions = CircularLinkedList(UP, RIGHT, DOWN, LEFT)

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

    def rotate(self, rotmatrix):
        newpos = []
        for i in range(0, 3):
            newpos.append(self.vector_multiplication(self.pos, rotmatrix[i]))
        return newpos[0], newpos[1], newpos[2]

    def vector_multiplication(self, vector1, vector2):
        sum = 0
        for i in range(0, 3):
            sum += vector1[i] * vector2[i]
        return sum



