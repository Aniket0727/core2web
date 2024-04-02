class parent:
    def marry(self):
        print("Deepika")

class child(parent):
    def marry(self):
        # super().marry()
        print("Alia")
        

child()
# obj=parent()
# obj.marry()