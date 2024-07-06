import heapq

def candy_count(n, bags):
    heapq.heapify(bags)  # min heap
    cnt = 0
    while len(bags) > 1: # keep pulling smallest bags together until one group
        combine_bag = heapq.heappop(bags) + heapq.heappop(bags)
        cnt += 2 * combine_bag
        heapq.heappush(bags, combine_bag) # add combined bag to heap
    return cnt

n = int(input())
bags = [int(input()) for _ in range(n)]
print(candy_count(n, bags))
