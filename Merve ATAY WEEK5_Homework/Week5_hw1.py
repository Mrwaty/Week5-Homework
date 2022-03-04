'''
Merve Atay 03.03.2022

Question 1:

Create the class Society with following information:
society_name,house_no_of_mem, flat, income
Methods :
*An __init__ method to assign initial values of society_name,house_no_of_mem, flat, income
*input_data() To read information from members
*allocate_flat() To allocate flat according to income using the below table.
*show_data() to display the details of the entire class.
Income	            Flat
>=25000	            A Type
>=20000 and <25000	B Type
>=15000 and <20000	C Type
<15000	            D Type

'''

class Society():
    
    def __init__(self):
        self.society_name = input("Please write your surname: ")
        self.house_no_of_mem= int(input("Please write the number of family members: "))
        self.income= int(input("Please write your monthly income: "))
     
    def allocate_flat(self):
        income_per_person= ((self.income)*12) / (self.house_no_of_mem)
        if income_per_person >= 25000:
            return "A Type"

        elif 20000 <= income_per_person < 25000:
            return "B Type" 
            
        elif 15000 <= income_per_person <20000:
            return "C Type"
            
        else:
            return "D Type"
            
    def show_data(self):
        print ("Family {} --------> {}"  .format(self.society_name, self.allocate_flat()))
    
user= Society()
Society.show_data(user)