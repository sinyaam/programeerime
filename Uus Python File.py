from abc import ABC 
import random
class Human(ABC):
    def __init__(self,name,strength):
        self.name = name
        self.strength = strength
    
    def talkTO(self,userinput):
        print(f"{self.name}:")
        print(userinput)
        
class Villager(Human):
    def __init__(self,name,strength):
        self.ready_for_war = random.choice([True, False])
        super().__init__(name , strength)
class Village():
    def __init__(self):
        self.villagerList = []
        self.friendly = random.choice([True, False])
    def add(self,villager):
        self.villagerList.append(villager)
    def remove(self,villager):
        self.villagerList.remove(villager)
class Gladiator(Human):
    def __init__(self,name , strength):
        self.legion = []
        super().__init__(name , strength)
    def legionCheck(self):
        for i in self.legion:
            print(i)
    def treneravat(self):
        for o in self.legion:
            o.strength += 2
        for u in self.legion:
            print(f"{u.name} , сила:{u.strength}")
    def villagercheck(self,villager):
        
        if len(self.legion) <= 10:
            if villager.strength >= 5 and villager.ready_for_war:
                self.legion.append(villager)
                print(f"{villager.name} , успешно завербован")
            else:
                print("не готов или не хватает силы")
        else:
            print("legion is full")
gladiator = Gladiator("Maksimus" , 20)
human1 = Villager("human1", 6)
human2 = Villager("human2", 3)
human3 = Villager("human3", 5)
human4 = Villager("human4", 7)
human5 = Villager("human5", 4)
human6 = Villager("human6", 3)
human7 = Villager("human7", 5)
human8 = Villager("human8", 4)
human9 = Villager("human9", 7)
village1 =Village()
village2 =Village()
village3 =Village()
village1.villagerList = [human1,human2,human3]
village2.villagerList = [human4,human5,human6]
village3.villagerList = [human7,human8,human9]
gladiator.villagercheck(human1)

print("бродим по деревьям")
if village1.friendly == True:
    for q in village1.villagerList:
        print("эта деревня дружелюбна")
        gladiator.villagercheck(q)
    else:
        print("эта деревня настроена враждебно")
gladiator.treneravat()