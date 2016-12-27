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

    def run(self, game : Game, player_a, player_b):
        self.game = game
        self.marked = None
        ans = 'y'
        while ans=='y':
            while game.get_state() == GameState.notStarted:
                try:
                    n = self.get_input('n: ')
                    k = self.get_input('k: ')
        
                    game.start_new(n, k)
                except InvalidOperationException as ex:
                    print(ex.args)

            self.print_numbers(game.get_list())

            player_1, player_2 = player_a, player_b

            while game.is_running():
                self.mark1(game, player_1)
                self.mark2(game, player_1)
                self.select(game, player_2)
                (player_1, player_2) = (player_2, player_1)
                pass

            if game.state == GameState.player_a_won:
                print('Human wins!')
                pass
            elif game.state == GameState.player_b_won:
                print('Computer wins!')
                pass
            else:
                print('Draw! No more moves.')
                pass
            if game.state != GameState.draw:
                print("Progression:")
                for x in game.best:
                    print(str(x), end=" ")
                    pass
                print()
            self.clear()
            game.end()
            ans = input('once again? [y/n]: ')
        self.window.destroy()
        pass
    def mark1(self, game, player):
        move_succeeded = False
        while not move_succeeded:
            try:
                num = player.mark(game.get_list())
                game.mark1(num, player.code)
                self.print_numbers(game.get_list())
                move_succeeded = True
                pass
            except InvalidOperationException as ex:
                print(ex.args)
                move_succeeded = False
            pass
        pass
    def mark2(self, game, player):
        move_succeeded = False
        while not move_succeeded:
            try:
                num = player.mark(game.get_list())
                game.mark2(num, player.code)
                self.print_numbers(game.get_list())
                move_succeeded = True
                pass
            except InvalidOperationException as ex:
                print(ex.args)
                move_succeeded = False
            pass
        pass
    def select(self, game, player):
        move_succeeded = False
        while not move_succeeded:
            try:
                num = player.select(game.get_list())
                game.select(num, player.code)
                self.print_numbers(game.get_list())
                move_succeeded = True
                pass
            except InvalidOperationException as ex:
                print(ex.args)
                move_succeeded = False
            pass
        pass

    def get_input(self, str):
        input = self.window.get_input(str)
        while input == None:
            input = self.window.get_input(str)
            sleep(0.05)
        return input

    def print_numbers(self, numbers):
        self.window.update_buttons(numbers)

    def clear(self):
        self.window.clear()
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