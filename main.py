from graphics import Line, Point, Window

def main():
    win = Window(800, 600)
    
    p1 = Point(100, 100)
    p2 = Point(500, 100)
    
    win.draw_line(Line(p1, p2), "red")
    
    win.wait_for_close()

if __name__ == "__main__":
    main()