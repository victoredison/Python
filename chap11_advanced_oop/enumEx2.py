#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of @property decorator '

__author__ = 'victor yu'

# Modify the gender attribute of the Student class to be an enumeration type, which can avoid using strings:
# python
# 
# from enum import Enum, unique

# class Gender(Enum):
#     Male = 0
#     Female = 1

# class Student(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender

# # Test:
# bart = Student('Bart', Gender.Male)
# if bart.gender == Gender.Male:
#     print('Test passed!')
# else:
#     print('Test failed!')



from enum import Enum, unique

@unique
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender: Gender):
        self.name = name
        self.gender = gender

# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('Test passed!')
else:
    print('Test failed!')
