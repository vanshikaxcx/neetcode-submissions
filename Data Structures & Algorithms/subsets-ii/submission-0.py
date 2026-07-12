class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        def helper(i, nums, curset, subsets):
            if i>=len(nums):
                subsets.append(curset.copy())
                return

            curset.append(nums[i])
            helper(i+1,nums,curset,subsets)
            curset.pop()

            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            helper(i+1,nums,curset,subsets)

        subsets, curset=[],[]
        helper(0,nums,curset,subsets)
        return subsets