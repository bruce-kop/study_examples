class Animal():
    '''抓住动物的基本特性'''

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self,food):
        print("It eat the {}".format(food))

    def sleep(self):
        print("It is sleeping.")


class Dog(Animal):
    '''继承Animal类，扩展run和bark的技能'''

    def run(self):
        print("{} is running.".format(self.name))


    def bark(self):
        print("wang wang.")


class Cat(Animal):
    '''继承Animal类，扩展新技能抓老鼠'''

    def CatchMouse(self):
        print("{} catching the Maouse.".format(self.name))


class Bird(Animal):
    '''继承Animal类，扩展了新技能fly'''

    def fly(self):
        print("{} is flying.".format(self.name))


class HuntingDog(Dog):
    '''继承Dog类，扩展新技能Hunting'''

    def hunt(self):
        print("{} is hunting.".format(self.name))


class TeddyDog(Dog):
    '''继承Dog类，扩展新技能Dance'''

    def __init__(self, name, age, origin="France"): #origin原产地
        super().__init__(name, age)
        self.origin = origin

    def dance(self):
        print('{} is dancing.'.format(self.name))


if __name__ == '__main__':
    teddy = TeddyDog("teddy", 5)
    teddy.dance()
    teddy.eat("bone")
    teddy.run()
    teddy.bark()

    hunting_dog = HuntingDog("hunting dog", 6)
    hunting_dog.hunt()

    bird = Bird("bird", 3)
    bird.fly()