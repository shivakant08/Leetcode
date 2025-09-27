nums1 = [1,3] 
nums2 = [2]
# Output: 2.00000
def findMedianOfSortedArrays(nums1, nums2):
    result = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            result.append(nums1[i])
            i += 1
        else:
            result.append(nums2[j])
            j += 1

    while i < len(nums1):
        result.append(nums1[i])
        i+=1
    while j < len(nums2):
        result.append(nums2[j])
        j +=1

    n = len(result)
    if n % 2 == 0:
        return (result[n // 2 -1] + result[n//2]) / 2.0
        
    else:
       return result[n//2]

    

print(findMedianOfSortedArrays(nums1,nums2))

        