import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        '''
        #this code has time limit exceeded
        ans = 1
        for i in range(1, n+1):
            ans = ans*i
        zeros = 0
        while(ans%10==0):
            zeros = zeros + 1
            ans = ans%10
        return zeros
        '''
        num = 0
        while(n!=0):
            num = num + int(n/5)
            n = int(n/5)
        return num
