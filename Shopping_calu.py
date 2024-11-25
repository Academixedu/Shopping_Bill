
def calculate_total(cart):
    return sum(item['price'] for item in cart)

def apply_discounts(total, loyalty_card, seasonal_offer):
    discount_percentage = 0
    if loyalty_card:
        discount_percentage += 10  
    if seasonal_offer:
        discount_percentage += 5  
    discount = (discount_percentage / 100) * total
    final_price = total - discount
    return discount, final_price

def receipt(cart, total, discount, final_price):
    print("Bill for total shopping ")
    print("Items Purchased:")
    for item in cart:
        print(f"{item['name']}: ₹{item['price']:.2f}")
    print(f"\nTotal Price Before Discount: ₹{total:.2f}")
    print(f"Discount Applied: ₹{discount:.2f}")
    print(f"Final Price After Discount: ₹{final_price:.2f}")

def main():
    print("Welcome to the Shopping Bill Calculator")
    
    num_items = int(input("Give the number to the count to purchage "))
    cart = []
    for _ in range(num_items):
        name = input("\nEnter item name: ")
        price = float(input(f"Enter price for {name}: "))
        cart.append({'name': name, 'price': price})
    
    print("Shopping Cart:")
    for item in cart:
        print(f"{item['name']}: ₹{item['price']:.2f}")
    
    loyalty_card = input("Do you have a loyalty card? (yes/no): ")== "yes"
    seasonal_offer = input("Is there a seasonal offer? (yes/no): ")== "yes"
    
    total = calculate_total(cart)
    discount, final_price = apply_discounts(total, loyalty_card, seasonal_offer)
    
    print(" Complete  Bill recept")
    print(f"Total Price Before Discount: ₹{total:.2f}")
    print(f"Discount Applied: ₹{discount:.2f}")
    print(f"Final Price After Discount: ₹{final_price:.2f}\n")
    
    receipt(cart, total, discount, final_price)

if __name__ == "__main__":
    main()


