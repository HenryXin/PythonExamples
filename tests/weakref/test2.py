import sys
import weakref
from test1 import SomeObject

obj = SomeObject()

reference = weakref.ref(obj)

print(reference)
print(reference())
print(obj.__weakref__)
print(sys.getrefcount(obj))

obj = None
print(reference)
print(reference())

