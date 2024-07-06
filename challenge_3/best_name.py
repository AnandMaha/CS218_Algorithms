def opt_str(str, i):
    if i == len(str) + 1:
        return str
    return min(opt_str(str, i+1), opt_str(str[:i:][::-1] + str[i:], i+1)) 

best_str = opt_str(input(), 2)
print(best_str)
