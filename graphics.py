from tkinter import Tk, BOTH, Canvas

class Point():
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

class Line():
    def __init__(self, p1: Point, p2: Point):
        # self.line = Point(p1.x, p2.y)
        self.p1 = p1
        self.p2 = p2
    
    def draw(self, canvas: Canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
    
class Window():
    def __init__(self, width: int, height: int):
        self.__root_widget = Tk()
        self.__root_widget.title("Maze Solver")
        self.__canvas = Canvas(
            self.__root_widget, bg="white", height=height, width=width
        )
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__is_running = False
        self.__root_widget.protocol("WM_DELETE_WINDOW", self.close)
    
    def redraw(self):
        self.__root_widget.update_idletasks()
        self.__root_widget.update()
    
    def wait_for_close(self):
        self.__is_running = True
        while self.__is_running:
            self.redraw()
        print("window closed...")
    
    def close(self):
        self.__is_running = False
    
    def draw_line(self, line: Line, fill_color="black"):
        line.draw(self.__canvas, fill_color)
