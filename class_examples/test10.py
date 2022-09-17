
class Banks():
    '''银行类'''

    def __init__(self,uname):
        self.__name = uname             #用户姓名
        self.__balance = 0              #开户金额
        self.__title = "zhongguo Bank"  #银行名称
        self.__rate = 6.9            #美元兑换人名币的汇率
        self.__service_charge = 0.01 #服务费

    def save_money(self, money):
        self.__balance += money
        print("存款 {} 元完成。".format(money))

    def withdraw_money(self,money):     #提款
        self.__balance -= money
        print("提款 {} 元完成。".format(money))

    def get_balance(self):
        print("{} 目前余额：{}".format(self.__name, self.__balance))

    def usa_to_rmb(self, usa_d):
        self.result = self.__cal_rate(usa_d)
        return self.result

    def __cal_rate(self, usa_d):
        return int(usa_d * self.__rate * (1 - self.__service_charge))


bank = Banks("bruce")
bank._var = 10000
print(bank._var)
bank.get_var()

bank.get_balance()
usadallor = 60
print(usadallor, "美金可以兑换",bank.usa_to_rmb(usadallor),"rmb")