class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter={}
        result=[]
        for n in nums:
            if n in counter:
                counter[n]+=1
            else:
                counter[n]=1
        sorterd_counter =sorted(counter.items(), key=lambda x: x[1], reverse=True)
        # print(sorterd_counter)
        for n,count in sorterd_counter[:k]:
            result.append(n)
        return result 


