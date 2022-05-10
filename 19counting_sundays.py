year = 1901
day = 0
days_list = [31,28,31,30,31,30,31,31,30,31,30,31]
# Jan 1st 1901 was a Tuesday. If Tuesday is index 0 then
# Tue: 0, Wed: 1, Thurs: 2, Fri: 3, Sat: 4, Sun: 5, Mon: 6
month = 0
count = 0

while year < 2001:
    if day % 7 == 5:
        count += 1
    day += days_list[month%12]
    
    if year % 4 == 0 and month % 12 == 1:
        day += 1
    
    month += 1

    if month % 12 == 0:
        year += 1

print(count)