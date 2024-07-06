from collections import deque

def can_reach_all_exits(n, m, heights):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * m for _ in range(n)]
    reachable_from_top = [[False] * m for _ in range(n)]
    
    def bfs(start):
        queue = deque([start])
        visited[start[0]][start[1]] = True
        while queue:
            x, y = queue.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and heights[x][y] > heights[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    # Check reachability from all top row cells
    for j in range(m):
        if not visited[0][j]:
            bfs((0, j))
    
    # Mark reachable cells from the top row
    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                reachable_from_top[i][j] = True
    
    # Reset visited for the second pass
    visited = [[False] * m for _ in range(n)]
    
    # Check reachability from each exit
    reachable_exits = 0
    for j in range(m):
        if reachable_from_top[n-1][j]:
            reachable_exits += 1
        elif not visited[n-1][j]:
            bfs((n-1, j))
    
    # Count distinct reachable entrances
    reachable_entrances = set()
    for j in range(m):
        for i in range(n):
            if reachable_from_top[i][j]:
                reachable_entrances.add(j)
                break
    
    if reachable_exits == m:
        return 1, len(reachable_entrances)
    else:
        return 0, reachable_exits

def main():
    n, m = map(int, input().split())
    heights = [list(map(int, input().split())) for _ in range(n)]
    
    can_reach, value = can_reach_all_exits(n, m, heights)
    print(can_reach)
    print(value)

if __name__ == "__main__":
    main()
