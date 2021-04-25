class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        #return len([x for x in nums if len(str(x)) % 2 == 0])
        res = 0
        for num in nums:
            if(len(str(num))%2==0):
                res+=1
        return res
