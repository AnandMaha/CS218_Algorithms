from collections import deque
import math

# euclidean dist
def eucl_dist(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def bfs():
    queue = deque()
    for student in range(n):
        if matchL[student] == -1:
            dist[student] = 0
            queue.append(student)
        else:
            dist[student] = float('inf')
    dist[-1] = float('inf')
    while queue:
        student = queue.popleft()
        if dist[student] < dist[-1]:
            for shelter in adj[student]:
                next_student = matchR[shelter]
                if dist[next_student] == float('inf'):
                    dist[next_student] = dist[student] + 1
                    queue.append(next_student)
    return dist[-1] != float('inf')

def dfs(student):
    if student != -1:
        for shelter in adj[student]:
            next_student = matchR[shelter]
            if dist[next_student] == dist[student] + 1 and dfs(next_student):
                matchR[shelter] = student
                matchL[student] = shelter
                return True
        dist[student] = float('inf')
        return False
    return True

n, m, b = map(int, input().split())
students = []
for _ in range(n):
    sxi, syi, ri = map(int, input().split())
    students.append((sxi, syi, ri))

shelters = []
for _ in range(m):
    txi, tyi = map(int, input().split())
    shelters.append((txi, tyi))

adj = [[] for _ in range(n)]
for i in range(n):
    sxi, syi, ri = students[i]
    for j in range(m):
        txj, tyj = shelters[j]
        if eucl_dist(sxi, syi, txj, tyj) / ri <= b:
            adj[i].append(j)

matchL = [-1] * n
matchR = [-1] * m
dist = [-1] * (n + 1)
matching = 0
while bfs():
    for student in range(n):
        if matchL[student] == -1 and dfs(student):
            matching += 1
print(n - matching)
