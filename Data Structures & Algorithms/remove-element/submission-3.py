class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        c = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[l], nums[r] = nums[r], nums[l]
                c+=1
                l+=1
        return c