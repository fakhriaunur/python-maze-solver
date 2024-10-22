from cell import Cell
from graphics import Line, Point, Window

def main():
    win = Window(800, 600)
    
    p1 = Point(100, 100)
    p2 = Point(500, 100)
    
    line1 = Line(p1, p2)
    
    # win.draw_line(line1, "red")
    
    cell1 = Cell(win)
    cell1.draw(100, 100, 500, 500)
    
    cell2 = Cell(win)
    cell2.draw(200, 200, 300, 300)
    
    cell3 = Cell(win)
    cell3.has_bottom_wall = False
    cell3.draw(50, 50, 610, 610)
    
    win.wait_for_close()

if __name__ == "__main__":
    main()