from collections import deque

def determineMeeting(grid, r, c, p1, p2):
    visited = [[False] * c for _ in range(r)]
    q = deque([p1])
    visited[p1[0]][p1[1]] = True
    while q:
        x, y = q.popleft()
        if (x, y) == p2:
            return True
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and grid[nx][ny] == '.':
                visited[nx][ny] = True
                q.append((nx, ny))
    return False

def meltIce(grid, r, c, meltQ):
    newMeltQ = deque()
    while meltQ:
        x, y = meltQ.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 'X':
                grid[nx][ny] = '.'
                newMeltQ.append((nx, ny))
    return newMeltQ

def computeMeetDay(grid, r, c, p1, p2):
    meltQ = deque()
    waterCells = set()
    for i in range(r):
        for j in range(c):
            if grid[i][j] == '.':
                waterCells.add((i, j))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < r and 0 <= ny < c and grid[nx][ny] == 'X':
                        meltQ.append((i, j))
    days = 0
    while not determineMeeting(grid, r, c, p1, p2):
        meltQ = meltIce(grid, r, c, meltQ)
        days += 1
    return days

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]
p1, p2 = None, None
for i in range(r):
    for j in range(c):
        if grid[i][j] == 'L':
            if p1:
                p2 = (i, j)
            else:
                p1 = (i, j)
            grid[i][j] = '.'
result = computeMeetDay(grid, r, c, p1, p2)
print(result)
