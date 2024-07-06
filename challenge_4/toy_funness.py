import itertools

def max_happiness(toys):
    curr_toy = -1
    cumm_tot = 0
    res = 0
    for toy in toys:
        if curr_toy < toy:
            curr_toy = toy
            cumm_tot += curr_toy
        res += cumm_tot
    return res

def max_happiness_perm(toys, curr_toy, cumm_tot, res):
    print(toys, curr_toy, cumm_tot, res)
    for i in range(len(toys)):
        if i < len(toys) - 1:
            toy = toys[i]
            next_toy = toys[i+1]
            if toy <= next_toy and curr_toy < toy:
                curr_toy = toy
                cumm_tot += toy
            elif toy > next_toy and curr_toy < toy:
                return max(max_happiness_perm(toys[i+1:],toy, cumm_tot + toy,res + cumm_tot + toy), 
                        max_happiness_perm(toys[i+1:],curr_toy, cumm_tot,res))
        elif i == len(toys) - 1:
            if curr_toy < toys[i]:
                cumm_tot += toys[i]
        res += cumm_tot
        print(toys, curr_toy, cumm_tot, res)
    return res

n = int(input())
toys = list(map(int, input().split()))
# print(max_happiness_perm(toys, -1, 0, 0))
# print(max_happiness(n, toys))


best = -1
indices = list(range(len(toys)))
index_subsets = []
for r in range(len(indices) + 1):
    index_subsets.extend(itertools.combinations(indices, r))
for subset in index_subsets:
    best = max(best, max_happiness([toys[i] for i in subset]))

print(best)
