# coding: utf-8


# 装饰器模式
import functools


def memoize(fn):
    known = dict()

    @functools.wraps(fn)  # 封装原函数信息.
    def memoizer(*args):
        if args not in known:
            known[args] = fn(*args)
        return known[args]

    return memoizer


@memoize
def nsum(n):
    '''返回前n个数字的和'''
    assert(n >= 0), 'n must be >= 0'
    return 0 if n == 0 else n + nsum(n-1)  # 注意:尾递归.


@memoize
def fibonacci(n):
    '''返回斐波那契数列的第n个数'''
    assert(n >= 0), 'n must be >= 0'  # todo::assert expression1 [, expression2]
                                      # todo::expression1的值会返回Ture或者False，当值为False的时候会引发AssertionError，而expression2是可选的，用来传递具体的异常信息。
    return n if n in (0, 1) else fibonacci(n-1) + fibonacci(n-2)  # 注意:二分尾递归.

if __name__ == '__main__':
    from timeit import Timer
    measure = [{'exec': 'fibonacci(100)', 'import': 'fibonacci',
                'func': fibonacci}, {'exec': 'nsum(200)', 'import': 'nsum',
                                     'func': nsum}]
    for m in measure:
        t = Timer('{}'.format(m['exec']), 'from __main__ import \
            {}'.format(m['import']))
        print('name: {}, doc: {}, executing: {}, time: \
            {}'.format(m['func'].__name__, m['func'].__doc__,
                       m['exec'], t.timeit()))
