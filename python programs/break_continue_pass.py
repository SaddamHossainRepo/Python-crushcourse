
# x = int(input("How many candies you want:"))
# av = 5
# i = 1
# while i <= x:
#     if i > av:
#         print("We are out of stock")
#         break

#     print("Candy")
#     i = i+1


# print("Bye")



# for i in range(1,101):

#     if i %3 == 0 and i%5==0:# skip the values whick=h are divisible by 3 and(both) 5
#         continue
#     print(i)

# print("Bye")



# or is used for skipping the number which are divisible by 3 or 5


# for i in range(1,101):
#     if(i%2!=0):
#         pass#pass means just ignore it

#     else:
#         print(i)

# print("\nBye")


x = int(input("How many candies do you want?"))

av = 3

i = 1
while i <= x:
    if i > av:
        break

    print("candy")
    i = i+1

print("Bye")