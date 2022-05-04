sum_of_squares = 0
square_of_sum = 0
start = 1
end = 100

for i in range(end-start+2):
    square_of_sum += i
    sum_of_squares += i**2

square_of_sum **= 2
print(square_of_sum-sum_of_squares)