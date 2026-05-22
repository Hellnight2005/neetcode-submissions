class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = ""
        for char in s:
            if char.isalpha() or char.isdigit() is True:
                alpha +=char
        l,r = 0, len(alpha) -1
        while l<r:
            if alpha[l].lower() != alpha[r].lower():
                
                return False
            l,r=l+1,r-1
            
        return True


            

        
