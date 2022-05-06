term = 2
factors_count = 0
sum = 1
while factors_count < 500:
    divisor = 2
    factors = {}
    factors_count = 1
    sum += term
    num = sum
    while num != 1:
        while num % divisor == 0:
            factors[divisor] = factors.get(divisor,0) + 1
            num /= divisor
        divisor += 1
    for value in factors.values():
        factors_count *= (value+1)

    term += 1

print(sum)
            