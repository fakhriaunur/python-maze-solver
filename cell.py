
from graphics import Line, Point, Window


class Cell():
    def __init__(self, win: None | Window):
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_left_wall = True
        self.has_right_wall = True
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
            
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        
        bg_color = "white"
        
        top_line = Line(Point(x1, y1), Point(x2, y1))
        if self.has_top_wall:
            self._win.draw_line(top_line)
        else:
            self._win.draw_line(top_line, bg_color)
        
        bottom_line = Line(Point(x1, y2), Point(x2, y2))
        if self.has_bottom_wall:
            self._win.draw_line(bottom_line)
        else:
            self._win.draw_line(bottom_line, bg_color)
        
        left_line = Line(Point(x1, y1), Point(x1, y2))
        if self.has_left_wall:
            self._win.draw_line(left_line)
        else:
            self._win.draw_line(left_line, bg_color)
        
        right_line = Line(Point(x2, y1), Point(x2, y2))
        if self.has_right_wall:
            self._win.draw_line(right_line)
        else:
            self._win.draw_line(right_line, bg_color)
    
    def draw_move(self, to_cell, undo=False):
        fill_color = "gray" if undo else "red"
        x, y = self.__center_point()
        tc_x, tc_y = to_cell.__center_point()
        line = Line(Point(x, y), Point(tc_x, tc_y))
        self._win.draw_line(line, fill_color)
    
    def __center_point(self):
        mid_x = abs(self._x2 - self._x1) // 2 + self._x1
        mid_y = abs(self._y2 - self._y1) // 2 + self._y1
        return (mid_x, mid_y)