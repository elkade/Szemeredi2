from enum import Enum
class GameState(Enum):
    notStarted = 0
    player_a_marking = 1
    player_b_marking = 2
    player_a_selecting = 3
    player_b_selecting = 4
    player_a_won = 5
    player_b_won = 6
    draw = 7


