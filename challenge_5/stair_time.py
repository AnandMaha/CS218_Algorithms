from collections import deque, defaultdict

def earliest_arrival_time(n, m, k, stairways):
    graph = defaultdict(list)
    for x, y, z in stairways:
        graph[x].append((y, z))
        graph[y].append((x, x))
        graph[z].append((x, x)) 

    queue = deque([(0, 0)])
    visited = set([(0, 0)])
    
    while queue:
        current_platform, current_time = queue.popleft()
        
        if current_platform == k:
            return current_time
        
        next_time = current_time + 1
        for y, z in graph[current_platform]:
            if current_time % 2 == 0:
                next_platform = y
            else:
                next_platform = z
            
            next_state = (next_platform, next_time)
            if next_state not in visited:
                visited.add(next_state)
                queue.append(next_state)
    
    return -1

n, m, k = map(int, input().split())
stairways = [tuple(map(int, input().split())) for _ in range(m)]

result = earliest_arrival_time(n, m, k, stairways)
print(result)
