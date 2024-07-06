import heapq
 
def heuristic(x, y):
    # Precomputed heuristic values (Manhattan distance)
    return abs(x - (n-1)) + abs(y - (n-1))
 
def in_bounds(x, y):
    return 0 <= x < n and 0 <= y < n
 
def astar(n, t, grid):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
    pq = [(0, 0, 0)]  # (f, g, x*n+y)
    visited = set()
    shortest_paths = {0: 0}  # Memoization of shortest paths
    
    while pq:
        f, g, cell = heapq.heappop(pq)
        x, y = divmod(cell, n)
        
        if (x, y) == (n-1, n-1):
            return g
        
        if cell in visited:
            continue
        visited.add(cell)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny):
                new_time = g + (1 if grid[nx][ny] != 'b' else 1 + t)
                h = heuristic(nx, ny)
                nf = new_time + h
                
                if nx*n+ny not in shortest_paths or new_time < shortest_paths[nx*n+ny]:
                    shortest_paths[nx*n+ny] = new_time
                    heapq.heappush(pq, (nf, new_time, nx*n+ny))
 
n, t = map(int, input().split())
grid = [input() for _ in range(n)]
 
print(astar(n, t, grid))