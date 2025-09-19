class Pet:
    def __init__(self, name, category, age):
        # Attributes passed during creation
        self.name = name
        self.category = category
        self.age = age

        # Default attributes for all pets
        self.vaccinated = False           # Vaccination status, default is False
        self.ccard = 'unknown'            # Credit card, default is 'unknown'
        self.billing_address = 'unknown'  # Billing address, default is 'unknown'
        self.owner_name = 'unknown'       # Owner name, default is 'unknown'
        self.account_balance = 0          # Account balance, default is 0

    # Method to return vaccination status
    def vaccination_status(self):
        return f"{self.name} vaccinated: {self.vaccinated}"


# --- Activities ---

# Create a Pet object called Bonnie
bonnie = Pet('Bonnie', 'cat', 3)

# Print Bonnie's vaccination status
print(bonnie.vaccination_status())  # Expected: Bonnie vaccinated: False