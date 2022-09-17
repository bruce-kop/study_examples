class Customer(object):
    '''客户类的DocString，客户说明以及注意事项'''
    name = "" #客户姓名
    nation = "" #国籍
    phone = "" #客户手机号
    sex = "male" #客户性别，初始值“male”

    #类实例化的初始化工作
    def __init__(self):
        print("class is init.")
        self.nation = "China"

    def __new__(cls, *args, **kwargs):
        print("class is new.")
        return super().__new__(cls, *args, **kwargs)


    #设置客户手机号
    def set_phone(self,phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

#end of class Customer

if __name__ == "__main__":
    cust = Customer()
    cust.set_phone("13712345678")
    print("设置手机号：{}".format(cust.get_phone()))

    print("默认国籍:{}".format(cust.nation))

    print("DocString: {}".format(Customer.__doc__))
