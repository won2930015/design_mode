#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Singleton
'''


class Singleton(object):
    ''' A python style singleton '''

    def __new__(cls, *args, **kw):
        if not hasattr(cls, '_instance'):
            org = super(Singleton, cls)
            #cls._instance = org.__new__(cls, *args, **kw)
            # 为何带参数会提示object() takes no parameters???(对象()不接受参数.)
            cls._instance = org.__new__(cls)

        return cls._instance


if __name__ == '__main__':
    class SingleSpam(Singleton):  # 继承单例类只能实例化一个实例.
        def __init__(self, s):
            self.s = s

        def __str__(self):
            return self.s

s1 = SingleSpam('spam')
print(id(s1), s1)
s2 = SingleSpam('spa')
print(id(s2), s2)
print(id(s1), s1)

