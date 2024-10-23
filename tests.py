import unittest

from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    
    def test_maze_create_cells_large(self):
        num_cols = 16
        num_rows = 12
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        
        self.assertEqual(
            len(m1._cells),
            num_cols
        )
        
        self.assertEqual(
            len(m1._cells[0]),
            num_rows
        )
    
    def test_entrance_wall_removed(self):
        maze = Maze(0, 0, 10, 10, 10, 10)
        maze._break_entrance_and_exit()
        
        self.assertEqual(
            maze._cells[0][0].has_top_wall, False
        )
    
    def test_exit_wall_removed(self):
        maze = Maze(0, 0, 10, 10, 10, 10)
        maze._break_entrance_and_exit()
        
        self.assertEqual(
            maze._cells[-1][-1].has_bottom_wall, False
        )
    
    def test_other_walls_intact(self):
        maze = Maze(0, 0, 10, 10, 10, 10)
        maze._break_entrance_and_exit()
        
        self.assertEqual(
            maze._cells[0][0].has_right_wall, True
        )
        
        self.assertEqual(
            maze._cells[-1][-1].has_left_wall, True
        )

if __name__ == "__main__":
    unittest.main()