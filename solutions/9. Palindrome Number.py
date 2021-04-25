class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.x = x
        if(x<0):
            return False
        else:
            y = x
            z = 0
            while(y>0):
                rem = y%10
                z = (z*10) + rem
                y = y//10
            if(z==x):
                return True
            else:
                return False
        '''
        else if(x>0 and x<9):
            return true
        else if(x==11 or x==22 or x==33 or x==44 or x==55 or x==66 or x==77 or x==88 or x==99):
            return true
        else if(x>100):
        
            y = x
            z = 0
            while(y>0):
                rem = y%10
                z = (z*10) + rem
                y = y//10
            if(z==x):
                return true
            else:
                return false
        '''
