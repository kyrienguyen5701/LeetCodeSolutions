'''
Given a triangle array, return the minimum path sum from top to bottom.
For each step, you may move to an adjacent number of the row below. 
More formally, if you are on index i on the current row, you may move to 
either index i or index i + 1 on the next row.
'''

def minimumTotal(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    min_cost = [triangle[0], [entry + triangle[0][0] for entry in triangle[1]]]
    for row in triangle[2:]:
        row_min_cost = []
        for i in range(len(row)):
            if i == 0:
                row_min_cost.append(min_cost[-1][0] + row[i])
            elif i == len(row) - 1:
                row_min_cost.append(min_cost[-1][-1] + row[i])
            else:
                row_min_cost.append(min([min_cost[-1][i - 1] + row[i], min_cost[-1][i] + row[i]]))
        min_cost.append(row_min_cost)
    return min(min_cost[-1])

'''
Runtime: 52ms - 95.06%
Memory Usage: 15MB - 65.59%
'''