import logging
a = logging.getLogger("first")
b = logging.getLogger("second")
print(a is b)

c = logging.getLogger("first")
print(a is c)
