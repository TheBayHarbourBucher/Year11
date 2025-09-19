class Pet:
    
    def __init__(self, name, category, breed=None, age=0):
        self._name = name                  # safe
        self.__category = category         # Private
        self.__breed = breed               # Private 
        self.age = age                     # Public 
        self.__ccard = 'unknown'           # Private 
        self.vaccinated = False            # Public 
        self.weight = 0                    # Public 

    #changing the name
    def set_name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print('Use a string as a name')  #error msg

    #method to get the pets name
    def get_name(self):
        return self._name

    #method to get the pets weight
    def get_weight(self):
        return self.weight

    # getting the pets weight(only gtes numbers and positives)
    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print('Enter a proper weight')  #if not positive
        else:
            print('Enter a number')  #if not a number

    # age +1
    def have_birthday(self):
        self.age += 1

    # Method that defines how the object is printed using print()
    def __str__(self):
        payment_status = 'unregistered'
        
        # Check if credit card is registered (simulated by checking string length)
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        #summary
        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status



p1 = Pet(name='Bonnie', category='cat', age=10)

p1.set_name(45632) #testing by typing mumbers
print(p1.get_name())  #name should still be bonny
print(p1)  # print all
