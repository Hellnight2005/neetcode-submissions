from collections import defaultdict
# the collections is use for the default key has presnt in that
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)
        result = []

        for s in strs:
            sorted_s = tuple(sorted(s))
            # after sort each sorted_s look like this 
            # ('a', 'c', 't')

            anagram[sorted_s].append(s)
                    #    ('a', 'c', 't') ===> here the it he contained the word like cat and act 

        for val in anagram.values():
            result.append(val)      

        return result       