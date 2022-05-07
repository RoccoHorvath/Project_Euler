grid = 20

n_fact = 1
for n in range(1,grid*2+1):
    n_fact *= n

k_fact = 1
for k in range(1,grid+1):
    k_fact *= k

j_fact = 1
for j in range(1,grid*2-grid+1):
    j_fact *= j

paths = n_fact /(k_fact*j_fact)
print(paths)