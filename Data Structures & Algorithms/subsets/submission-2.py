class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def helper(i, nums, curset, subsets):
            if i>=len(nums):
                subsets.append(curset.copy())
                return

            curset.append(nums[i])
            helper(i+1,nums,curset,subsets)
            curset.pop()

            helper(i+1, nums, curset, subsets)

        subsets, curset=[],[]
        helper(0,nums, curset, subsets)
        return subsets
