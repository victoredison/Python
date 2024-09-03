#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' an exercise of @property decorator '

__author__ = 'victor yu'

# Use @property to add width and height attributes to a Screen object, as well as a read-only attribute resolution:
# python
# 
# class Screen(object):
#     pass

# # Test:
# s = Screen()
# s.width = 1024
# s.height = 768
# print('resolution =', s.resolution)
# if s.resolution == 786432:
#     print('Test passed!')
# else:
#     print('Test failed!')


class Screen(object):
    def __init__(self):
       self.__width  = None
       self.__height = None
       self.__resolution=None

        

    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        self.__width=value
        self.__update_resolution()
    
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        self.__height=value
        self.__update_resolution()

    @property
    def resolution(self):
        return self.__resolution
    
    def __update_resolution(self):
        if self.__width is not None and self.__height is not None:
            self.__resolution = self.__width * self.__height
        else:
            self.__resolution = None

# 测试:
s = Screen()
s.width = 1024
s.height = 768
print('resolution =', s.resolution)
if s.resolution == 786432:
    print('Test passed!')
else:
    print('Test failed!')