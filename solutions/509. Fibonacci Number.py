class Solution:
    def fib(self, n: int) -> int:
        self.n = n
        f1=0
        f2=1
        for i in range(n):
            nxt = f1 + f2
            f1=f2
            f2=nxt
            
        return f1
