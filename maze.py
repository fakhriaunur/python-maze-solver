from time import sleep
import time
from cell import Cell
from graphics import Window
from typing import List, Optional
from collections import deque
import random


class Maze():
    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int | float,
        cell_size_y: int | float,
        win: Optional[Window] = None,
        seed: int | float | str | bytes| bytearray | None = None
    ):
        self._cells: List[List[Cell]] = []
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        if seed is not None:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for i in range(self._num_cols):
            cols: List[Cell] = []
            for j in range(self._num_rows):
                cell = Cell(self._win)
                cols.append(cell)
            self._cells.append(cols)
        
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i: int, j: int):
        if self._win is None:
            return
        
        x1 = self._x1 + (i * self._cell_size_x)
        y1 = self._y1 + (j * self._cell_size_y)
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y
        
        cell = self._cells[i][j]
        cell.draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        
        self._win.redraw()
        sleep(0.01)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        
        bottom_right_x = self._num_cols - 1
        bottom_right_y = self._num_rows - 1
        self._cells[bottom_right_x][bottom_right_y].has_bottom_wall = False
        self._draw_cell(bottom_right_x, bottom_right_y)
    
    def _break_walls_in_between(self, i: int, j: int, di: int, dj: int):
        # moving right
        if di == 1:
            self._cells[i][j].has_right_wall = False
            self._cells[i + 1][dj].has_left_wall = False
        # moving left
        elif di == -1:
            self._cells[i][j].has_left_wall = False
            self._cells[i - 1][j].has_right_wall = False
        # moving down
        elif dj == 1:
            self._cells[i][j].has_bottom_wall = False
            self._cells[i][j + 1].has_top_wall = False
        # moving up
        elif dj == -1:
            self._cells[i][j].has_top_wall = False
            self._cells[i][j - 1].has_bottom_wall = False
    
    def _break_walls_r(self, i: int, j: int):
        # mark current cell as visited
        self._cells[i][j].visited = True
        
        # infinite loop
        while True:
            # list to hold possible visits
            possible_visits = []
            possible_dirs = [
                (0, 1), (1, 0), (0, -1), (-1, 0)
            ]
            
            for di, dj in possible_dirs:
                ni, nj = i + di, j + dj
                #maze boundary check
                if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows:
                    # check if visited
                    if not self._cells[ni][nj].visited:
                        # add to possible visits
                        possible_visits.append((ni, nj))
            
            # check if no possible visits
            if not possible_visits:
                self._draw_cell(i, j)
                return # backtrack
            
            # choose random direction
            chosen_i, chosen_j = possible_visits[random.randrange(len(possible_visits))]
            
            # breaking walls
            di = chosen_i - i
            dj = chosen_j - j
            self._break_walls_in_between(i, j, di, dj)
            
            # recurse the next visits
            # print(f"possible visits: {possible_visits}")
            self._break_walls_r(chosen_i, chosen_j)

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False
    
    def solve(self):
        time_start = time.time()
        result = self._solve_r(0, 0)
        # result = self._solve_bfs(0, 0)
        time_end = time.time()
        print(f"result: {result}, within {time_end - time_start}sec")
        return result
    
    def _solve_bfs(self, i: int, j: int):
        queue = deque([(i, j)])
        visited = set()
        visited.add((i, j))
        
        while queue:
            self._animate()
            
            x, y = queue.popleft()
            
            if self._is_end(x, y):
                return True
            
            # cols, rows = len(self._cells), len(self._cells[0])
            for nx, ny in self._get_neighbors(x, y):
                if (nx, ny) not in visited:
                    curr_cell = self._cells[x][y]
                    to_cell = self._cells[nx][ny]
                    curr_cell.draw_move(to_cell)
                    visited.add((nx, ny))
                    queue.append((nx, ny))
        
        return False
        
    def _solve_r(self, i: int, j: int):
        self._animate()
        self._cells[i][j].visited = True
        
        if self._is_end(i, j):
            return True
        
        # cols, rows = len(self._cells), len(self._cells[0])
        for ni, nj in self._get_neighbors(i, j):
            if not self._cells[ni][nj].visited:
                curr_cell = self._cells[i][j]
                to_cell = self._cells[ni][nj]
                curr_cell.draw_move(to_cell)
                if self._solve_r(ni, nj):
                    return True
        
        return False
    
    def _is_end(self, i: int,j: int):
        last_col = self._num_cols - 1
        last_row = self._num_rows - 1
        return (i, j) == (last_col, last_row)
    
    def _is_blocked(self, i: int, j: int, direction):
        curr_cell = self._cells[i][j]
        
        if direction == "top":
            return curr_cell.has_top_wall
        elif direction == "bottom":
            return curr_cell.has_bottom_wall
        elif direction == "left":
            return curr_cell.has_left_wall
        elif direction == "right":
            return curr_cell.has_right_wall
        
        return True
    
    def _get_neighbors(self, i: int, j: int):
        directions = {
            "right": (1, 0),
            "bottom": (0, 1),
            "left": (-1, 0),
            "top": (0, -1)
        }
        neighbors = []
        
        for direction, (di, dj) in directions.items():
            ni, nj = i + di, j + dj
            if 0 <= ni < self._num_cols and 0 <= nj < self._num_rows:
                # curr_cell = self._cells[i][j]
                if not self._is_blocked(i, j, direction):
                    neighbors.append((ni, nj))
        
        return neighbors
            