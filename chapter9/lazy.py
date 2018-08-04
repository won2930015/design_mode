# coding: utf-8


class LazyProperty:  # 懒惰代理...

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__
        print('function overriden: {}'.format(self.method))
        print("function's name: {}".format(self.method_name))

    def __get__(self, obj, cls):  # todo::https://www.cnblogs.com/saolv/p/6890645.html
        print('obj:{} ,cls:{}'.format(obj,cls))
        if not obj:
            return None
        value = self.method(obj)  # 通过类调用,这里的obj对象是Test的实例,被当做self传入到方法.
        print('value {}'.format(value))
        setattr(obj, self.method_name, value)  #obj:实例对象, self.method_name:属性, value:属性值
        return value


class Test:

    def __init__(self):
        self.x = 'foo'
        self.y = 'bar'
        self._resource = None

    @LazyProperty
    def resource(self):
        print('initializing self._resource which is: {}'.format(self._resource))
        self._resource = tuple(range(5))    # 代价大的
        return self._resource


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # 做更多的事情。。。
    print(t.resource)  # 第一次调用时,装饰器@LazyProperty 把.resource方法替换成.resource变量.并返回结果.
    print(t.resource)  # 第二次调用时,就是直接调用.resource变量.返回结果.实际只进行一次运算,可重复调用结果.的懒惰代理...

if __name__ == '__main__':
    main()
