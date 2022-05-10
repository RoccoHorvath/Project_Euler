with open("p067_triangle.txt", "r") as f:
    nums = f.read()

num_string_list = nums.split('\n')
num_string_list.pop()
print(num_string_list)
num_list=[]
for i in range(len(num_string_list)-1,-1,-1):
    num_list.append(num_string_list[i].split())


for count_n, n in enumerate(num_list):
    for count_m, m in enumerate(n):
        num_list[count_n][count_m] = int(num_list[count_n][count_m])
        
# Everything above this is formatting th data to a nested list with elements that are integers.
temp_list = []
sum = []

for count, n in enumerate(num_list[1]):
    if n + num_list[0][count] > n + num_list[0][count+1]:
        sum.append((n + num_list[0][count]))
    else:
        sum.append((n + num_list[0][count+1]))

for  n in num_list[2:]:
    for count_m, m in enumerate(n):
        if m + sum[count_m] > m + sum[count_m+1]:
            temp_list.append((m + sum[count_m]))
        else:
            temp_list.append((m + sum[count_m+1]))

    sum = temp_list
    temp_list = []

print(sum)