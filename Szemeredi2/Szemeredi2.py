from GameMaster import GameMaster
from Game import Game
from LongestSubProgressionFinder import LongestSubProgressionFinder
from HumanPlayer import HumanPlayer
from PlayerCode import PlayerCode
from colorama import init
init()


finder  = LongestSubProgressionFinder()
game = Game(finder)

human = HumanPlayer()
computer = HumanPlayer()

game_master = GameMaster(human, computer)
game_master.play(game)

#TODO: obs�u�y� remis - brak ruchu