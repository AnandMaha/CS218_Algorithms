def calc_car_destroyed(n, train_cars, m, attacks):
    trains_destroyed = set()
    num_destroyed = [0] * m
    
    for j in range(m): # attacks
        Aj, bj, yj = attacks[j]
        for i in range(n): # trains
            xi, Di = train_cars[i]
            if i not in trains_destroyed and abs(xi - yj) <= bj and Di <= Aj:
                num_destroyed[j] += 1
                trains_destroyed.add(i)
    
    return num_destroyed

n = int(input())
train_cars = [tuple(map(int, input().split())) for _ in range(n)]
m = int(input())
attacks = [tuple(map(int, input().split())) for _ in range(m)]
for x in calc_car_destroyed(n, train_cars, m, attacks):
    print(x)
