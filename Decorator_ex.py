
    
def decor(func):
    def inner(name):
        if name == 'xxx':
            print('Bad Morning xxx')
        else:
            func(name)

    return inner

@decor
def greet(name):
    print('Good morning:',name)
    
greet('abhay')
greet('xxx')
            
