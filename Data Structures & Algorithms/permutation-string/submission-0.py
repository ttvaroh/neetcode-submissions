class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        if size > len(s2): return False
        main = defaultdict(int)
        test = defaultdict(int)

        for i in range(size):
            main[s1[i]] += 1
            test[s2[i]] += 1
        if main == test: return True

        for r in range(size, len(s2)):
            test[s2[r]] += 1
            if test[s2[r-size]] == 1:
                test.pop(s2[r-size])
            else:
                test[s2[r-size]] -= 1
            
            if main == test: return True
        
        return False
        
