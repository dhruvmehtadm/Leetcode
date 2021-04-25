class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 0
        if(n==0):
            ans = 1
            return ans
        else:
            ans = float(x**n)
            return float(ans)
