
'''
import sys

sys.setrecursionlimit(10)
print(sys.getrecursionlimit())

i = 0
def greept():
    global i
    i = i+1
    print("Hello",i)
    greept()

greept()

'''


def fact(n):
    if n==0:
        return 1

    return n*fact(n-1)


result = fact(int(input("Enter the number:")))
print(result)





'''

import sys
sys.setrecursionlimit(10)

print(sys.getrecursionlimit())

i = 0

def rec():
    global i
    i = i+1
    print("Hello",i)
    rec()

rec()

'''
