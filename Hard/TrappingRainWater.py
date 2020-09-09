'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.
'''

def trap(heights):
    if not heights:
        return 0

    H, W = max(heights), len(heights)
    total, air = H * W, 0
    ground = sum(heights)

    i, j, l, r = 0, W - 1, 0, 0
    while heights[i] < H or heights[j] < H:
        if heights[i] < H:
            l = max(l, heights[i])
            air += H - l
            i += 1
        if heights[j] < H:
            r = max(r, heights[j])
            air += H - r
            j -= 1

    return total - ground - air


'''
Runtime: 52ms - 81.59%
Memory: 14.4MB - 91.16%
'''