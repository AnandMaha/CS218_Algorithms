import heapq

def dijkstra(n, m, u, v, s, hotel_prices, highways):
    dist = [[float('inf')] * (s + 1) for _ in range(n)]
    dist[u - 1][0] = 0
    pq = [(0, u, 0)]

    while pq:
        cost, city, gas_left = heapq.heappop(pq)
        if city == v:
            return cost

        for neighbor, gas_cost in highways[city]:
            for stay_cost in hotel_prices:
                if gas_left >= gas_cost:
                    gas_left -= gas_cost
                    total_cost = cost + stay_cost
                    if total_cost < dist[neighbor - 1][gas_left]:
                        dist[neighbor - 1][gas_left] = total_cost
                        heapq.heappush(pq, (total_cost, neighbor, min(s, gas_left + 1)))
                    gas_left += gas_cost

    return -1

# Input
n, m, u, v, s = map(int, input().split())
hotel_prices = [int(input()) for _ in range(n)]
highways = {i: [] for i in range(1, n + 1)}
for _ in range(m):
    a, b, c = map(int, input().split())
    highways[a].append((b, c))
    highways[b].append((a, c))

# Add hotel prices for Pittsburgh and Riverside
hotel_prices[u - 1] = 0
hotel_prices[v - 1] = 0

# Output
print(dijkstra(n, m, u, v, s, hotel_prices, highways))
