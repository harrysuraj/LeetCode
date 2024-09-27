class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        Closest=nums[0]
        for Random_number in nums:
            if abs(Random_number) <abs(Closest):
                Closest=Random_number
        if Closest<0 and abs(Closest) in nums:
            return abs(Closest)
        else:
            return Closest             
     