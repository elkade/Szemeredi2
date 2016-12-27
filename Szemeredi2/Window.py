from tkinter import Tk, Frame, Button, Entry, Label
from threading import Thread
from time import sleep
from threading import Lock
from Number import Number

class Window(Thread):
    def __init__(self, lock : Lock):
        self._input = None
        self._number = None
        self.buttons = None
        self.lock = lock
        self.lock.acquire()
        Thread.__init__(self)
    def run(self):
        self.root = Tk()

        self.frame = Frame(self.root)
        self.frames = []

        self.label = Label(self.frame)
        self.label.pack(side='left')

        self.entry = Entry(self.frame, text='Name')
        self.entry.pack(side='left')
        self.entry.focus_set()

        self.button = Button(self.frame, text='Submit', command = self.set_input)
        self.button.pack(side='right')
        self.lock.release()
        self.root.mainloop()

    def get_input(self, label):
        self.lock.acquire()
        self.frame.pack(side='left')
        if self.label != None:
            self.label.configure(text = label)
        input = self.validate(self._input)
        self._input = None
        if input != None:
            self.frame.pack_forget()
        self.lock.release()
        return input

    def update_buttons(self, list):
        self.lock.acquire()
        if self.buttons == None:
            self.buttons = [self.create_button(x) for x in range(len(list))]
        else:
            for i in range(len(list)):
                val = list[i]
                button = self.buttons[i]
                if val == Number.empty:
                    button.configure(bg = "WHITE")
                elif val == Number.marked:
                    button.configure(bg = "YELLOW")
                elif val == Number.selected_by_player_a:
                    button.configure(bg = "GREEN")
                elif val == Number.selected_by_player_b:
                    button.configure(bg = "RED")
        self.lock.release()

    def create_button(self, num):
        i = num % 30
        if i == 0:
            self.frames.append(Frame(self.root))
            self.frames[-1].pack(side='top')
        button = Button(self.frames[-1], text = str(num), command = lambda: self.set_number(button, num),  height = 2, width = 4)
        button.pack(side='left', pady = 3, padx = 3)
        button.configure(bg = "WHITE")
        return button

    def set_number(self, button, number):
        self._number = number

    def get_number(self):
        self.lock.acquire()
        number = self._number
        self._number = None
        self.lock.release()
        return number

    def set_input(self):
        self._input = self.entry.get()
        self.entry.delete(0, 'end')

    def validate(self, str):
        if str == None:
            return None
        try:
            output = int(str)
        except Exception as ex:
            print(ex.args)
            return None
        return output

    def clear(self):
        self.lock.acquire()
        for frame in self.frames:
            frame.pack_forget()
        self.frames = []
        for button in self.buttons:
            button.pack_forget()
        self.buttons = None
        self.lock.release()
    def destroy(self):
        self.root.quit()