nums = [0,1,2,3,4,5,6,7,8,9]

perms = [1]
perm = 1
for n in range(1,11):
    perm *= n
    perms.append(perm)

num = []
count = 0
target = 999999

for i in perms[-2::-1]:
    count = target//i

    if target == 0:
        num.append(str(nums[0]))
        nums.remove(nums[0])
    else:
        num.append(str(nums[count]))
        nums.remove(nums[count])

    target %= i

print(''.join(num))