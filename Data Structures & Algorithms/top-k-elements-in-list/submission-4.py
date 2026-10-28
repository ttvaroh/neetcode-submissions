class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        count_arr = sorted(count, key=count.get)

        return count_arr[-k:]