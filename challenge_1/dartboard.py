def dartboard(N, M, sectors):
    dp = [0] * (M + 1)
    chosen = [[] for _ in range(M + 1)]
 
    for i in range(4): # 1,2,3,4 darts!
        for j in range(M, 0, -1):  # point limit
            for k in range(N):  # sectors
                if sectors[k] <= j:
                    score_with_dart = dp[j - sectors[k]] + sectors[k]
                    if score_with_dart > dp[j]:
                        dp[j] = score_with_dart
                        chosen[j] = chosen[j - sectors[k]] + [k + 1]
            if i == 3:
                break
 
    max_points = dp[M]
    while len(chosen[M]) < 4:
        chosen[M].append(0)
    return max_points, chosen[M]
 
N, M = map(int, input().split())
sectors = [int(input()) for _ in range(N)]
max_points, sectors_chosen = dartboard(N, M, sectors)
print(*sectors_chosen)