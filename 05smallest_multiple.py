smallest = 0
max_factor = 20
min_factor = 1
counter = max_factor
while not smallest:
    factors = 0
    for i in range(max_factor,0,-1):
        i += 1
        if counter % i == 0:
            factors += 1
        else: break

    if factors == 20:
        smallest = counter
    counter += max_factor

print(smallest)