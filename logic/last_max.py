l = [1,2,3,4,9,5,3,7,6]

max = 0
second_max = 0
for i in l:
    if i > max:
        max = i
        l.remove(max)

for i in l:
    if i > second_max:
        second_max = i

print(second_max)     
