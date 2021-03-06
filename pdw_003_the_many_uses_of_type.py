pdw_id   = 3
title    = "The many uses of type"
pub_date = (2010, 12, 3, 13, 27)
author   = "Kurt"
tags     = ('type', 'class')
"""
The ``type`` function is a gloriously powerful thing. Here are just a few
ways it can be put to use.

Use #1: call type to get the type of something
>>> type(5)
<type 'int'>
>>> type([])
<type 'list'>

Use #2: call type to construct a new type, more dynamic alternative to class keyword
>>> class A(object): pass
...
>>> bases = (A,)
>>> attributes = {"one": 1}
>>> B = type("B", bases, attributes)
>>> B().one
1

Use #3: type is the type of (new-style) classes, and built-ins
>>> class A(object): pass
...
>>> type(A)
<type 'type'>
>>> type(int)
<type 'type'>
>>> type(int) == type
True

Use #4: inherit from type to make a meta-class
>>> class Meta(type):
...    def __new__(cls, name, bases, dct):
...       print "hello meta world"
...       return type.__new__(cls, name, bases, dct)
...
>>> class A(object):
...    __metaclass__ = Meta
...
hello meta world
"""


