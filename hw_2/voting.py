def min_support(n, depart):
    depart.sort()
    min_num = 0
    for i in range(n // 2 + 1):
        min_num += depart[i] // 2 + 1
    return min_num


n = int(input())
depart = [int(input()) for _ in range(n)]
print(min_support(n, depart))