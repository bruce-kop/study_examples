import gc
import sys
import ctypes

# 通过内存地址去访问没有引用的对象（unreachable objects）
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


gc.enable()  # 禁用分代回收算法
lst = []
lst.append(lst)
lst_address = id(lst)
del lst

object_1, object_2 = {}, {}

object_1['obj2'] = object_2
object_2['obj1'] = object_1
obj_address = id(object_1)
del object_1, object_2

print(gc.get_count())
# 手动对象回收
#gc.collect()
print(gc.isenabled())

# 获取对象引用数量
print(PyObject.from_address(obj_address).refcnt)

print(PyObject.from_address(lst_address).refcnt)

import time
time.sleep(100)
# 获取对象引用数量
print(PyObject.from_address(obj_address).refcnt)

print(PyObject.from_address(lst_address).refcnt)