#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of class access restriction '

__author__ = 'victor yu'


# Hide the gender field of the Student object from external access, and replace it with get_gender() and set_gender(). Also, check the validity of the parameters:
# python
# 
# class Student(object):
#     def __init__(, name, gender):
#         self.name = name
#         self.gender = gender

# # Test:
# bart = Student('Bart', 'male')
# if bart.get_gender() != 'male':
#     print('Test failed!')
# else:
#     bart.set_gender('female')
#     if bart.get_gender() != 'female':
#         print('Test failed!')
#     else:
#         print('Test passed!')

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.__gender = gender
    
    def get_gender(self):
        return self.__gender
    
    def set_gender(self, gender):
        if gender != 'male' and gender !='female':
            raise ValueError('PLEASE ENTER A VALID GENDER')
        self.__gender=gender

# 测试:
bart = Student('Bart', 'male')
if bart.get_gender() != 'male':
    print('test failed!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('test failed!')
    else:
        print('test passed!')