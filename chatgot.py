class Pet:
    def __init__(self, name, category, breed=None, age=0):
        self._name = name
        self.__category = category
        self.__breed = breed
        self.age = age
        self.__ccard = 'unknown'
        self.vaccinated = False
        self.weight = 0

    def set_name(self, new_name):
        if type(new_name) == str:
            self._name = new_name
        else:
            print('Use a string as a name')

    def get_name(self):
        return self._name

    def get_weight(self):
        return self.weight

    def set_weight(self, new_weight):
        if type(new_weight) == int or type(new_weight) == float:
            if new_weight > 0:
                self.weight = new_weight
            else:
                print('Enter a proper weight')
        else:
            print('Enter a number')

    def have_birthday(self):
        self.age += 1

    def __str__(self):
        payment_status = 'unregistered'
        if len(self.__ccard) == 19:
            payment_status = 'registered'

        my_status = 'Name: ' + self._name +'\nCategory: ' + self.__category + '\nAge: ' + str(self.age) +'\nPayment status: ' + payment_status + '\nVaccinated: '+ str(self.vaccinated)
        return my_status
 


# Testing
p1 = Pet(name='Bonnie', category='cat', age=10)
p1.set_name(45632)  # Wrong type
print(p1.get_name())  # Should still print 'Bonnie'
print(p1)  # Will now show nicely formatted info