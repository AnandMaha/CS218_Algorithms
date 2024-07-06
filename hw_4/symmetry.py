def min_insert_cost(str1, str2, cost):
    m, n = len(str1), len(str2)
    
    # store the min cost to make substrings equal
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(m + 1):
        for j in range(n + 1):
            # one of the strings is empty, insert chars from the other string
            if i == 0:
                dp[i][j] = sum(cost.get(char, 0) for char in str2[:j])
            elif j == 0:
                dp[i][j] = sum(cost.get(char, 0) for char in str1[:i])
            # chars are equal, no cost
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                # min cost between inserting into str1 or str2
                dp[i][j] = min(dp[i - 1][j] + cost.get(str1[i - 1], 0),
                               dp[i][j - 1] + cost.get(str2[j - 1], 0))

    # min cost to make the strings equal
    return dp[m][n]

def min_candy_symmetry(n, k, prices, candy_string):
    return int(min_insert_cost(candy_string, candy_string[::-1], prices) / 2)

n, k = map(int, input().split())
prices = {}
for i in range(k):
    prices[chr(ord('a') + i)] = int(input())
candy_string = input()

real_prices = {}
for key in set(candy_string):
    real_prices[key] = prices[key]

print(min_candy_symmetry(n, k, prices, candy_string))
