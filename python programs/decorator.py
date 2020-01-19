
# Decorator allows us to add extra functionality to the existing function without changing it

'''

def div(a,b):
    print(a/b)

div(2,4)

'''

'''
def div(a,b):
    print(a/b)


def smart_div(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)

    return inner


div1 = smart_div(div)

div1(2,4)

'''

import time

def calc_square(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number)
    end = time.time()
    print("calc _suare took" +str((end-start)*1000) + "mil sec")
    return result


def calc_cube(numbers):
    start = time.time()
    result = []
    for number in numbers:
        result.append(number*number*number)
    end = time.time()
    print("calc cube took" + str((end - start) * 1000) + "mil sec")
    return result

array = range(1,1000)
out_square = calc_square(array)
out_cube = calc_cube(array)