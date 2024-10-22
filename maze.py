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
        cell_size_x: int,
        cell_size_y: int,
        win: Window
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.__create_cells()
    
    def __create_cells(self):
        self.__cells: List[List[Cell]] = []
        for i in range(self.num_rows):
            rows: List[Cell] = []
            for j in range(self.num_cols):
                cell = Cell(self.win)
                rows.append(cell)
            self.__cells.append(rows)
        
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i: int, j: int):
        x1 = self.x1 + (j * self.cell_size_x)
        y1 = self.y1 + (i * self.cell_size_y)
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        
        cell = self.__cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self.__animate()
    
    def __animate(self):
        self.win.redraw()
        sleep(0.05)