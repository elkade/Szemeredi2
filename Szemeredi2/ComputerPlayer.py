from LongestSubProgressionFinder import LongestSubProgressionFinder
from Number import Number
class ComputerPlayer(object):

    def __init__(self, finder: LongestSubProgressionFinder, code):
        self.finder = finder
        self.code = code

    def mark(self, list):
        print("Computer marked:", end=' ')
        ind1 = self.find_best_marking(list)
        ind2 = self.find_best_marking(list,  ind1)
        print(str(ind1) + ' ' + str(ind2))
        return (ind1, ind2)

    def select(self, list):
        print("Computer selected:", end=' ')
        max = -1
        ind = -1
        for i in range(0, len(list)):
            if list[i] != Number.marked:
                continue
            list[i] = self.code
            l = len(self.finder.find(list, i))
            if l > max:
                max, ind = l, i
            list[i] = Number.marked
            pass
        print(str(ind))
        return ind

    def find_best_marking(self, list, bestInd = None):
        min = len(list)
        ind = -1
        for i in range(0, len(list)):
            if list[i] != Number.empty:
                continue
            if(i == bestInd):
                continue
            list[i] = Number.get_oponent_code(self.code)
            l = len(self.finder.find(list, i))
            if l < min:
                min, ind = l, i
            list[i] = Number.empty
        return ind