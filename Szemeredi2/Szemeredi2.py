from GameMaster import GameMaster
from Game import Game
from LongestSubProgressionFinder import LongestSubProgressionFinder
from HumanPlayer import HumanPlayer
from colorama import init
from Number import Number
from ComputerPlayer import ComputerPlayer
init()


finder  = LongestSubProgressionFinder()
game = Game(finder)

human = HumanPlayer(Number.selected_by_player_a)
human = ComputerPlayer(finder, Number.selected_by_player_a)
computer = ComputerPlayer(finder, Number.selected_by_player_b)

game_master = GameMaster(human, computer)
game_master.play(game)
