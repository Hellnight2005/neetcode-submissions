class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position , speed)]
        fleets = 0
        slowest = 0.0

        for p,s in sorted(pair)[::-1]:
            time = (target-p )/s 
            
            if time > slowest:
                fleets +=1
                slowest = time
        return fleets