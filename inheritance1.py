class parent:
    
    def __init__(self):
        print("In constructor parent")

    def parentFunc(self):
        print("In parent function")
        
class child(parent):
    def __init__(self):
        # parent()
        # super().__init__()
        parent.__init__(self)
        print("In child constructor")

    def childFunc(self):
        print("In child function")

obj1=child()
obj1.parentFunc()
obj1.childFunc()