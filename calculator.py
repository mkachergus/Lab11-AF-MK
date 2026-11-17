"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
import math
def square_root(a):
    try:
        return math.sqrt(a)
    except ZeroDivisionError:
        raise ZeroDivisionError
def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except ValueError:
        raise ValueError
# First example
def add(a, b): 
    return a+b
def sub(a, b):
    return a-b
def mul(a, b):
    return a*b
def div(a, b):
    if a==0:
        raise ZeroDivisionError
    return b/a
def log(a, b):
    if a<=0 or b<=0 or a==1:
        raise ValueError
    return math.log(b,a)
def exp(a, b):
    return a**b
print(add(2, 3))
print(sub(5, 2))
print(mul(3, 4))
print(div(2, 10))
print(log(2, 8))
print(exp(2, 3))
print(square_root(25))
print(hypotenuse(3, 4))