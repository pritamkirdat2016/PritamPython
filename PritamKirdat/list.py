Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> lis=[12,16,3,6,'a']
>>> dir(lis)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>> len(lis)
5
>>> lis.append(['c',2,6,])
>>> lis
[12, 16, 3, 6, 'a', ['c', 2, 6]]
>>> lis.extend()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    lis.extend()
TypeError: extend() takes exactly one argument (0 given)
>>> lis.extend(['f',8,9])
>>> lis
[12, 16, 3, 6, 'a', ['c', 2, 6], 'f', 8, 9]
>>> help(lis.extend)
Help on built-in function extend:

extend(iterable, /) method of builtins.list instance
    Extend list by appending elements from the iterable.

>>> lis.clear()
>>> lis'
SyntaxError: EOL while scanning string literal
>>> lis
[]
>>> lis.copy(['a',6,8,5])
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    lis.copy(['a',6,8,5])
TypeError: copy() takes no arguments (1 given)
>>> lis.copy([4,7,46])
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    lis.copy([4,7,46])
TypeError: copy() takes no arguments (1 given)
>>> l1=[1,6,3]
>>> l2.copy(l1)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l2.copy(l1)
NameError: name 'l2' is not defined
>>> l1.copy(l2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    l1.copy(l2)
NameError: name 'l2' is not defined
>>> l2.copy(l1)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    l2.copy(l1)
NameError: name 'l2' is not defined
>>> l1
[1, 6, 3]
>>> help(l1.copy)
Help on built-in function copy:

copy() method of builtins.list instance
    Return a shallow copy of the list.

>>> l2=l1.copy()
>>> l2
[1, 6, 3]
>>> l2.append(['2,4'])
>>> l2
[1, 6, 3, ['2,4']]
>>> l1
[1, 6, 3]
>>> newl=l1[:]
>>> newl
[1, 6, 3]
>>> li
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    li
NameError: name 'li' is not defined
>>> l1
[1, 6, 3]
>>> newl.append(['dog'])
>>> newl
[1, 6, 3, ['dog']]
>>> l1
[1, 6, 3]
>>> l1.count(3)
1
>>> l1.index(1)
0
>>> l1.index(6)
1
>>> l1.index(77)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    l1.index(77)
ValueError: 77 is not in list
>>> l1.insert(2,['h'])
>>> l1
[1, 6, ['h'], 3]
>>> l1.pop('h')
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    l1.pop('h')
TypeError: 'str' object cannot be interpreted as an integer
>>> l1.pop(2)
['h']
>>> l1
[1, 6, 3]
>>> l1.remove(3)
>>> l1
[1, 6]
>>> l1.reverse()
>>> l1
[6, 1]
>>> l1.sort()
>>> l1
[1, 6]
>>> l1.sorted()
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    l1.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> l1.sorted()
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    l1.sorted()
AttributeError: 'list' object has no attribute 'sorted'
>>> sorted(l1)
[1, 6]
>>> 
