target = 1000

def py_triplet(target):
    found = False
    while not found:
        for a in range(1,target):
            for b in range(target,a,-1):
                c = (a**2 + b**2) ** (1/2)
                if a + b + c == target and b < c:
                    return f'{a} + {b} + {c} = {a+b+c}\n{a} x {b} x {c} = {a*b*c}\n'
                
                
print(py_triplet(target))
