class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        l,r = 0 ,len(numbers)-1
        print(l, r)
        while l<r:
            for num in numbers:
                
                number = numbers[l]+numbers[r]
                if number > target:
                    r-=1
                elif number < target:
                    l+=1
                else :
                    return ([l+1,r+1])
                
        
        
            