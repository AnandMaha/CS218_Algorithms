from collections import defaultdict

def max_treats(n, treats):
    max_count = 0
    for i in range(n): # get most points on the same slope
        treat_count = defaultdict(int)
        x1, y1 = treats[i]
        
        for j in range(i+1, n):
            x2, y2 = treats[j]
            if x1 == x2:
                slope = float('inf')  # vert line
            else:
                slope = (y2 - y1) / (x2 - x1)
            treat_count[slope] += 1
        
        max_count = max(max_count, max(treat_count.values(), default=0) + 1)
    
    return max_count

n = int(input())
treats = [list(map(int, input().split())) for _ in range(n)]
print(max_treats(n, treats))
