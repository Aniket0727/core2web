def decorFun(func):
    print("In decor fun")
    print(func)
    def wrapper():
        print("Strat Wrapper")
        func()
        print("End Wrapper")
        
    return wrapper

def normalFun(x,y):
    print("Normal Function")
    return x+y
    
print(decorFun(normalFun(10,20)))
