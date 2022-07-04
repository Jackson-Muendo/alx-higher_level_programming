#!/usr/bin/python3

'''
Docstring goes here
'''


def lookup(obj):
    ''' lookup fn '''
    return dir(obj)


if __name__ == '__main__':
    lookup = __import__('0-lookup').lookup

    class MyClass1(object):
        pass

    class MyClass2(object):
        my_attr1 = 3

        def my_meth(self):
            pass

    print(lookup(MyClass1))
    print(lookup(MyClass2))
    print(lookup(int))
