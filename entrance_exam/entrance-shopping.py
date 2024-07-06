def items_can_buy(k, prices):
    prices.sort()
    num_items = 0
    curr_money = 0
    for price in prices:
        if curr_money + price <= k:
            num_items += 1
            curr_money += price
        else:
            break
    print(num_items)

k, n = map(int, input().split())
prices = list(map(int, input().split()))
items_can_buy(k, prices)
