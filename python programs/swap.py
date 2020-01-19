a = 5
b = 6

'''
temp = a
a = b
b = temp

a = a^b # 11   ^ is xor here
b = a^b #5
a = a^b #6
'''
print("Before swap a = %d and b = %d" %(a,b))
a,b = b,a
print("After swap a = %d and b = %d" %(a,b))

print()