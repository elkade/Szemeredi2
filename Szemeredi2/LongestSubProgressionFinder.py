class LongestSubProgressionFinder(object):
    
    def find(self, list, num, k = None):
        val = list[num]
        n = len(list)
        if k == None:
            k = n
            pass
        best = [num]
        for step in range(1, n):
            count = 0
            start = num
            end = num
            for i in range(num, -1, -step):
                if list[i] == val:
                    start = i
                    count+=1
                    if count == k:
                        return range(start, num + step, step)
                    pass
                else:
                    break
            for i in range(num + step, n, step):
                if list[i] == val:
                    end = i
                    count+=1
                    if count == k:
                        return range(start, end + step, step)
                    pass
                else:
                    break
            if count > len(best):
                best = range(start, end + step, step)
            pass
        return best


