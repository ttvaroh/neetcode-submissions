class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        seen = []
        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while len(seen) > 0 and temperatures[i] > temperatures[seen[-1]]:
                result[seen[-1]] = i - seen[-1]
                seen.pop()
            seen.append(i)
        return result