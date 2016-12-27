from Game import Game
from LongestSubProgressionFinder import LongestSubProgressionFinder
from HumanPlayer import HumanPlayer
from Number import Number
from ComputerPlayer import ComputerPlayer
from GuiHandler import GuiHandler
from CliHandler import CliHandler

class Program(object):
    def start(interfaceHandler):
        finder  = LongestSubProgressionFinder()
        game = Game(finder)

        human = HumanPlayer(Number.selected_by_player_a, interfaceHandler.window)
        #human = ComputerPlayer(finder, Number.selected_by_player_a)
        computer = ComputerPlayer(finder, Number.selected_by_player_b)

        interfaceHandler.run(game, human, computer)
