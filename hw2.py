class PC:
    #hidden password
    __password="AMITY123"

    def __init__ (self,name,PC_NUM):
        self.name=name
        self.PC_NUM=PC_NUM
    def fun(self):
        print(self.__password)
       

PC1=PC("anukriti", "23",)
print(PC1.name)
#print(PC1.__password)
PC1.fun()