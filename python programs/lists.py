cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nHere is the original list:")
print(cars)

print("Here is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

cars.reverse()

print(len(cars))

magicians = ['alice', 'david', 'carolinda']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick! \n")

print(f"{magician.title()}, Thanks for the show!")

for value in range(1,6):
    print(value)


numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2,11,2))
print(even_numbers)