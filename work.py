class pet:
    def __init__(self, name ,category, age):#creating a class 
        self.name = name
        self.category = category
        self.age = age
        self.ccard = "unknown"
        self.vaccinated = False
                 
             
        self.billing_address = 'unknown'  
        self.owner_name = 'unknown'      
        self.account_balance = 0       
    
    def __str__(self):#if the card has 19 digits it will be registered and if not it will be unregistered
        payment_status = 'unregistered'
        if len(self.ccard) == 19:
            payment_status = 'registered'

# class
        my_status = 'Name: ' + self.name + '\nCategory: ' + self.category + '\nAge: '+ str(self.age) + '\nPaymentstatus: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status



       
#inserting the variables and values for the class
p1 = pet('Bonnie','cat', 3)
p2 = pet('Foxy','frog', 4)
p3 = pet('lobo','dinosour',74)



pets1 = [p1, p2, p3 ] #lists



print("Vaccinating each pet:")
for pet in pets1:
    pet.vaccinated = True
    print(pet) # Print new version
    print('')
