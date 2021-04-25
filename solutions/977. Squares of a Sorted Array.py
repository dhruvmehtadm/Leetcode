class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squ = []
        for num in nums:
            squ.append(num*num)
        squ = sorted(squ)
        return squ
