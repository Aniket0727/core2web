#Method overloading

class Parent:
    def fun(self):
        print("fun:parent")
        
    def gun(self):
        print("gun:parent")

class Child(Parent):
        
    def gun(self):
        print("gun:Child")
        return 10

obj1=Child()
obj1.fun()
obj1.gun()
