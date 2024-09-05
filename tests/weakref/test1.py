import sys

class SomeObject:
    def __del__(self):
        print(f"(Deleting {self=}")

obj = SomeObject()

print(sys.getrefcount(obj))
obj2 = obj
print(sys.getrefcount(obj))

obj = None
obj2 = None
