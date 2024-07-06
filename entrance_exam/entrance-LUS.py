def longest_unimodal_subsequence(arr):
    n = len(arr)
    increasing = [1] * n
    decreasing = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                increasing[i] = max(increasing[i], increasing[j] + 1)
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if arr[i] > arr[j]:
                decreasing[i] = max(decreasing[i], decreasing[j] + 1)
    return max(increasing[i] + decreasing[i] - 1 for i in range(n))

n = int(input())
arr = list(map(int, input().split()))
print(longest_unimodal_subsequence(arr))
