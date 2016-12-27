from Game import Game
from GameState import GameState
from Number import Number
from colorama import Fore, Back, Style, init
from InvalidOperationException import InvalidOperationException
class CliHandler(object):
    def __init__(self, **kwargs):
         self.window = None
    def run(self, game : Game, player_1, player_2):
        init()
        ans = 'y'
        while ans=='y':
            while game.get_state() == GameState.notStarted:
                try:
                    n = self.read_val('n: ')
                    k = self.read_val('k: ')
                    game.start_new(n, k)
                except InvalidOperationException as ex:
                    print(ex.args)

            self.print_numbers(game.get_list())

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
            game.end()
            ans = input('once again? [y/n]: ')
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
            except Exception as ex:
                print(ex.args)
            pass
        return num
