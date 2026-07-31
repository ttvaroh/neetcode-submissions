class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        buckets = [[] for i in range(len(nums) + 1)]
        for num in nums:
            hmap[num] = hmap.get(num, 0) + 1

        for key in hmap:
            buckets[hmap[key]].append(key)
        
        ans = []
        i = len(buckets) - 1
        while (len(ans) < k and i > 0):
            while (len(ans) < k and len(buckets[i]) > 0):
                nextk = buckets[i].pop(len(buckets[i]) - 1)
                ans.append(nextk)
            i-=1
        return ans


