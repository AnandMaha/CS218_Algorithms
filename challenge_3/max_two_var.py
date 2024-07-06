def max_two_var(n, cow_vals):
    best_res = -1 * float('inf')
    for i in range(1, 2 ** n):
        ts, tf = 0, 0
        for j in range(n):
            if (i >> j) & 1:
                ts += cow_vals[j][0]
                tf += cow_vals[j][1]
         
        if ts >= 0 and tf >= 0:
            best_res = max(ts + tf, best_res)

    return best_res if best_res != -1 * float('inf') else 0

 
n = int(input())
cow_vals = []
for _ in range(n):
    si, fi = map(int, input().split())
    cow_vals.append((si, fi))
print(max_two_var(n, cow_vals))
