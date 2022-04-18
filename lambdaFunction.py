"""
@author: ahmet

*lambda functions are functions without a name
*Unlike functions with "def()" and "return" syntax,lambda returns an expression without a "return" statement
*Lambda can be defined anywhere a function is expected without having to assign a variable


If we want to write a function that takes the cube;

y2 and y functions values ​​work the same.
    
"""



y = lambda x : x ** 3
print(y(8))



def y2(x):
    x **= 3
    return x
print(y2(8))



print(y2(5)==y(5))



'''
[Out]:
    512
    512
    True
'''
