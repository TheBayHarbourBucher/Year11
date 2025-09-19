class Pet:
    def __init__(self, name, category, breed=None, age=0):
      
        self._name = name#public
        self.__category = category#private
        self.__breed = breed#private
        self.age = age#public
        self.__ccard = 'unknown'#private
        self.vaccinated = False#public

    def have_birthday(self):
        # Increase pet's age by 1
        self.age += 1

    def __str__(self):
        # Check payment status based on the lengh of the card
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        # Build string representation
        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status

      

    def get_category(self):
        # Accessor for the private category
        return self.__category

    def get_breed(self):
        # Accessor for the private breed
        return self.__breed

# Create a pet instance
p1 = Pet(name='Bonnie', category='Cat', age=10)
p1.__category = 'boniefier'
# Print pet details
print(p1)

