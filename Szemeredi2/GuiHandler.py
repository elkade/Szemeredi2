from tkinter import *
from Game import Game

class GuiHandler(object):

    def run(self, game : Game, player_1, player_2):
        self.game = game

        n = self.getInput('n: ')
        k = self.getInput('k: ')
        
        game.start_new(n, k)

        self.root = Tk()

        self.button = Button(self.root, text = 'Press', command = lambda: GuiHandler.Pressed(button, 'siema'))
        self.button.pack(pady = 20, padx = 20)
        self.string = ''
        self.frame = Frame(self.root)
        self.frame.pack()        
        self.acceptInput("abc")
        self.root.mainloop()


    def getInput(self, str):
        msgBox = takeInput(str)
        msgBox.waitForInput()
        return int(msgBox.getString())
    def acceptInput(self, str):
        r = self.frame
        k = Label(r,text=str)
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

    def Pressed(button, text):
        button['state'] = 'disabled'
        print('buttons are cool. ' + text)

    def read_val(self, str):
        self.waitForInput()
        return int(self.getString())


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