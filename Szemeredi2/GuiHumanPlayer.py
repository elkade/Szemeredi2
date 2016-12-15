from tkinter import Tk
from Window import Window
class GuiPlayer(object):

    def __init__(self, code, window : Window):
        self.code = code
        self.window = window

    def mark(self, list):
        return self.read_vals('Mark two numbers: ')

    def select(self, list):
        self.window.mainloop()

    def read_vals(self, str):
        (num1, num2) = (None, None)
        while num1 == None or num2 == None:
            try:
                (num1, num2) = input(str).split()
                (num1, num2) = int(num1), int(num2)
            except ValueError:
                pass
            pass
        return (num1, num2)

    def read_val(self, str):
        num = None
        while num == None:
            try:
                num = int(input(str))
            except ValueError:
                pass
            pass
        return num