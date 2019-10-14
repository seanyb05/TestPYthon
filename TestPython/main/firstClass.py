'''
Created on Oct 13, 2019

@author: seany
'''

class Person:
    '''
    classdocs
    '''
    def __init__(self, name,age):
        '''
        Constructor
        '''
        self.name = name
        self.age = age


if __name__== "__main__":
    p1 = Person("John", 36)
    print(p1.name)
    print(p1.age)