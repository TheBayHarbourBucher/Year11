class Pet:
    def __init__(self, name, category, age = 0): #making the class
        self.name = name
        self.category = category
        self.age = age
        self.ccard = 'unknown'
        self.vaccinated = False
        self.paymentdetails = True
        

    def __str__(self):  
        my_status = 'Name: ' + self.name + '\nCatergory:' + self.category + '\nPayment details:' + self.paymentdetails +'\nage: ' + str(self.age) 
        return my_status
p1 =Pet('Bonnie', 'Cat')

print(p1)