from enum import Enum
class GameState(Enum):
    notStarted = 0
    player_a_marking1 = 1
    player_b_marking1 = 2
    player_a_marking2 = 3
    player_b_marking2 = 4
    player_a_selecting = 5
    player_b_selecting = 6
    player_a_won = 7
    player_b_won = 8
    draw = 9


