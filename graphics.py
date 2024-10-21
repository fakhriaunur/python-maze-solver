from tkinter import Tk, BOTH, Canvas

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