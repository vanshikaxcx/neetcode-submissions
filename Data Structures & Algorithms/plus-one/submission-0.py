class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s="".join(str(d) for d in digits)
        new=int(s)+1
        ans=list(str(new))
        return ans