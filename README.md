# **Assignment: Shopping Bill Calculator**

## **Objective**
Create a Python program that acts as a **Shopping Bill Calculator** and demonstrates key Python concepts, including arrays (lists), control flow, functions, and file handling. The program will allow the user to input items and their prices, apply discounts based on specific conditions, and generate a receipt stored in a text file. Additionally, use **Git** to manage the version control of the project.

## **Requirements**

### **1. Program Functionality**
1. **Shopping Cart Input**:
   - Prompt the user to input the number of items they wish to purchase.
   - For each item, prompt the user to enter the **name** and **price**.

2. **Discount Calculation**:
   - Apply a **loyalty card discount** (e.g., 10%) if the user has a loyalty card.
   - Apply an additional **seasonal offer discount** (e.g., 5%) if there is a seasonal offer.

3. **Total Price Calculation**:
   - Calculate the **total price** of all items before and after discounts.
   - Display the total price, discount applied, and final price after discounts.

4. **Generate and Save Receipt**:
   - Create a **receipt** and Print it in Console :
     - A list of all items with their prices.
     - Total price before and after discount.
     - Discount applied.
     - Final price after discount.

### **2. Python Concepts to Implement**
- **Arrays** (Lists): Store and manage the items in the shopping cart.
- **Control Flow**: Use `if-else` statements to apply discounts based on user input.
- **Functions**: Create functions to handle specific tasks such as calculating the total price, applying discounts, and saving the receipt.

### **3. Git Version Control Tasks**
1. **Initialize Git Repository**:
   - Initialize a Git repository using `git init`.

2. **Commit Changes**:
   - Track your changes using `git add` and commit them using `git commit -m "message"`.

3. **Branching and Merging**:
   - Prepare a Branch and Complete The Code and Raise PR from That Branch
     
4. **Push to Remote Repository** (optional):
   - Create a remote repository (e.g., GitHub) and push your project using:
     ```bash
     git remote add origin <repository-url>
     git push -u origin main
     ```

### **4. Submission Guidelines**
1. Submit the Python file `bill_calculator.py` that implements the shopping bill calculator.
2. Provide the GitHub repository URL or a zip file of the project folder.
3. Ensure that the program works as expected and the receipt is saved correctly in the text file.

### **Evaluation Criteria**
1. **Python Basics**:
   - Correct use of arrays (lists), control flow, and functions.
   - Accurate calculation of discounts and total price.
   - Proper file handling to store the receipt.

2. **Git Basics**:
   - Correct usage of Git commands (`git init`, `git add`, `git commit`, `git merge`, etc.).
   - Proper commit history and branching.
   - Clear project structure and clean commits.

### **Sample Output**

**Welcome to the Shopping Bill Calculator!**

How many items would you like to purchase? **3**

Enter item name: **Shirt**  
Enter price for Shirt: **20**

Enter item name: **Jeans**  
Enter price for Jeans: **40**

Enter item name: **Shoes**  
Enter price for Shoes: **60**

---

## **Shopping Cart:**

- **Shirt**: $20.00  
- **Jeans**: $40.00  
- **Shoes**: $60.00  

---

Do you have a loyalty card? (yes/no): **yes**  
**Loyalty card applied!** 10% discount added.

Is there a seasonal offer? (yes/no): **yes**  
**Seasonal offer applied!** 5% discount added.

---

## **Total Price Before Discount**: **$120.00**  
**Discount Applied**: **15.00%**  
**Final Price After Discount**: **$102.00**

---
