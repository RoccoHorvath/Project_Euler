highest = -1
highest_num = -1
num = 0
count = 0
frequency = {}
while num < 1000000:
    num += 1
    changing_num = num
    count = 0
    while changing_num != 1:
        if changing_num in frequency:
            count += frequency[changing_num]
            break
        elif changing_num % 2 == 0:
            changing_num /= 2
            count += 1

        else:
            changing_num = changing_num * 3 + 1
            count += 1
    frequency[num] = frequency.get(num,count)
    
    if count > highest:
        highest = count
        highest_num = num

print(highest_num, highest)