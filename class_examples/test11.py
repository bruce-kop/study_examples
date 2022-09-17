'''多态'''



class Animal():
    def __init__(self,name = ""):
        self.name = name

    def skill(self):
        print("I can eat.")


class Dog(Animal):
    def __init__(self, name = "Dog"):
        super().__init__(name)
        print("I am dog")

    def skill(self):
        print("I can eat.")
        print("I can bark.")
        print("I can run.")
        print("I can protect my master.")

class chicken(Animal):
    def __init__(self, name = "chicken"):
        super().__init__(name)
        print("I am chicken")

    def skill(self,name):
        print(name)
        print("I can eat.")
        print("I can crow.")
        print("I can fly.")
        return 0

    def skill(self,name,age):
        print("test skill",name,age)

class Game():
    def __init__(self):
        print("动物技能大赛")

    def set_player(self,player:Animal):
        self.player = player

    def show_skill(self):
        self.player.skill()


g = Game()
g.set_player(Dog())
g.show_skill()
print("*"*30)

#g.set_player(chicken())
#g.show_skill()
c = chicken()
c.skill("chick")