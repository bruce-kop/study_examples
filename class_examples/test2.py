class Student(object):
    count = 80
    course = ["english", "chinese"]
    name = "xiao ming"
    def __init__(self, name):
        self.name = name

    def set_age(self,age):
        self.age = age


s1 = Student("zhang san")

print(s1.name)
print(Student.name)



