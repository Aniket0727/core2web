def outerFunc():
    print("In outer fun")
    
    def innerFun1():
        print("In inner fun-1")
        
    def innerFun2():
        print("In inner fun-2")

    return innerFun1,innerFun2

    
a=outerFunc()
a[0]()
a[1]()

