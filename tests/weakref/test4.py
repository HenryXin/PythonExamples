import weakref

class Node:
    def __init__(self, value):
        self.value = value
        self._children = weakref.WeakValueDictionary()

    @property
    def children(self):
        return list(self._children.items())

    def add_child(self, key, child):
        self._children[key] = child

root = Node("parent")
n1 = Node("child one")
n2 = Node("child two")

root.add_child("n1", n1)
root.add_child("n2", n2)

print(root.children)

del n1
print(root.children)
