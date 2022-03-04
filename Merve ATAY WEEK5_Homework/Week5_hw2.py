'''
Merve Atay 03.03.2022

Question 2:
Define a class named ``ItemInfo` with the following description:
item_code(Item Code), item(item name), price(Price of each item), qty(quantity in stock), discount(Discount percentage on the item), net_price(Price after discount)
Methods :
*A member method calculate_discount() to calculate discount as per the following rules:
*If qty <= 10                —> discount is 0
*If qty (11 to 20 inclusive) —> discount is 15
*If qty >= 20                —> discount is 20
*A constructor init method to assign the initial values for item_code to 0 and price, qty, net_price and discount to null
*A function called buy() to allow user to enter values for item_code, item, price, qty. Then call function calculate_discount() to calculate the discount and net_price(price * qty - discount).
*A function show_all() or similar name to allow user to view the content of all the data members.

'''

class ItemInfo:
    def __init__(self):
        self.item_code=input("Please write your Item Code: ")
        self.item=input("Please write your Item Name: ")
        self.price=int(input("Please write the price of Item: "))
        self.qty=int(input("Please enter quantity in stock: "))

    def calculate_discount(self):
        if self.qty <= 10:
            discount = 0
        elif 11 <= self.qty <= 20:
            discount = 15/100
        else:
            discount = 20/100
        total_price = self.price * self.qty
        net_price= total_price - discount*total_price
        return net_price
    
    def buy(self):
        self.calculate_discount()

    def show_all(self):
        print("\n\nYour Item Code: {}\nYour Item Name: {}\nThe total amount of the products is {}\nDiscounted Amount is {}".format(
            self.item_code,
            self.item,
            self.price * self.qty,
            self.calculate_discount()
            ))

user=ItemInfo()
ItemInfo.show_all(user)