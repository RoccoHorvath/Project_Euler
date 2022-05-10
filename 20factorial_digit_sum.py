num = 1
for n in range(1,101):
    num *= n

sum = 0
while num > 0:
    sum += (num%10)
    num //= 10

print(sum)