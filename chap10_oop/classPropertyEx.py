#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of class access restriction '

__author__ = 'victor yu'


# To count the number of students, you can add a class attribute to the Student class. Each time an instance is created, this attribute automatically increments:
# 
# class Student(object):
#     count = 0

#     def __init__(self, name):
#         self.name = name

# # Test:
# if Student.count != 0:
#     print('Test failed!')
# else:
#     bart = Student('Bart')
#     if Student.count != 1:
#         print('Test failed!')
#     else:
#         lisa = Student('Bart')
#         if Student.count != 2:
#             print('Test failed!')
#         else:
#             print('Students:', Student.count)
#             print('Test passed!')



class Student(object):
    count = 0

    def __init__(self, name):
        self.name = name
        Student.count=Student.count+1


if Student.count != 0:
    print('Test failed!')
else:
    bart = Student('Bart')
    if Student.count != 1:
        print('Test failed!')
    else:
        lisa = Student('Bart')
        if Student.count != 2:
            print('Test failed!')
        else:
            print('Students:', Student.count)
            print('Test passed!')


