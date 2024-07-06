def feasible(k, thickness, max_width):
    count = 1
    width = 0
    for book in thickness:
        if width + book > max_width:
            count += 1
            width = 0
        if count > k:
            return False
        width += book
    return True

def find_min_width(k, thickness):
    left = max(thickness)
    right = sum(thickness)
    
    while left < right:
        mid = (left + right) // 2
        if feasible(k, thickness, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

n, k = map(int, input().split())
thickness = [int(input()) for _ in range(n)]
print(find_min_width(k, thickness))