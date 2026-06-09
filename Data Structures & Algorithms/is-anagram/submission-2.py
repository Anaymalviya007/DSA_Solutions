class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}

        for items_in_s in s:
            mapS[items_in_s] = mapS.get(items_in_s, 0) + 1
        for items_in_t in t:
            mapT[items_in_t] = mapT.get(items_in_t, 0) + 1

        return mapS == mapT