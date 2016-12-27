from GameState import GameState
from Number import Number
from InvalidOperationException import InvalidOperationException
class Game(object):
    def __init__(self, finder):
        self.state = GameState.notStarted
        self.finder = finder
        pass
    
    def start_new(self, n, k):
        if n < 2:
            raise InvalidOperationException("n cannot be lower than 2.")
        if k > n/2:
            raise InvalidOperationException("k cannot be greater than n/2.")
        self.k = k
        self.best = None
        self.state = GameState.player_a_marking1
        self.list = []
        for x in range(1, n + 1):
            self.list.append(Number.empty)
            pass
        pass

    def mark1(self, num, player_code):
        self.validate(num)
        player_a_marking = self.state == GameState.player_a_marking1 and player_code == Number.selected_by_player_a
        playes_b_marking = self.state == GameState.player_b_marking1 and player_code == Number.selected_by_player_b
        if player_a_marking or playes_b_marking:
            if self.list[num] == Number.empty:
                self.marked1 = num
                self.list[num] = Number.marked
                if player_a_marking:
                    self.state = GameState.player_a_marking2
                    pass
                else:
                    self.state = GameState.player_b_marking2
                    pass
                return
            raise InvalidOperationException("Cannot mark this number.")
        raise InvalidOperationException("Wrong player.")
        pass

    def mark2(self, num, player_code):
        if num == self.marked1:
            raise InvalidOperationException("Forbidden to mark two same numbers.")
        self.validate(num)
        player_a_marking = self.state == GameState.player_a_marking2 and player_code == Number.selected_by_player_a
        playes_b_marking = self.state == GameState.player_b_marking2 and player_code == Number.selected_by_player_b
        if player_a_marking or playes_b_marking:
            if self.list[num] == Number.empty:
                self.marked2 = num
                self.list[num] = Number.marked
                if player_a_marking:
                    self.state = GameState.player_b_selecting
                    pass
                else:
                    self.state = GameState.player_a_selecting
                    pass
                return
            raise InvalidOperationException("Cannot mark this number.")
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
            if(self.is_draw()):
                self.state = GameState.draw
                return
            self.state = GameState.player_a_marking1
            return
        if player_b_selecting:
            self.list[num] = Number.selected_by_player_b
            if self.is_finished(num):
                self.state = GameState.player_b_won
                return
            if(self.is_draw()):
                self.state = GameState.draw
                return
            self.state = GameState.player_b_marking1
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
        pass
    def is_draw(self):
        free_slots = [x for x in self.list if x == Number.empty]
        return len(free_slots) < 2
    def get_list(self):
        return list(self.list)

    def get_state(self):
        return self.state
    def end(self):
        self.state = GameState.notStarted