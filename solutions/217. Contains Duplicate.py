class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''
        res = 1
        n = len(nums)
        for i in range(1, len(nums)):
            j = 0
            for j in range(i):
                if(nums[i]==nums[j]):
                    break
            if(i==j+1):
                res = res + 1
        if(res!=n):
            return True
        else:
            return False
        '''
        nums.sort()
        n = len(nums)
        res = 0
        i = 0
        while(i<n):
            while(i<n-1 and nums[i] == nums[i+1]):
                i = i + 1
            res = res + 1
            i = i + 1
            
        if(res!=n):
            return True
        else:
            return False
