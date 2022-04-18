"""
version : 3. 7. 1
@author: ahmet

Care should be taken when giving the parameter of the function.
"""

#If the value is not named, it works index number to the parameter.
def oper(val1=3, val2=9, val3=5):
    
    value = val1 * val3 / val2
    
    return value

value1 = oper(4, 8, 10)

print(value1)


'''If the order of the given parameter is mixed, but the names match 
the function names, the names are taken into account...'''

def func(val1=3, val2=9, val3=5):
    
    value = val1 * val3 / val2
    
    return value

value2 = func(val2 = 4, val3=8, val1=10)

print(value2)

#missing parameters : system runs without error if there is parameter that satisfies the rest

def luck(val1=3, val2=9, val3=5):
    
    value = val1 * val3 / val2
    
    return value

value3 = luck(10,2)

print(value3)







