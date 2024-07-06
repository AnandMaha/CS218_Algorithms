def knapsack_limit(W, n, k, weights, values):
    max_values = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): # subset of items
        for j in range(1, W + 1): # weight limit
            for t in range(min(j // weights[i - 1], k) + 1): # num times to include it
                # either include the new item "t" times, or keep what was already there
                max_values[i][j] = max(max_values[i - 1][j - t * weights[i - 1]] + t * values[i - 1], max_values[i][j])
    return max_values[n][W]

W, n, k = map(int, input().split())
weights = []
values = []
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
print(knapsack_limit(W, n, k, weights, values))
