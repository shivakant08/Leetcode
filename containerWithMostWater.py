height = [1,8,6,2,5,4,8,3,7]
Output: 49

def maxArea(height):
    max_area = 0
    left, right = 0, len(height) -1

    while left < right:
        width = right - left
        currArea = width * min(height[left], height[right])
        max_area = max(max_area, currArea)

        if height[left] < height[right]:
            left += 1
        else:
            right -=1

    return max_area

print(maxArea(height))