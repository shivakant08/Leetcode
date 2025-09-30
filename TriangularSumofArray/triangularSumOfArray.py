nums = [1,2,3,4,5]
Output: 8

def triangularSum(nums):
    while len(nums) > 1:
        new_nums =[]
        for i in range(len(nums) -1):
            new_nums.append((nums[i] + nums[i + 1]) % 10)
        nums = new_nums
    return nums[0]
        
print(triangularSum(nums))