#print("Jakkama")

''' def succ(x):
    print(x + 1)
    #return x + 1

successor = succ

del succ

successor(11) '''

''' def f():

    def g():
        print("Hi, it's me 'g'")
        print("Thanks for calling me")
    

    print("This is the function 'f'")
    print("I am calling 'g' now:")
    g()

f() '''

''' def temperature(t):
    def celcius2farenheat(x):
        return 9*x / 5 + 32
    
    result = "it's " + str(celcius2farenheat(t)) +  " degress!"
    return result

print(temperature(11)) '''

''' def g():
    
    print("Hi, it's me 'g'")
    print("Thanks for calling me")

def f(function):
    print("Hi, it's me 'f'")
    print("I will call 'func' now")
    function()
    print("func's real name is " + function.__name__)

f(g) '''

import math

''' def foo(func):
    print("The function " + func.__name__ + " was passed to foo")
    res = 0
    for x in [1,2,2.7]:
        res += func(x)
    return res
print(foo(math.sin))
print(foo(math.cos)) '''

''' def f(x):
    def g(y):
        return y + x + 3 
    return g

nf1 = f(1)
#nf2 = f(3)

print(nf1(2))
#print(nf2(7)) '''

''' def polynomial_creator(a,b,c):
    def polynomial(x):
        return a * x**2 + b * x + c

    return polynomial

p1 = polynomial_creator(2, 3, -1)
p2 = polynomial_creator(-1, 2, 1)

for x in range(-2, 2, 1):
    print(x, p1(x), p2(x)) '''


''' def polynomial_creator(*coefficients):
    """ coefficients are in the form a_0, a_1, ... a_n 
    """
    def polynomial(x):
        res = 0
        for index, coeff in enumerate(coefficients):
            res += coeff * x** index
        return res
    return polynomial
  
p1 = polynomial_creator(4)
p2 = polynomial_creator(2, 4)
p3 = polynomial_creator(2, 3, -1, 8, 1)
p4  = polynomial_creator(-1, 2, 1)


for x in range(-2, 2, 1):
    print(x, p1(x), p2(x), p3(x), p4(x)) '''



''' def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        func(x)
        print("After calling " + func.__name__)
    return function_wrapper

def foo(x):
    print("Hi, foo has been called with " + str(x))

print("We call foo before decoration:")
foo("Hi")
    
print("We now decorate foo with f:")
foo = our_decorator(foo)

print("We call foo after decoration:")
foo(42) '''

''' def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

@our_decorator
def succ(n):
    return n + 1

succ(10) '''

''' def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)

print(call_foo_with_arg(foo, 3)) '''
''' 
def parent():
    print("Printing from the parent() function.")

    def first_child():
        #return "Printing from the first_child() function."

        print("Printing from the first_child() function.")

    def second_child():
        return "Printing from the second_child() function."

    first_child() '''

        #print(first_child())
        #print(second_child())
#parent()
    #first_child()
''' 

def parent(num):
    
    def first_child():
        return "Printing from the first_child() function."

    def second_child():
        return "Printing from the second_child() function."

    try:
        assert num == 10
        return first_child
    except AssertionError:
        return second_child

foo = parent(10)
bar = parent(11)

print(foo)
print(bar)

print(foo())
print(bar()) '''


''' def my_decorator(some_function):
    
    def wrapper():

        print("Something is happening before some_function() is called.")

        some_function()

        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!") '''


''' import time
def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "\n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("\nSum of all the numbers: " + str((sum(num_list))))

print(my_function()) '''


''' just_some_function = my_decorator(just_some_function)

just_some_function() '''


''' from time import sleep

def sleep_decorator(function):

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_nu mber(num))''' '''


def my_Decorator(msg='aaaaaaaaaaaa'):
    
    def decorated(func):
        print("hai",msg)
    
        def wrapper(*args, **kwargs):
            print("Calling before function")
            func(*args, **kwargs)
            print("Calling after function")

        return wrapper

    return decorated

@my_Decorator(msg='madam')
def printName(name):
    print(name)

printName('panni') '''


''' from math import sin, cos

def our_decorator(func):
    def function_wrapper(x):
        print("Before calling " + func.__name__)
        res = func(x)
        print(res)
        print("After calling " + func.__name__)
    return function_wrapper

sin = our_decorator(sin)
cos = our_decorator(cos)

for f in [sin, cos]:
    f(3.1415) '''



''' def argument_test_natural_number(f):
    def helper(x):
        if type(x) == int and x > 0:
            return f(x)
        else:
            raise Exception("Argument is not an integer")
    return helper
    
@argument_test_natural_number
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

for i in range(1,10):
	print(i, factorial(i))

print(factorial(-1)) '''


''' def call_counter(func):
    def helper(x):
        helper.calls += 1
        return func(x)
    helper.calls = 0

    return helper

@call_counter
def succ(x):
    return x + 1

print(succ.calls)
for i in range(10):
    succ(i)
    
print(succ.calls) '''



''' def evening_greeting(func):
    def function_wrapper(x):
        print("Good evening, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

def morning_greeting(func):
    def function_wrapper(x):
        print("Good morning, " + func.__name__ + " returns:")
        func(x)
    return function_wrapper

@evening_greeting
def foo(x):
    print(42)

foo("Hi") '''


''' def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator

@greeting("καλημερα")
def foo(x):
    print(42)

foo("Hi") '''

''' 
def greeting(expr):
    def greeting_decorator(func):
        def function_wrapper(x):
            print(expr + ", " + func.__name__ + " returns:")
            func(x)
        return function_wrapper
    return greeting_decorator


def foo(x):
    print(42)
    print(x)

greeting2 = greeting("καλημερα")
foo = greeting2(foo)
foo("Hi") '''


class Fibonacci:
    
    def __init__(self):
        self.cache = {}

    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[0] = 0
            elif n == 1:
                self.cache[1] = 1
            else:
                self.cache[n] = self.__call__(n-1) + self.__call__(n-2)
        return self.cache[n]

fib = Fibonacci()

for i in range(15):
    print(fib(i), end=", ")














    


    
