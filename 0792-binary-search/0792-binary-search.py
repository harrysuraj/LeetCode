class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low=0  # The first element in binary search
        high=len(nums)-1 #the last element in binary search
        while low<=high: 
            mid=(low+high)//2 #takling the middle element(its percentiles value)
            if nums[mid]==target: #here we are accessing middle element from nums so no()
                return mid
            elif nums[mid]>target:#if middle is greater than the target is between left&mid
                high=mid-1     # here we move the right pointer one beside the mid 
            elif nums[mid]<target:                
                low=mid+1       # low pointer is shifted to right side of mid
        return -1 # the element doesnt exist in the list        


        