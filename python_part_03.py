# class Customer:
#     def __init__(self, name, gender, address):
#         self.name = name
#         self.gender = gender
#         self.address = address

# class Address:
#     def __init__(self, city, pincode, state):
#         self.city = city
#         self.pincode = pincode
#         self.state = state

# add = Address("Kishoregaing", 232, "WB")
# cus = Customer("Tuhin", "Male", add)

# print(cus.address.pincode)


class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address

    def edit_profile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.change_add(new_city, new_pin, new_state)

class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def change_add(self, new_city, new_pin, new_state):
        self.city = new_city
        self.pincode = new_pin
        self.state = new_state

add = Address("Kishoregaing", 232, "WB")
cus = Customer("Tuhin", "Male", add)
cus.edit_profile("Sahin", "Karimgan", 234, "Niyamotpur")

print(cus.address.pincode)


#inheritance



