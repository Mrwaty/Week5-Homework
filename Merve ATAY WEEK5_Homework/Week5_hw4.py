'''
Merve Atay 03.03.2022

Write a Customer class and Items class. Let user enter customer information and add stuff to his/her shopping card.
Class Items : Method : __init__(), __str__(), calculate_discount(), shopping_cart(), get_total_amount()
calculate_discount():
*total_price = price * qty
*discount —> 25% if total_price >= 4000
*discount —> 15% if total_price >= 2000
*discount —> 10% if total_price < 2000
*price_tobe_paid = total_price - discount
*shopping_cart():

Let user add items in the shopping basket. Be creative with the items, set their prices as well.
__str__():
*Print items added and total price nicely. Class Customer : Methods: __init__()``, get_cust_info()this is optional,str()`
*Optionally create a get_cust_info() or similar to allow customer to enter his/her information or just define them in 
__init__() and pass customer information as arguments while creating a customer object.
*Print customer information and price nicely. Find a way to link two classes. 
For example, instances of both classes may have a customer number. 
With a get method, get the customer number and pass it to the item object as an argument to set customer number attribute. 
So Customer class instance holds the customer info, Items class holds the shopped item’s info for the same customer ID number 
such as price, quantity or so.
*In the end, print both info (customer info and shopped items info) using their respective __str__ format in a nice way.
*Simple example:
Customer1 = [name : Jack, last_name : Russel, customer_id : 123]
shopping_cart1 = [customer_id : 123, items : [necklace, ring, ear ring], total_price : 2000, discount : 300, price_tobe_paid : 1700]
Crate a few customers and print their information (Personal and shopping info).

'''

class Customer():
    def __init__(self):
        self.name= input("Enter please your name: ")
        self.surname= input("Enter please your surname: ")
        self.id= input("enter please your ID: ")
    
    def customer_info(self):
        print ("\nName :{}, Last Name :{}, Customer-ID :{}\n".format(self.name, self.surname, self.id))

class Items(Customer):
    def __init__(self):
        super().__init__()
        pass
        
    def shopping_card(self):
        self.add_basket=[]
        self.add_prices=[]
        
        while True:
            
            self.item_name= input("\nWrite please the name of the product you want to buy: ")
            self.add_basket.append(self.item_name)
            
            self.quantity= int(input("Write please how many of this product you want to buy: "))
            self.price=int(input("Write please the unit price of the product: "))
            self.total= self.quantity * self.price
            self.add_prices.append(self.total)
            
            self.quit= input("\nPress 'q' to exit or press any key to continue shopping:  ")
            if self.quit=='q':
                break
            else:
                continue
    def calculate_discount(self):
        self.total_price=0
        for i in self.add_prices:
            self.total_price+=i
        
            
        if self.total_price >= 4000 :
            self.discount= 0.25
        elif 4000 < self.total_price <= 2000:
            self.discount= 0.15
        else:
            self.discount= 0.10
            
        self.total_discount= self.total_price * self.discount
        self.price_to_be_paid= self.total_price - self.total_discount

    def items_info(self):
        
        print("Items: {}, Total Price: {}, Total Discount: {}, Price to be paid: {} ".format(
            self.add_basket,
            self.total_price,
            self.total_discount,
            self.price_to_be_paid
        ))

customer1=Customer()
Items.shopping_card(customer1)
Items.calculate_discount(customer1)
Items.customer_info(customer1)
Items.items_info(customer1)