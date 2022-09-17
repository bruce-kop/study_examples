
class Student:
    count = 10
    def __init__(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    @staticmethod
    def print_string():
        print("hello world.")

    @classmethod
    def print_name(cls):
        print("class method ",cls.count)
        cls.print_string()

   #class end

def print_var():
    print(Student.count)


    s1 = Student("xiao zhang")
    s1.set_age(20)
    s1.print_name()

    print(s1.age)
    s1.count = 5
    print(s1.count)
    print(s1.name)
    print("-"*30)
    print(Student.count)

    s2 = Student("xiao huang")
    print(s2.count)

print_var()