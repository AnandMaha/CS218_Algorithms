def longest_path_height(r, c, heights, i, j, long_arr):
    if long_arr[i][j] != float('inf'):
        return long_arr[i][j]
    
    long_num = 1
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < r and 0 <= new_j < c and heights[i][j] > heights[new_i][new_j]: # in range and valid move
            long_num = max(longest_path_height(r, c, heights, new_i, new_j, long_arr) + 1, long_num)
    long_arr[i][j] = long_num
    return long_num

def long_path(r, c, heights):
    long_arr = [[float('inf')] * c for _ in range(r)]
    long_num = 0
    
    for i in range(r):
        for j in range(c):
            long_num = max(longest_path_height(r, c, heights, i, j, long_arr), long_num)
    return long_num

r, c = map(int, input().split())
heights = [list(map(int, input().split())) for _ in range(r)]
print(long_path(r, c, heights))
