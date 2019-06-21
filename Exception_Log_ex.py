import logging as log
class MyExp(Exception):
    def __init__(self,msg):
        self.msg = msg

def myCode(num):
    
    import datetime as d
    td_l = d.date.today()
    td = str(td_l.day)
    tm = str(td_l.month)
    log.basicConfig(filename = 'log_'+td+'_'+tm+'.txt',level=log.DEBUG)
    log.info('Started program')
    try:
        if int(num) == 0:
            raise MyExp('Please enter number other than zero')
        else:
            print('Entered number is ',num)
    except MyExp as msg:
        print(msg)
        log.exception(msg)
    else:
        print('No errors found')
    finally:
        print('End of program')
        log.info('End of program')

        
x = input('Enter the number: ')

myCode(x)
