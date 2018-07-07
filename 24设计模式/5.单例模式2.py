#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def singleton(cls, *args, **kwargs):
    """单例模式"""
    __instances = {}
    __lock = Lock()

    def _singleton(*args, **kwargs):
        if cls not in __instances:
            __lock.acquire()
            __instances[cls] = cls(*args, **kwargs)
            __lock.release()
        return __instances[cls]
    return _singleton
# 2018 GitHub, Inc.
# 用法在类前面
@singleton
class Test