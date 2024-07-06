class UnionFind:
    def __init__(self, size):
        self.placement = [1] * size
        self.par = list(range(size))
        
    def find(self, u):
        if self.par[u] != u:
            self.par[u] = self.find(self.par[u])
        return self.par[u]

    def union(self, u, v):
        rootU = self.find(u)
        rootV = self.find(v)
        if rootU != rootV:
            if self.placement[rootU] < self.placement[rootV]:
                self.par[rootU] = rootV
            elif self.placement[rootU] > self.placement[rootV]:
                self.par[rootV] = rootU
            elif self.placement[rootU] == self.placement[rootV]:
                self.placement[rootU] += 1
                self.par[rootV] = rootU
            return True
        return False

def min_capacity(n, edges):
    edges.sort(key=lambda x: x[2]) # sort weights in ascending order for kruskal
    union_find_obj = UnionFind(n)
    min_capacity_edge = 0

    for x, y, z in edges:
        if union_find_obj.union(x, y):
            min_capacity_edge = z

    return min_capacity_edge

n, m = map(int, input().split())
edges = []
for _ in range(m):
    x, y, z = map(int, input().split())
    edges.append((x, y, z))
print(min_capacity(n, edges))
