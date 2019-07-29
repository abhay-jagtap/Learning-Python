s = 'Tieto India Private Limited'
x = []
s1 = ''
l = s.split()
ln = len(l) - 1

while ln >= 0:
    x.append(l[ln])
    ln -= 1
    
s = ' '.join(x)
print(s)
