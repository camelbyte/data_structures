import math # Import the math module to use the math functions.



def subtract(args, kwargs):
    return args - kwargs


def add(args, kwargs):
    return float(args + kwargs)


def multiply(args, kwargs):
    return args * kwargs


def divide(args, kwargs):
    return args / kwargs


def square_root(args):
    return math.sqrt(args)


def power(args, kwargs):
    return args ** kwargs


def factorial(args):
    return math.factorial(args)


def sin(args):
    return math.sin(args)


def cos(args):
    return math.cos(args)


"""

# examples

Arguments: Pass a integer or float value to the function.

print(square_root(25))
print(power(5, 5))
print(factorial(5))
print(sin(3.90))
print(cos(3.90))
print(subtract(5, 5))
print(square_root(25))
print(add(5, 5))
print(multiply(5, 5))
print(divide(5, 5))


Output: The result of the function called in the form of an integer or float.

"""





