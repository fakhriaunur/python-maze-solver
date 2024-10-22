from cell import Cell
from graphics import Line, Point, Window
from maze import Maze

def main():
    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    maze._break_entrance_and_exit()
    # win = Window(800, 600)
    
    # p1 = Point(100, 100)
    # p2 = Point(500, 100)
    
    # line1 = Line(p1, p2)
    
    # # win.draw_line(line1, "red")
    
    # cell1 = Cell(win)
    # cell1.draw(100, 100, 500, 500)
    
    # cell2 = Cell(win)
    # cell2.draw(200, 200, 300, 300)
    
    # cell3 = Cell(win)
    # cell3.has_bottom_wall = False
    # cell3.draw(50, 50, 610, 610)
    
    # cell2.draw_move(cell1)
    
    # cell1.draw_move(cell3, True)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()