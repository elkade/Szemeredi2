from Game import Game
from GameState import GameState
from Number import Number
from PlayerCode import PlayerCode
from colorama import Fore, Back, Style
from InvalidOperationException import InvalidOperationException
class GameMaster(object):
    
    def __init__(self, human, computer):
        self.human = human
        self.computer = computer
        pass

    def play(self, game : Game):
        n = self.read_val('n: ')
        k = self.read_val('k: ')

        game.start_new(n, k)

        self.print_numbers(game.list)

        player_1 = self.human
        player_2 = self.computer
        player_1.code = PlayerCode.player_a
        player_2.code = PlayerCode.player_b

        while game.is_running():
            self.mark(game, player_1)
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
        print("Progression:")
        for x in game.best:
            print(str(x), end=" ")
            pass
        print()
        pass

    def select(self, game, player):
        move_succeeded = False
        while not move_succeeded:
            try:
                num = player.select()
                game.select(num, player.code)
                self.print_numbers(game.list)
                move_succeeded = True
                pass
            except InvalidOperationException as ex:
                print(ex.args)
                move_succeeded = False
            pass
        pass
    def mark(self, game, player):
        move_succeeded = False
        while not move_succeeded:
            try:
                (num1, num2) = player.mark()
                game.mark(num1, num2, player.code)
                self.print_numbers(game.list)
                move_succeeded = True
                pass
            except InvalidOperationException as ex:
                print(ex.args)
                move_succeeded = False
            pass
        pass
    def print_numbers(self, list):
        cols = {
            Number.empty: Fore.WHITE,
            Number.marked: Fore.YELLOW,
            Number.selected_by_player_a: Fore.GREEN,
            Number.selected_by_player_b: Fore.RED
            }
        i = 0
        for x in list:
            print(cols[x] + str(i), end=" ")
            i+=1
            pass
        print(Fore.WHITE)

    def read_val(self, str):
        num = None
        while num == None:
            try:
                num = int(input(str))
            except ValueError:
                pass
            pass
        return num
