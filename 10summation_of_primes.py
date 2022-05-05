sum = 0
i = 2
while i < 2000000:
    is_prime = True
    if i % 2 != 0 and i % 5 != 0:        
        sqrt = int(i ** (1/2)//1)
        for j in range(2,sqrt+1):
            if i % j == 0:
                is_prime = False
    else: is_prime = False
    if is_prime or i/2 == 1 or i/5 == 1:
        sum += i
    i += 1
   
print(sum)