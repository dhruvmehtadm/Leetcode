class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        summ = 0
        for i in nums:
            summ = summ + i
            out.append(summ)
        return out
