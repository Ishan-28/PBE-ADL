class BuildProduct:
    def __init__(self):
        self.product_number = 0
        self.product_dictionary = {}    # Original Product dictionary, update this dictionary for adding products for website
        self.new_product_dictionary = {
            "ID": 0,
            "Name": "",
            "Price": 0,
            "Description": ""
        }

    def increase_item_number(self):
        self.product_number += 1

    def update_product_dictionary(self, product):
        self.product_dictionary[self.product_number] = product

    def take_user_input(self):
        product_id = int(input("Enter the product id: "))
        self.new_product_dictionary["ID"] = product_id
        name = input("Enter name: ")
        self.new_product_dictionary["Name"] = name
        price = int(input("Enter the product's price: "))
        self.new_product_dictionary["Price"] = price
        description = input("Enter the product description")
        self.new_product_dictionary["Description"] = description


# Dictionary for testing
product = {
    "ID": 1,
    "Name": "QR-Code",
    "Price": 10,
    "Description": "A customised QR Code sticker which stores data",
}

print(product)
#
# for fetch_id in product:
#     print(fetch_id)


