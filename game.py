
class Player():
    def __init__(self,name):
        self.__name = name
        self.__onlvl = onlvl
        
class Lvl():
    def __init__(self,inlvl,lvl1):
        self.__inlvl = inlvl
        self.__lvl1 = lvl1
        self.playersList = []
    def addplayers(self,urself):
        self.playersList.append(urself)

        
    def gonextlvl(self):
        self.__lvl1 += 1
        print(f"lvl is: {self.__lvl1} ")
class Plartform():
    def __init__(self,resourses):
        self.resourses = resourses
        
        
    def trade(self):
        self.resourses -= 5
        print(f"resourses is : {self.resourses}")
    def eat(self):
        self.resourses -= 10
        print(f"resourses is : {self.resourses}")
    def gonextlvl(self):
        self.resourses -= 3
        print(f"resourses is : {self.resourses}")

platform = Plartform(100)
                     
lvl = Lvl(2,1)
human1 = ("ivan",1)
human2 = ("petya",1)
human3 = ("petya",2)
human4 = ("petya",2)
human5 = ("petya",3)
human6 = ("petya",3)
human7 = ("petya",4)
human8 = ("petya",4)
human9 = ("petya",5)
human10 = ("petya",5)
human11 = ("petya",6)
human12 = ("petya",6)
human13 = ("petya",7)
human14 = ("petya",7)
human15 = ("petya",8)
human16 = ("petya",8)
human17 = ("petya",9)
human18 = ("petya",9)
human19 = ("petya",10)
human20 = ("petya",10)

lvl.addplayers(human1)
lvl.addplayers(human2)
lvl.addplayers(human3)
lvl.addplayers(human4)
lvl.addplayers(human5)
lvl.addplayers(human6)
lvl.addplayers(human7)
lvl.addplayers(human8)
lvl.addplayers(human9)
lvl.addplayers(human10)
lvl.addplayers(human11)
lvl.addplayers(human12)
lvl.addplayers(human13)
lvl.addplayers(human14)
lvl.addplayers(human15)
lvl.addplayers(human16)
lvl.addplayers(human17)
lvl.addplayers(human18)
lvl.addplayers(human19)
lvl.addplayers(human20)

for i in range (1,10):
    print("U have 3 option:\n 1.trade \n 2.eat extra \n 3.go next lvl")
    userinput = input("choose someone: ")
    
    if platform.resourses <= 0:
        print("все на нынешнем уровне и ниже умерли поздравляю!! \n ______game end ______")
        break
    elif userinput == 1:
        platform.trade()
    elif userinput == 2:
        platform.eat()
    else:
        platform.eat()
        lvl.gonextlvl()
    