# Python provides a sum() function that can accept a list and return the sum. 
# Please write a prod() function that can accept a list and use reduce() to calculate the product:

# from functools import reduce

# def prod(L):
#     pass

# print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
# if prod([3, 5, 7, 9]) == 945:
#     print('Test passed!')
# else:
#     print('Test failed!')


from functools import reduce

def prod(L):
    def fn(x,y):
        return x*y
    return reduce(fn, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


