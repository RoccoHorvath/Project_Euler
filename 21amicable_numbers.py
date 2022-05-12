
total = 0
num_dict = {}
for n in range(1,10000):
    d = 1
    sum = 0
    while d < n/2+1:
        if n % d == 0:
            sum += d
        d+= 1
    
    if sum in num_dict and num_dict[sum] == n:  
        total += sum
        total += n

    num_dict[n] = sum

print(total)


