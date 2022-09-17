
from utils import *
def verify_phone(phone):
    # A regular expression for the mobile phone number format
    reg = '^1(3[0-9]|4[5,7]|5[0,1,2,3,5,6,7,8,9]|6[2,5,6,7]|7[0,1,7,8]|8[0-9]|9[1,8,9])\d{8}$'
    if not re.match(reg, phone):
        print("phone is invalid.")
    else:
        print("phone is valid.")

verify_phone("13712345678")
print(os.name)
print(sys.path)