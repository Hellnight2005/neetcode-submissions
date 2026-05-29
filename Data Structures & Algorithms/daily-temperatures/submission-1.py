class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output =[0]*len(temperatures)
        stack =[]
        
        
        for Index,temp  in enumerate(temperatures):
            
            while stack  and  temp >stack[-1][0]:
                
                stackTemp,stackindex = stack.pop()
                
                
                output[stackindex] = (Index - stackindex)
            stack.append([temp,Index])
        
        return output
        

