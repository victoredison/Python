# Use the map() function to convert a list of improperly formatted English names 
# into properly formatted names with the first letter capitalized and the rest in lowercase. 
# Input: ['adam', 'LISA', 'barT'], Output: ['Adam', 'Lisa', 'Bart']:

# def normalize(name):
#     pass

# # Test:
# L1 = ['adam', 'LISA', 'barT']
# L2 = list(map(normalize, L1))
# print(L2)



def normalize(name):

    return name.lower().capitalize()

# 测试:

L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)



