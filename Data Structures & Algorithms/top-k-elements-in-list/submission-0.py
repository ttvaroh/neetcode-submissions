class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}

        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        numsSorted = sorted(hmap.items(), reverse=True, key=lambda item:item[1])
        ans = []
        for i in range(k):
            ans.append(numsSorted[i][0])

        return ans