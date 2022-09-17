class Animal():
    '''动物基类'''

    def __init__(self,name):
        self.name = name
        print("{} is a animal.".format(self.name))


class Mammal(Animal):
    '''哺乳动物类，集成动物基类，扩展技能方法'''

    def __init__(self,name):
        super().__init__(name)
        print("{} is a warm-blooded animal.".format(name))

    def skill(self):
        print("{} can doing.".format(self.name))

class NonwingedMammal(Mammal):
    '''非飞行类哺乳动物，继承哺乳动物类'''

    def __init__(self,name):
        super().__init__(name)
        print("{} is a nonwinged mammal animal.".format(self.name))


    def skill(self):
        print("{} can't fly.".format(self.name))
        super().skill()

class NonMarneMammal(Mammal):
    '''非海洋类哺乳动物，继承哺乳动物类'''

    def __init__(self, name):
        super().__init__(name)
        print("{} is a nonmarne mammal animal.".format(self.name))


    def skill(self):
        print("{} can't swim.".format(self.name))
        super().skill()

class Dog(NonwingedMammal, NonMarneMammal):
    '''犬类动物继承，NonwingedMammal和NonMarneMammal'''

    def __init__(self,name="Dog"):
        super().__init__(name)
        print("Dog has 4 legs.")


    def skill(self):
        print("{} can bark.".format(self.name))
        super().skill()

if __name__ == '__main__':
    #1.测试init的顺序
    print("1.测试调用__init__的顺序")
    d=Dog()
    print("-"*30)

    #2.测试钻石模式
    print("\n2.测试钻石测试")
    d.skill()
    print("-" * 30)

    #3.查看类Dog的祖先树
    print("\n3.Dog 的祖先树：")
    for var in Dog.__mro__:
        print(var)

    #4.在测试super()
    print("\n4.再测试super()")
    bat = NonMarneMammal("Bat")
