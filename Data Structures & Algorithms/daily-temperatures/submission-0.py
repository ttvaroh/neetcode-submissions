class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while tempStack and temperatures[i] > temperatures[tempStack[-1]]:
                result[tempStack[-1]] = i - tempStack[-1]
                del tempStack[-1]
            tempStack.append(i)
        return result