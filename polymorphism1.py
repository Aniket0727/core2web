# class Demo:
#     def fun(self):
#         print("In Demo: fun")
        
# class Memo:
#     def fun(self):
#         print("In Memo: fun")
        
# def callFun(obj):
#     obj.fun()
    
# obj1=Demo()
# obj2=Memo()

# callFun(obj1)
# callFun(obj2)
# #

class Demo:
    def fun():
        print("In Demo: fun")
        
class Memo:
    def fun():
        print("In Memo: fun")
        
def callFun(obj):
    if(obj is Demo):
        Demo.gun()
    else:
        Memo.fun()
    
obj1=Demo()
obj2=Memo()
# callFun(obj1)
callFun(obj2)




