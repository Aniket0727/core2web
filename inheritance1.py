# class parent:
    
#     def __init__(self):
#         # print("In constructor parent")
#         print(self)

#     def parentFunc(self):
#         print("In parent function")
        
# class child(parent):
#     def __init__(self):
#         # parent()   #it create parent addres
#         # super().__init__()  #it create child addres
#         parent.__init__(self)  #it create child addres
#         print("In child constructor")

#     def childFunc(self):
#         print("In child function")

# obj1=child()
# obj1.parentFunc()
# obj1.childFunc()





class parent:
    z=30
    def __init__(self):
        print("In constructor parent")
        self.x=10
        self.y=20
    
    def disData(self):
        print(self.x)
        print(self.y)  
    @classmethod
    def disParent(cls):  
        print(cls.z)         
class child(parent):
    pass

obj=parent()
obj.disData()
obj.disParent()



