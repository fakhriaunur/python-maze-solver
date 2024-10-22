from graphics import Cell, Line, Point, Window

def main():
    win = Window(800, 600)
    
    p1 = Point(100, 100)
    p2 = Point(500, 100)
    
    line1 = Line(p1, p2)
    
    # win.draw_line(line1, "red")
    
    p3 = Point(100, 100)
    p4 = Point(500, 500)
    
    cell1 = Cell(p3, p4, win)
    cell1.draw()
    
    p5 = Point(200, 200)
    p6 = Point(300, 300)
    
    cell2 = Cell(p5, p6, win)
    cell2.draw()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()