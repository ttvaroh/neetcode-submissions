class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupings = {}
        for s in strs:
            gen_s = "".join(sorted(s))
            if not groupings.get(gen_s):
                groupings[gen_s] = [s]
            else:
                groupings[gen_s].append(s)
        
        ret = []
        for key in groupings:
            ret.append(groupings[key])
        return ret