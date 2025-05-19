from point import Point
from line import Line


class Cell:
    def __init__(self, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = window

    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "white")
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "white")
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "white")
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "white")
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        midx1 = (self._x1 + self._x2) / 2
        midy1 = (self._y1 + self._y2) / 2
        midx2 = (to_cell._x1 + to_cell._x2) / 2
        midy2 = (to_cell._y1 + to_cell._y2) / 2
        if undo:
            color = "red"
        else:
            color = "gray"
        self._win.draw_line(Line(Point(midx1, midy1), Point(midx2, midy2)), color)
