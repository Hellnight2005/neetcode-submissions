class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        print(sorted_nums)
        count = 1
        maxcount =1
        for i in range(len(sorted_nums)-1):
            
            print(i)
            if sorted_nums[i] - sorted_nums[i+1] == -1 :
                count+=1
            else :
                count =1
            maxcount = max(count , maxcount)
        return maxcount


