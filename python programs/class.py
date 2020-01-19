'''


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting!")

    def roll_over(self):
        print(f"{self.name} rolled over")
        


my_dog = Dog('Whillie', 6)
your_dog = Dog('Lucy', 3)

my_dog.sit()
my_dog.roll_over()

your_dog.sit()
your_dog.roll_over()

print(f"My dog's name is {my_dog.name}")
print(f"{my_dog.name} is {my_dog.age} years old")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old")
your_dog.sit()


'''

class computer:
    def config(self):
        print("i5 16gb 1TB")

comp1 = computer()
comp2 = computer()

comp1.config()
comp2.config()
#
# computer.config(comp1)
# computer.config(comp2)