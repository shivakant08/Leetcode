points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2.00000

def largestTriangleArea(points):
    max_area = 0   # to track area 
    n = len(points)

    for i in range(n -2):
        for j in range(i + 1, n -1):
            for k in range(j + 1, n):
                # Destructuring each point in the points array
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]

                #   Calculating the current Area using the shoelace formula for traingle
                #  Area = ½ |(x₁y₂ + x₂y₃ + x₃y₁) - (y₁x₂ + y₂x₃ + y₃x₁)| -----> FORMULA
                currArea = 0.5 * abs((x1 * y2 + x2 * y3 + x3 * y1) - (y1 * x2 + y2 * x3 + y3 * x1))

                if currArea > max_area:
                    max_area = currArea
    return max_area
 

largestTriangleArea(points)