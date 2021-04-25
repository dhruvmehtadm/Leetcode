class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxi = 0
        m = accounts[0]
        for i in range(len(accounts)):
            count = 0
            for j in range(len(m)):
                count = count + accounts[i][j]
            maxi = max(count, maxi)
        return maxi    
