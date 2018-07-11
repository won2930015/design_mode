#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# http://ginstrom.com/scribbles/2008/11/06/generic-adapter-class-in-python/

import os


class Dog(object):  # 狗
    def __init__(self):
        self.name = "Dog"

    def bark(self):
        return "woof!"


class Cat(object):  # 猫
    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow!"


class Human(object):  # 人
    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "'hello'"


class Car(object):  # 车
    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "vroom%s" % ("!" * octane_level)


class Adapter(object):  # 适配器
    """
    Adapts an object by replacing methods.
    通过替换方法来调整对象
    Usage:
    dog = Dog
    dog = Adapter(dog, dict(make_noise=dog.bark))
    """
    def __init__(self, obj, adapted_methods):
        """We set the adapted methods in the object's dict"""
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        """All non-adapted calls are passed to the object"""
        return getattr(self.obj, attr)


def main():
    objects = []
    dog = Dog()
    objects.append(Adapter(dog, dict(make_noise=dog.bark)))
    cat = Cat()
    objects.append(Adapter(cat, dict(make_noise=cat.meow)))
    human = Human()
    objects.append(Adapter(human, dict(make_noise=human.speak)))
    car = Car()
    car_noise = lambda: car.make_noise(3)
    objects.append(Adapter(car, dict(make_noise=car_noise)))

    for obj in objects:
        print("A", obj.name, "goes", obj.make_noise())


if __name__ == "__main__":
    main()

