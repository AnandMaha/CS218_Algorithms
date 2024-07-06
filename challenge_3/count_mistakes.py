def min_mistakes(n, key, mod):
    key_dp = [i for i in range(n + 1)] # only store a row at a time
    
    for j in range(1, n + 1):
        new_row = [j] * (n + 1)
        for i in range(1, n + 1):
            # order: remove letter, add letter, copy letter
            if key[i - 1] == mod[j - 1]:
                new_row[i] = min(key_dp[i] + 1, new_row[i - 1] + 1, key_dp[i - 1])
            else:
                new_row[i] = min(key_dp[i] + 1, new_row[i - 1] + 1, key_dp[i - 1] + 1)
        key_dp = new_row
    
    return key_dp[n]

n = int(input())
key = input().strip()
mod = input().strip()
print(min_mistakes(n, key, mod))
