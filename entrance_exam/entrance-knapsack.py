def dp_knapsack(W, n, weights, values):
    max_values = [[0] * (W + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] > w:
                max_values[i][w] = max_values[i - 1][w]
            elif weights[i - 1] <= w:
                max_values[i][w] = max(max_values[i - 1][w], max_values[i - 1][w - weights[i - 1]] + values[i - 1])
    return max_values[n][W]

W, n = map(int, input().split())
weights = []
values = []
for _ in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)
print(dp_knapsack(W, n, weights, values))
