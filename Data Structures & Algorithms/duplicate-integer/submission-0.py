class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        prevmap = {}
        result = False
        for i , n in enumerate(nums):
            if n in prevmap:
                result = True
            else:
                prevmap[n]=i
        print(prevmap)
        print(result)
        return result 