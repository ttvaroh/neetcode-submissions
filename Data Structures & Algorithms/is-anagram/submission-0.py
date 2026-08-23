class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        smap = {}
        tmap = {}

        for c in s:
            smap[c] = smap.get(c, 0) + 1
        for c in t:
            tmap[c] = tmap.get(c, 0) + 1

        for key in smap:
            if smap[key] != tmap.get(key,0):
                return False
            tmap.pop(key, None)
        
        return len(tmap) == 0