'''
1. Two Sum
'''

# 1st method 

class Sum:
    def two_sum(self,nums,target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []


sum = Sum()
result = ([2,7,11,15],9)
print(sum.two_sum(result[0],result[1]))

# 2nd method

class Sum:
    def two_sum(self,nums,target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []
    
sum = Sum()
result = ([2,7,11,15],9)
print(sum.two_sum(result[0],result[1]))

# 3rd method  [optinal]

class Sum:
    def two_sum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return []

# Example usage
sum_instance = Sum()
result = sum_instance.two_sum([2, 7, 11, 15], 9)
print(result)
