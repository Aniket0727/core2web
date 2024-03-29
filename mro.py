
# class Demo():
#     pass

# print(dir(object))
# print(dir(type))
# print()
# print(Demo.__base__)
# print(type.__base__)
# print(object.__base__)

# print()
# print(type(Demo))
# print(type(object))
# print(type(type))


class Manager:
    
    def project(self):
        print("In proejct manager")

class TeamLead1(Manager):
    pass

class TeamLead2(Manager):
    
    def proejct(self):
        print("In project:TeamLead2")
        
class Developer(TeamLead1,TeamLead2):
    pass

obj=Developer()
obj.proejct()