from GameState import GameState
from Number import Number
from InvalidOperationException import InvalidOperationException
class Game(object):
    def __init__(self, finder):
        self.state = GameState.notStarted
        self.finder = finder
        pass
    
    def start_new(self, n, k):
        if k > n/2:
            raise InvalidOperationException("k cannot be greater than n/2.")
        self.k = k
        self.best = None
        self.state = GameState.player_a_marking
        self.list = []
        for x in range(1, n + 1):
            self.list.append(Number.empty)
            pass
        pass

    def mark(self, num1, num2, player_code):
        if num1 == num2:
            raise InvalidOperationException("Forbidden to mark two same numbers.")
        self.validate(num1)
        self.validate(num2)
        player_a_marking = self.state == GameState.player_a_marking and player_code == Number.selected_by_player_a
        playes_b_marking = self.state == GameState.player_b_marking and player_code == Number.selected_by_player_b
        if player_a_marking or playes_b_marking:
            if self.list[num1] == Number.empty and self.list[num2] == Number.empty:
                self.marked1 = num1
                self.marked2 = num2
                self.list[num1] = Number.marked
                self.list[num2] = Number.marked
                if player_a_marking:
                    self.state = GameState.player_b_selecting
                    pass
                else:
                    self.state = GameState.player_a_selecting
                    pass
                return
            raise InvalidOperationException("Cannot mark these numbers.")
        raise InvalidOperationException("Wrong player.")
        pass

    def select(self, num, player_code):
        self.validate(num)
        if self.list[num] != Number.marked:
            raise InvalidOperationException("Selected number is not marked.")
        player_a_selecting = self.state == GameState.player_a_selecting and player_code == Number.selected_by_player_a
        player_b_selecting = self.state == GameState.player_b_selecting and player_code == Number.selected_by_player_b

        self.list[self.marked1] = Number.empty
        self.list[self.marked2] = Number.empty

        if player_a_selecting:
            self.list[num] = Number.selected_by_player_a
            if self.is_finished(num):
                self.state = GameState.player_a_won
                return
            self.state = GameState.player_a_marking
            return
        if player_b_selecting:
            self.list[num] = Number.selected_by_player_b
            if self.is_finished(num):
                self.state = GameState.player_b_won
                return
            self.state = GameState.player_b_marking
            return
        raise InvalidOperationException("Move is forbidden now.")

    def is_finished(self, num):
        best_prog = self.finder.find(self.list, num, self.k)
        if len(best_prog) == self.k:
            self.best = best_prog
            return True
        return False

    def is_running(self):
        return self.state not in [GameState.player_a_won, GameState.player_b_won, GameState.draw]

    def validate(self, num):
        if num < 0 or num >= len(self.list):
            raise InvalidOperationException("Selected number is out of range.")
