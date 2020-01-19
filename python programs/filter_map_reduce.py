'''

def is_even(n):
    return n%2==0


num = [10,34,42,5,2,13,43,12,45,22,33]

even = list(filter(is_even,num))

print(even)

'''

from functools import reduce

num = [10,34,42,5,2,13,43,12,45,22,33]

even = list(filter(lambda n: n%2==0,num))

double = list(map(lambda n : n*2,even))

sum = reduce(lambda a,b : a + b,double)

print(even)
print(double)
print(sum)









