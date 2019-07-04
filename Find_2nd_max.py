l = [11873,937,4947,9845,9384,9586,8364,20000]

m = 0
m1 = 0
for i in range(0,len(l)):
    if i != 0:
        if m < l[i]:
            m1 = m
            m = l[i]
        elif m1 < l[i]:
            m1 = l[i]
    elif i == 0:
            m = l[i]
print('Max :',m)            
print('Second max :',m1)
