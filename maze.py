from time import sleep
from cell import Cell
from graphics import Window
from typing import List


class Maze():
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x,
        cell_size_y,
        win: None | Window
    ):
        self._cells: List[List[Cell]] = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        
        self._create_cells()
        self._break_entrance_and_exit()
    
    def _create_cells(self):
        for i in range(self.num_cols):
            cols: List[Cell] = []
            for j in range(self.num_rows):
                cell = Cell(self.win)
                cols.append(cell)
            self._cells.append(cols)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i: int, j: int):
        if self.win is None:
            return
        
        x1 = self.x1 + (i * self.cell_size_x)
        y1 = self.y1 + (j * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        
        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        
        self.win.redraw()
        sleep(0.05)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        bottom_right_x = self.num_cols - 1
        bottom_right_y = self.num_rows - 1
        self._cells[bottom_right_x][bottom_right_y].has_bottom_wall = False
        self._draw_cell(bottom_right_x, bottom_right_y)
        