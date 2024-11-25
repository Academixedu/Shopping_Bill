class MyClass:
    def __init__(self, number_of_items):
        self.number_of_items = number_of_items
        self.items = []  
        self.total_items_price = 0
        self.each_item()  
        self.calculate_total_price()  
        self.discount_value = self.discount()  
        
print("Welcome to the Shopping Bill Calculator!")
def each_item(self):
        for _ in range(self.number_of_items):
            name = input("Enter item name: ")
            price = int(input("Enter the price of the item: "))
            self.items.append({"name": name, "price": price})  
def calculate_total_price(self):
        self.total_items_price = 0
        
        for item in self.items:
            self.total_items_price += item["price"]

def discount(self):
        loyalty_card = input("Do you have a loyalty card? (yes/no): ")
        seasonal_offer = input("Is there a seasonal offer? (yes/no): ")
        both_offer = input("Do you have both offers? (yes/no): ")
        
        x = self.total_items_price * 0.1  
        y = self.total_items_price * 0.05  
        z = x + y  
        
        if both_offer.lower() == "yes":
            return z
        elif loyalty_card.lower() == "yes":
            return x
        elif seasonal_offer.lower() == "yes":
            return y
        else:
            return 0  

number_of_items = int(input("How many items would you like to purchase? "))

p1 = MyClass(number_of_items)

print("Receipt:")
print("Shopping cart: ")
for item in p1.items:
    print(f"Item: {item['name']}, Price: {item['price']}")  
print(f"Number of items: {p1.number_of_items}")
print(f"Total price (before discount): {p1.total_items_price}")
print(" ")
print(f"Discount applied: {p1.discount_value}")
print(f"Total price (after discount): {p1.total_items_price - p1.discount_value}")
