import os
os.chdir(r'C:\Users\jagtaabh\Documents\Tutorial\Python\Practice\Pract1')

if os.path.isfile('MyFile.txt'):
    try:
        with open('MyFile.txt','a+') as f:
            print('File name is: %s' %f.name)
            
            print('File is open in %s mode' %f.mode)

            print('Is file writable?',f.writable())

            print('Is file readable?',f.readable())
            t = f.read()
            if 'Now this file has became old.' not in t:
                f.write('\nNow this file has became old.')
                
        f = open('MyFile.txt','r')
        print('Pointer is at location {}'.format(f.tell()))
        x = f.readlines()
        print('File content is as below: \n')
        for txt in x:
            print(txt)
        print('At the end pointer is at location {}'.format(f.tell()))
        f.seek(0)
        print('Now pointer is at location {}'.format(f.tell()))
        f.close()
    except:
        print('Error has occured...')
else:
    print('File "MyFile.txt" does not exists, creating new file')
    with open('MyFile.txt','a+') as f:
        f.write('This file is newly created')

