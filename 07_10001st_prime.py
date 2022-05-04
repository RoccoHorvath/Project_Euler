count = 1
num = 1
while count != 10001:
    num += 2
    sqrt = int(num**(1/2)//1)
    prime = True
    divisor = 2
    while prime and divisor <= sqrt:
        if num % divisor == 0:
            prime = False
        divisor += 1
    if prime:
        count += 1

     

print(num)