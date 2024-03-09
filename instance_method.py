class first:
    
    def __init__(self):
        print("init")
        
    @classmethod  #store in class name space
    def info1(self): #class method
        print("class method")
        print(self)
        
    def info2(self): #instance method #store in class name space
        print("Instance method")
        print(self)
        
        #static method #store in class name space both access class and object
    @staticmethod
    def info3(self):
        print("static method")
        print(self)
    
f1=first()

# f1.info1()
# first.info1()

f1.info2()
# first.info2()

# f1.info3()
# first.info3()



# first.info()
# first.info2()
# first()
# first.info3()
# f1.info3()


# object connected  is called instance method
# class connect is called class method


# who can call methods
# only object  --> instance method
# object and class --> class method
# object and class --> static method
