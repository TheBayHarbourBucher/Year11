class pet:
    def __init__(self, name ,category, age):
        self.name = name
        self.category = category
        self.age = age
        self.ccard = "unknown"
        self.vaccinated = "False"
                 
             
        self.billing_address = 'unknown'  
        self.owner_name = 'unknown'      
        self.account_balance = 0       


       

p1 = pet('Bonnie','cat', 3)
p2 = pet('Foxy','frog', 4)

bonnie = input(f"is{p1.name, p1.category, p1.age} is vaccinated? ")
if bonnie == 'Yes':
    print(f"is{p1.name, p1.category, p1.age} is vaccinated ")
if bonnie == 'No':
    print(f"is{p1.name, p1.category, p1.age} is not vaccinated ")

Frog = input(f"is{p1.name, p1.category, p1.age} is vaccinated? ")
if bonnie == 'Yes':
    print(f"is{p1.name, p1.category, p1.age} is vaccinated ")
if bonnie == 'No':
    print(f"is{p1.name, p1.category, p1.age} is not vaccinated ")




