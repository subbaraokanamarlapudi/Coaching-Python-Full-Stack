'''
Palindrome

'''

# 1st - method

class Solution:
    def isPalindrome(self,x):
        if x<0:
            return False
        else:
            return str(x) == str(x)[::-1]

s = Solution()
print(s.isPalindrome(121))

# 2nd - method

class Solution:
    def isPalindrome(self,x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_num = 0
        while x > reversed_num:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
        return x == reversed_num or x == reversed_num // 10
    
s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-10))
print(s.isPalindrome(-121))