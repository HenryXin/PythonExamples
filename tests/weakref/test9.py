import weakref

class Logger:
    def __init__(self, name):
        self.name = name

_logger_cache = weakref.WeakValueDictionary()

def get_logger(name):
    if name not in _logger_cache:
        l = Logger(name)
        _logger_cache[name] = l
    else:
        l = _logger_cache[name]

    return l
a = get_logger("first")
b = get_logger("second")
print(a is b)
#print(a)
#print(b)
c = get_logger("first")
print(a is c)
