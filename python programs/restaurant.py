class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Name of the restaurant is {self.restaurant_name}")
        print(f"The type of the restaurant is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"the {self.restaurant_name} is now open")


restaurant = Restaurant('H2O','Halal')
print(f"The name of the restaurant is {restaurant.restaurant_name}")
print(f"The type of the restaurant is {restaurant.cuisine_type}")





