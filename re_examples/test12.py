import re

s = "12℃"
p = "(\d+)℃"
m = re.match(p,s,re.S)
print(m.group(1))




