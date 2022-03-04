'''
Merve Atay 03.03.2022

Question 3:
Define a class named Product with the following specifications:
Data members:
*product_id - A string to store product.
*product_name - A string to store the name of the product.
*product_purchase_price - A decimal to store the cost price of the product.
*product_sale_price - A decimal to store Sale Price Margin - A decimal to be calculated as (product_sale_price - product_purchase_price)
*Remarks - To store "Profit" if Margin is positive else "Loss" if Margin is negative.
Methods :
*A constructor to intialize all the data members with valid default values.
*A method set_remarks() that assigns Margin as (product_sale_price - product_purchase_price) and sets Remarks as mentioned below :
Margin	        Remarks
<0 (negative)	Loss
>0 (positive)	Profit
*A method set_details() to accept values for product_id. product_name, product_purchase_price, product_sale_price and invokes SetRemarks() method.
*A method get_details() that displays all the data members.

'''
class Product:
    
    def __init__(self):
        
        self.product_id=input("Enter please Product-ID: ")
        self.product_name=input("Enter please Product-Name: ")
        self.product_purchase_price=int(input("Enter please Product Purchase Price: "))
        self.product_sale_price=int(input("Enter please Product Sale Price: "))

    def set_remarks(self):
        Margin= int(self.product_sale_price) - int(self.product_purchase_price)
        
        if Margin < 0 :
            return "Loss"
        
        else:
            return "Profit"

    def set_details(self):
        
        print("\n Product-ID : {}\n Product_Name : {}\n Purchase-Price: {}\n Sale-Price : ${}\n".format(
        self.product_id,
        self.product_name,
        self.product_purchase_price,
        self.product_sale_price,))

    def get_details(self):
        
        print ("\n The {} Margin from the sale of the product is {}$\n".format(
            self.set_remarks(),
            abs(self.product_sale_price - self.product_purchase_price)
        ))

product=Product()
Product.set_details(product)
Product.get_details(product)