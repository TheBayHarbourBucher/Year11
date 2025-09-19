

exec(open("/Users/akain/pyth/god.py").read())
name ='Bonnie'
animal_category = 'Cat'
age = 3
vaccinated = True
credit_card ='3423 2326 7543 1234'
billing_address = '17 Park Drive, The Shire 3695'
owner_name = 'Annie Jenkins'
account_balance = 129.95

def help():
    print ('welcome bla bla bla')
    print('he he he')

def increase_age():
    global age
    age = age + 1

help()
increase_age()
print(age)
