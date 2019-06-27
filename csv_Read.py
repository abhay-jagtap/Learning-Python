import csv, os

if os.path.isfile('emp.csv'):
    f = open('emp.csv','r')
    r = csv.reader(f)
    data = list(r)
    for line in data:
        for word in line:
            print(word,'\t',end='')
        print('')
else:
    print('File is missing')
