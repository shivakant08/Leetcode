nums = [1,2,3,4,5,6]

def EvenNumbersBitwiseOrs(nums):
    ans = 0
    for num in nums:
        if num % 2 == 0:
            ans |= num
    return ans

print(EvenNumbersBitwiseOrs(nums))