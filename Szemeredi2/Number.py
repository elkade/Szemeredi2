from enum import Enum
class Number(object):
    empty = 0
    selected_by_player_a = 1,
    selected_by_player_b = 2,
    marked = 3
    def get_oponent_code(code):
        if code == Number.selected_by_player_a:
            return Number.selected_by_player_b
        if code == Number.selected_by_player_b:
            return Number.selected_by_player_a
        return code
