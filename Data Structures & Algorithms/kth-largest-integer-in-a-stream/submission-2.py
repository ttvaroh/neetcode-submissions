class KthLargest:
    def mergeSort(self, nums, l, r):
        if r == l:
            return [nums[r]]
        m = l + (r-l) // 2
        left = self.mergeSort(nums, l, m)
        right = self.mergeSort(nums, m+1, r)
        i = j = 0
        merged = []
        while i < len(left) and j < len(right):
            if left[i] < right[i]:
                merged.append(left[i])
                i+=1
            else:
                merged.append(right[j])
                j+=1
        while i < len(left):
            merged.append(left[i])
            i+=1
        while j < len(right):
            merged.append(right[j])
            j+=1
        return merged

    def __init__(self, k: int, nums: List[int]):
        self.nums = sorted(nums)
        # self.nums = self.mergeSort(nums, 0, len(nums)-1)
        self.k = k

    def add(self, val: int) -> int:
        i = 0
        while i < len(self.nums):
            if val < self.nums[i]:
                break
            i+=1
        self.nums.insert(i, val)
        return self.nums[-self.k]