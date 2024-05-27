#parent class
class Car:
    def __init__(self,brand,model,fuel,color):
        self.brand=brand
        self.model=model
        self.fuel=fuel
        self.color=color

    def getColor(self):
        return self . color
    
    def setColor(self,newColor):
        self.color=newColor

    def showCar(self):
        print("car = {} = {} , fuel ={} color {}" .format( self.brand,self.model,self.fuel,self.color))


class  SUV(Car):
        def __init__(self,brand,model,fuel,color,transmission,turbo):
             #inheritind propeties of parent class
             Car.__init__(self,brand,model,fuel,color)
             self.transmission=transmission
             self.turbo = turbo
        def showCar(self):
             print("car = {} = {} , fuel ={} color {}, transmission = {}, turbo True / False = {}" 
                   .format(self.brand,self.model,self.fuel,self.color,self.transmission,self.turbo))
 

audiq3 = SUV("audi","q3","diesel","white,","automatic",True)

print(audiq3.getColor())

audiq3.setColor("BLACK")

#FUNCTION OVERRIDEN IN CHILD CLASS
print(audiq3.showCar())