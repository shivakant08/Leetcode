nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

def threeSum(nums):
    result =[]  #   create an empty array to store the final output

    # This step reduces the complexity of the code as it helps to simplifies the duplicate handling
    nums.sort()  # Sorting the array in ascending order
    n = len(nums)
    
    #   To Solve this problem we fix a pointer to a value in the array and then find the sum of the other two values using two-pointer approach
    for i in range(n):
        if n > 0 and nums[i] == nums[i - 1]:
            continue
        
        low, high = i + 1, n - 1
        while low < high:
            triplet = nums[i] + nums[low] + nums[high]
            if triplet > 0:
                high -=1
            elif triplet < 0:
                low +=1
            else:
                result.append([nums[i], nums[low], nums[high]])
                low += 1

                while nums[low] == nums[low -1] and low < high:
                    low +=1

    return result

print(threeSum(nums))


