# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms. 

def even_fib_sum(limit):
    fib = 1
    prev1 = 1
    prev2 = 1
    sum = 0
    while fib <= limit:
        if fib % 2 == 0:
            sum += fib        
        fib = prev1 + prev2
        prev2 = prev1
        prev1 = fib
    return sum

print(even_fib_sum(4000000))
# Result: 
# 4613732