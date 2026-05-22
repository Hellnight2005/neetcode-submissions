from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Map = defaultdict(list)
        M = [s,t]
        for s in M :
            sorted_m = tuple(sorted(s))
            if sorted_m in Map:
                return True 
            # print(sorted_m)
            # print(Map)
            Map[sorted_m].append(s)
        return False