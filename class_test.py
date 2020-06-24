#!/user/bin/python
# -*- coding:utf-8 -*-
import os
import sys

class myclass(object):
    static_version=10.0

    def myclass(self):
        print ('init my class 1')


    def myclass(self, x, y):
        print ('init my class 2'+x+y)

    def sayhello(self):
        print ('Hello')

    def calc(self, x):
        return (x+x)

    def err(self):
        try:
            x=y=1
            z=0
            x=y/z
        except IOError as e:
            print ('IO error!')
        except ValueError as e:
            print ('Value error')

class mysubclass(myclass,object):
    pass

if __name__=="__main1__":
    obj1=myclass()
    obj1.sayhello()
    obj2=myclass("123 ", " 456")
    obj2.sayhello();

def main():
    print ('run main function')
    cls1 =myclass()
    cls1.sayhello()
    print (cls1.calc(100))
    sub1=mysubclass()
    sub1.sayhello()
    print (sub1.calc(100))
    
main()