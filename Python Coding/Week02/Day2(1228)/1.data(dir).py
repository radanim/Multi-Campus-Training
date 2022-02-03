# 딕셔너리, 튜플, 리스트와 관련 메소드

my_list = []
print(dir(my_list)) #메소드 확인 방법

#__ => ( >=, >, <, <= , ==, != ) 사용 가능

#['__add__', '__class__', '__class_getitem__',
# '__contains__', '__delattr__', '__delitem__',
# '__dir__', '__doc__', '__eq__', '__format__',
# '__ge__', '__getattribute__', '__getitem__',
# '__gt__', '__hash__', '__iadd__', '__imul__',
# '__init__', '__init_subclass__', '__iter__',
# '__le__', '__len__', '__lt__', '__mul__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__',
# '__repr__', '__reversed__', '__rmul__',
# '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'append', 'clear',
# 'copy', 'count', 'extend', 'index', 'insert',
# 'pop', 'remove', 'reverse', 'sort']

my_tuple = ()
print(dir(my_tuple))
# ['__add__', '__class__', '__class_getitem__',
# '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__getnewargs__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__mul__', '__ne__', '__new__',
# '__reduce__', '__reduce_ex__', '__repr__', '__rmul__',
# '__setattr__', '__sizeof__', '__str__', '__subclasshook__',
# 'count', 'index']

my_dict = {}
print(dir(my_dict))
# ['__class__', '__class_getitem__', '__contains__',
# '__delattr__', '__delitem__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__',
# '__getitem__', '__gt__', '__hash__', '__init__',
# '__init_subclass__', '__ior__', '__iter__', '__le__',
# '__len__', '__lt__', '__ne__', '__new__', '__or__',
# '__reduce__', '__reduce_ex__', '__repr__', '__reversed__',
# '__ror__', '__setattr__', '__setitem__', '__sizeof__',
# '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys',
# 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault',
# 'update', 'values']