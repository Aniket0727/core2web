def fun():
    yield 10
    yield 20

a=fun()
print(a)
print(a)
for i in a:
    print(a)
    
