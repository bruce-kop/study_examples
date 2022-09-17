class Student:
    '''
    Dec：一个简单的学生类
    '''
    def __init__(self,name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print("student name is :", self.name)

s = Student("xiaoming")
print(callable(s))
s()