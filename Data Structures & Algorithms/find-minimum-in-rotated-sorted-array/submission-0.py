class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val=float('inf')
        for i in range(len(nums)):
            if nums[i]<min_val:
                min_val=nums[i]
            else:
                i+=1
        return min_val