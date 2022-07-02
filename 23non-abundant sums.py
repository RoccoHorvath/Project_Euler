abundant_list = []

for n in range(2,28124):
    if n in abundant_list:
        continue
    sum = 1
    for m in range(2,n//2+1):
        if n % m == 0:
            sum += m
    abun = n

    if sum == abun:
        n += abun
        while n < 28124:
            abundant_list.append(n)
            n += abun

    if sum > abun:
        while n < 28124:
            abundant_list.append(n)
            n += abun
abundant_list.sort()
abundant_sums = list(set([i+j for i in abundant_list for j in abundant_list if i + j<=28123]))

total = 0

for n in range(28124):
    if n not in abundant_sums:
        total += n

print(total)
            


