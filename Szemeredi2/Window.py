from tkinter import Tk, Frame, Button, Entry, Label
from threading import Thread
from time import sleep
from threading import Lock

class Window(Thread):
    def __init__(self, lock : Lock):
        self._input = None
        self._number = None
        self.lock = lock
        self.lock.acquire()
        Thread.__init__(self)
    def run(self):
        self.root = Tk()

        self.frame = Frame(self.root)
        self.frame.pack()

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
        self.frame.pack()
        if self.label != None:
            self.label.configure(text = label)
        input = self.validate(self._input)
        self._input = None
        if input != None:
            self.frame.pack_forget()
        self.lock.release()
        return input

    def get_number(self):
        number = self._number
        self._number = None
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