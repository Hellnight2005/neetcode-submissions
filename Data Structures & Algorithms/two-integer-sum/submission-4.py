
# first i use the burateforce metod and have problem 
#  for i in range(len(nums)) :
#             for j in  range(len(nums)):
#                 if nums[i]+nums[j]==target:

#                     return [i,j]

# as the i and j are start from zero index as the it match the both number like 
# imput =[ 5,5,4,8]
# target = 5
# output [0,1] means first inde and second

# but burateforce it will return the [0,0] the first i and j both are compare
# same element so it effect the same value approch 

# After solution
# no i see the solution it use the hashmap 

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = { }  # val : index 
        for i , n in enumerate(nums): #enumerate it return both [index : values]
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff] , i]
            prevMap[n] = i 

       
        