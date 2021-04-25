class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        quo = 0
        if(dividend>0 and divisor>0):
            quo = dividend//divisor
            if(quo<-2147483647):
                return -2147483648
            elif(quo>2147483647):
                return 2147483647
            else:
                return quo
        elif(dividend<0 and divisor<0):
            quo = (-1*dividend)//(-1*divisor)
            if(quo<-2147483647):
                return -2147483648
            elif(quo>2147483647):
                return 2147483647
            else:
                return quo
        elif(dividend>0 and divisor<0):
            quo = dividend//(-1*divisor)
            quo = -1*quo
            if(quo<-2147483647):
                return -2147483648
            elif(quo>2147483647):
                return 2147483647
            else:
                return quo
        elif(dividend<0 and divisor>0):
            quo = (-1*dividend)//divisor
            quo = -1*quo
            if(quo<-2147483647):
                return -2147483648
            elif(quo>2147483647):
                return 2147483647
            else:
                return quo
        elif(dividend==0):
            return 0
