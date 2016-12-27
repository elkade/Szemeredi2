from Window import Window
from time import sleep
class HumanPlayer(object):

    def __init__(self, code, window : Window = None):
        self.code = code
        self.window = window

    def mark(self, list):
        if self.window == None:
            return self.read_val('Mark a number: ')
        return self.read_window_val(list)

    def select(self, list):
        if self.window == None:
            return self.read_val('Select a number: ')
        return self.read_window_val(list)


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

    def read_window_vals(self, list):
        number = self.window.get_number()
        while number == None:
            number = self.window.get_number()
            sleep(0.05)
        return (number, number + 1)

    def read_window_val(self, list):
        number = self.window.get_number()
        while number == None:
            number = self.window.get_number()
            sleep(0.05)
        return number