import numpy as np

#string = input('What is your favourite number?:\n')

#print(f"Your favourite number is {string}")

'''
value = input("Please enter a string:\n")
 
print(f'You entered {value}')
''' 

'''
num = 12
name = 'sam'

print("My number is {}, and my name is: {}".format(num,name))


i = 1
while i <5:
    print('i is: {}'.format(i))
    i = i+1
'''

#x = lambda a: a + 10
#print(x(5))
#x = lambda a,b : a * b
#print(x(5,6))
#x = lambda a, b, c : a + b + c
#print(x(5, 6, 2))


def myfunc(n):
    return lambda a: a * n 

mydoubler = myfunc(4)

print(mydoubler(11))