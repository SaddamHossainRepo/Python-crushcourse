class phone:
    def call(self):
        print("call")

    def message(self):
        print("message")


class samsung(phone):
    def photo(self):
        print("photo")


s = samsung()
s.call()
s.message()
print(issubclass(phone,samsung))