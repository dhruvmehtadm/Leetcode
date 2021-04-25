class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        c = max(candies)
        boolList = []
        for i in candies:
            if(i+extraCandies>=c):
                boolList.append(True)
            else:
                boolList.append(False)
        return boolList
