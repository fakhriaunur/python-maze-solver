from graphics import Line, Point, Window

def main():
    win = Window(800, 600)
    
    p1 = Point(100, 100)
    p2 = Point(500, 100)
    
    line1 = Line(p1, p2)
    
    win.draw_line(line1, "red")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()