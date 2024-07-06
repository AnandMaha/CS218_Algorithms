def most_common_value(bad_list):
    counts = {}
    for row in bad_list:
        for value in row:
            counts[value] = counts.get(value, 0) + 1
    return max(counts, key = counts.get)

def num_furniture_remove(L, n, k, furnitures):
    grid = {}
    # fill in grid with furniture
    for idx, f in enumerate(furnitures, start = 1):
        for i in range(f[0], f[2] + 1):
            grid.setdefault(i, set()).add(idx)

    num_removed = 0
    while True:  # only break when all rows within limit
        # check each row if it's within k
        bad_list = [row for row in grid.values() if len(row) > k]

        if not bad_list:
            return num_removed

        num_removed += 1  # gotta be something to remove
        to_remove = most_common_value(bad_list)
        for row, furniture in grid.items():
            grid[row] = {x for x in furniture if x != to_remove}

L, n, k = map(int, input().split())
furnitures = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(n)]
print(num_furniture_remove(L, n, k, furnitures))
