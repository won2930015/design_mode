#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    # 注册对象
    def register_object(self, name, obj):
        """Register an object"""
        self._objects[name] = obj

    # 移除注册对象
    def unregister_object(self, name):
        """Unregister an object"""
        del self._objects[name]

    # 克隆
    def clone(self, name, **attr):
        # *允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
        # **,关键字参数允许你传入0个或任意个含参数名的参数,这些关键字参数在函数内部自动组装为一个dict。
        # todo https://www.cnblogs.com/xujiu/p/8352635.html
        """Clone a registered object and update inner attributes dictionary"""
        obj = copy.deepcopy(self._objects.get(name))
        obj.__dict__.update(attr) # todo https://blog.csdn.net/xiaolewennofollow/article/details/51455185
        return obj


def main():
    class A:
        pass

    a = A()
    prototype = Prototype()
    prototype.register_object('a', a)
    b = prototype.clone('a', a=1, b=2, c=3)

    print(a)
    print(b.a, b.b, b.c)


if __name__ == '__main__':
    main()
