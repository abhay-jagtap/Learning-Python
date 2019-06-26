import csv, os, sys

x = True
if not os.path.isfile('Employee.csv'):
    x = False
    print('File does not exists, creating new file')

try:
    with open('Employee.csv','a',newline='') as f:
        w =csv.writer(f)
    
        if not x:
            w.writerow(['ENo','EName','ESal','EAddr'])

        enum = input('Enter the no of emps: ')
        for e in range(int(enum)):
            eno = input('Enter emp no: ')
            enm = input('Enter emp name: ')
            esal = input('Enter emp salary: ')
            eadd = input('Enter emp address: ')
            w.writerow([eno,enm,esal,eadd])
    print('csv file successfully created')
except PermissionError as msg:
    print('Error: Please close the file from other apps before editing')
finally: 
	print('Ended the program')
