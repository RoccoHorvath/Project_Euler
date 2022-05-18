with open("p022_names.txt","r") as f:
    names = f.read()


names = names.replace('"',"")
names = names.split(",")

names.sort()

total = 0
for count, name in enumerate(names):
    word = 0
    for letter in name:
        word += (ord(letter)-64)
        print(letter,ord(letter)-64)
    total += word * (count+1)

print(total)