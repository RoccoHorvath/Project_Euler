# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

num = 100




def prime_factor(num):
    prime_factor = 0
    factor = int((num ** (1/2)) // 1)
    while not prime_factor:
        x = 3
        if num % factor == 0:
            if factor % 2 != 0:
                while x:
                    if factor % x == 0:
                        break
                    elif x > (factor ** (1/2)):
                        prime_factor = factor
                        return prime_factor

                    x += 2
        factor -= 1  

print(prime_factor(num))

