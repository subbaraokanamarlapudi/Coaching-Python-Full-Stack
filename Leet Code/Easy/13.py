'''
Roman to Integer converstion

'''

# method - 1

class Solution:
    def romanToInt(self,str):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        prev_value = 0

        for char in str:
            value = roman_dict[char]
            if value > prev_value:
                result += value - 2 * prev_value
            else:
                result += value
            prev_value += value
        
        return result
    
s = Solution()
print(s.romanToInt('IX'))
print(s.romanToInt('LVIII'))

# method - 2