class User:
    #hidden password
    __password="abc_123"

    def __init__ (self,name,email,username):
        self.name=name
        self.email=email
        self.username=username
    def fun(self):
        print(self.__password)
       

user1=User("haya", "hayaaslam@outlook.com","hayaaa")
print(user1.name)
#print(user1.__password)
user1.fun()