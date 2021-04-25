class Solution(object):
    def twoSum(self, nums, target):
        tally = {}
        for i, num in enumerate(nums):
            other = target - num
            try:
                if i != tally[other]:
                    return [tally[other], i]
            except:
                pass
            tally[num] = i
        return []
