def isPalindrome(self, x):
        x2 = x
        y = 0
        z = ""

        if x < 0:
            return False
        
        while x2 >= 1:
            y = x2 % 10
            x2 = x2 // 10
            z += str(y) 

        if x == int(z):
            return True
        else:
            return False

a = isPalindrome(0, 12)
print(a)