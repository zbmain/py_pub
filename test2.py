#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : zb
# @Time    : 2020/12/08 23:02

from zbmain.cls.singleton import *
from zbmain.cls.singleton import Singleton
class A(metaclass=SingletonType):
    def __init__(self,named):
        self.named = named
        print('init',self.named)

@Singleton
class B():
    def __init__(self, named):
        self.named = named
        print('init', self.named)



a = A('1')
b = A('2')
print(id(a),id(b))
print(a.named)

a = B._si
b = B('8')
print((a),(b))
print(id(a),id(b))
print(a.named)