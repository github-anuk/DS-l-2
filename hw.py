class Animals:
    def __init__(self,name,type,age):
        self.type=type
        self.age=age
        self.name=name
        
    def getAge(self):
        return self. age
    
    def setAge(self,newAge):
        self.age=newAge

    def show_animal():
        print("I have a pet , it's name is {} ,it is a {},it is {} years old  ")



class Pets(Animals):
    def __init__(self,name,type,age,breed,gender):
        Animals.__init__(self,name,type,age)
        self.breed=breed
        self.gender=gender

    def showPets(self):
        print("I have a pet {} , {} is named {},{} is a {},{},{} is {} years old".format(self.type,self.gender,self.name,self.gender,self.breed,self.type,self.gender,self.age))

    
lily=Pets("lily","cat",1,"ragdoll","she")
print(lily.getAge())

lily.setAge("2 ")
print(lily.showPets())