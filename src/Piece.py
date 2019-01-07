

CENTER = "center"
SIDE = "side"
EDGE = "edge"

class Piece:

    def __init__(self, piecetype, pos):
        self.piecetype = piecetype
        self.pos = pos
        self.piececolors = [None for _ in range(self.getnumberofsides(self.piecetype))]

    def getnumberofsides(self, piecetype):

        if piecetype == CENTER:
            return 1
        elif piecetype == SIDE:
            return 2
        elif piecetype == EDGE:
            return 3
        else:
            return -1

    def set_color(self, color, direction):
        for i in range(len(self.piececolors)):
            if self.piececolors[i] is None:
                self.piececolors[i] = (color, direction)
                return

    def all_colors_are_set(self):
        return not(None in self.piececolors)


