class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.nums):
            if val < self.nums[i]:
                break
            i+=1
        self.nums.insert(i, val)
        return self.nums[-self.k]