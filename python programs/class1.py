class employee:
    
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' +last + '@gmail.com' 
        

    def fullname(self):
        return '{} {}'.format(self.first,self.last)



#instance variables contain data that is unique to each instances
emp1 = employee('corey','schafer',50000)
emp2 = employee('baken','henry',40000)

# print(emp1)
# print(emp2)

print(emp1.email)
print(emp2.email)

# print('{} {}'.format(emp1.first,emp1.last))

print(emp1.fullname())