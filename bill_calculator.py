
# Objective
# Create a Python program that acts as a Shopping Bill Calculator and demonstrates key Python concepts, including arrays (lists), control flow, functions, and file handling. The program will allow the user to input items and their prices, apply discounts based on specific conditions, and generate a receipt stored in a text file. Additionally, use Git to manage the version control of the project.

# Requirements
# 1. Program Functionality
# Shopping Cart Input:

# Prompt the user to input the number of items they wish to purchase.
# For each item, prompt the user to enter the name and price.
# Discount Calculation:

# Apply a loyalty card discount (e.g., 10%) if the user has a loyalty card.
# Apply an additional seasonal offer discount (e.g., 5%) if there is a seasonal offer.
# Total Price Calculation:

# Calculate the total price of all items before and after discounts.
# Display the total price, discount applied, and final price after discounts.
# Generate and Save Receipt:

# Create a receipt and Print it in Console :
# A list of all items with their prices.
# Total price before and after discount.
# Discount applied.
# Final price after discount.
# 2. Python Concepts to Implement
# Arrays (Lists): Store and manage the items in the shopping cart.
# Control Flow: Use if-else statements to apply discounts based on user input.
# Functions: Create functions to handle specific tasks such as calculating the total price, applying discounts, and saving the receipt.
# 3. Git Version Control Tasks
# Initialize Git Repository:

# Initialize a Git repository using git init.
# Commit Changes:

# Track your changes using git add and commit them using git commit -m "message".
# Branching and Merging:

# Prepare a Branch and Complete The Code and Raise PR from That Branch
# Push to Remote Repository (optional):

# Create a remote repository (e.g., GitHub) and push your project using:
# git remote add origin <repository-url>
# git push -u origin main
# 4. Submission Guidelines
# Submit the Python file bill_calculator.py that implements the shopping bill calculator.
# Provide the GitHub repository URL or a zip file of the project folder.
# Ensure that the program works as expected and the receipt is saved correctly in the text file.
# Evaluation Criteria
# Python Basics:

# Correct use of arrays (lists), control flow, and functions.
# Accurate calculation of discounts and total price.
# Proper file handling to store the receipt.
# Git Basics:

# Correct usage of Git commands (git init, git add, git commit, git merge, etc.).
# Proper commit history and branching.
# Clear project structure and clean commits.
# Sample Output
# Welcome to the Shopping Bill Calculator!

# How many items would you like to purchase? 3

# Enter item name: Shirt
# Enter price for Shirt: 20

# Enter item name: Jeans
# Enter price for Jeans: 40

# Enter item name: Shoes
# Enter price for Shoes: 60

# Shopping Cart:
# Shirt: $20.00
# Jeans: $40.00
# Shoes: $60.00
# Do you have a loyalty card? (yes/no): yes
# Loyalty card applied! 10% discount added.

# Is there a seasonal offer? (yes/no): yes
# Seasonal offer applied! 5% discount added.

# Total Price Before Discount: $120.00
# Discount Applied: 15.00%
# Final Price After Discount: $102.00


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
