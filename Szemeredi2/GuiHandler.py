from tkinter import *
from Game import Game
from Number import Number
from GameState import GameState
from Window import Window
from time import sleep
from InvalidOperationException import InvalidOperationException

class GuiHandler(object):
    def __init__(self, window:Window):
        self.window = window

    def run(self, game : Game, player_1, player_2):
        self.game = game
        
        self.marked = None

        while game.get_state() == GameState.notStarted:
            try:
                n = self.get_input('n: ')
                k = self.get_input('k: ')
        
                game.start_new(n, k)
            except InvalidOperationException as ex:
                print(ex.args)
        self.buttons = [self.create_button(x) for x in range(n)]

        self.frame = Frame(self.root)
        self.frame.pack()        
        self.root.mainloop()

    def get_input(self, str):
        input = self.window.get_input(str)
        while input == None:
            input = self.window.get_input(str)
            sleep(0.05)
        return input

    def create_button(self, num):
        button = Button(self.root, text = str(num), command = lambda: self.pressed(button, num, Number.empty))
        button.pack(pady = 3, padx = 3)
        return button

    def pressed(self, button, number, value):
        if(self.game.get_state() == GameState.player_a_marking):
            button.configure(bg = "YELLOW")
            #button.configure(state = "disabled")
            if self.marked == None:
                self.marked = number
            elif number != self.marked:
                self.game.mark(number, self.marked, Number.selected_by_player_a)
                self.marked = None
        elif(self.game.get_state() == GameState.player_b_marking):
            button.configure(bg = "YELLOW")
            #button.configure(state = "disabled")
            if self.marked == None:
                self.marked = number
            elif number != self.marked:
                self.game.mark(number, self.marked, Number.selected_by_player_b)
                self.marked = None


class takeInput(object):

    def __init__(self,requestMessage):
        self.root = Tk()
        self.string = ''
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.acceptInput(requestMessage)

    def acceptInput(self,requestMessage):
        r = self.frame

        k = Label(r,text=requestMessage)
        k.pack(side='left')
        self.e = Entry(r,text='Name')
        self.e.pack(side='left')
        self.e.focus_set()
        b = Button(r,text='okay',command=self.gettext)
        b.pack(side='right')

    def gettext(self):
        self.string = self.e.get()
        self.root.destroy()

    def getString(self):
        return self.string

    def waitForInput(self):
        self.root.mainloop()