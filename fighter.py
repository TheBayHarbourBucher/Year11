import random, time  # bring random

class Fighter:
    def __init__(self, name, starting_health, weapon, shield):# give fighter name health and weopne
        self.name = name
        self.health = starting_health
        self.weapon = weapon
        self.shield = shield

    def report(self):
        #Print the fighters name and currenct health
        print(self.name + ': ' + 'Health: ' + str(self.health))

    def random_attack(self):
        attack_power = random.randint(self.weapon /2, self.weapon * 2)#generate random attacks multiplied by 2 or divided by 2
        print('Attack power:', attack_power)
        return attack_power
    
    def defend(self,attack_power):
        damage = attack_power - self.shield
        if damage > 0:
            self.health -= damage
            print('Damage:', damage)
        else:
            print('no damage')
       

    
#stats for player and troll
you = Fighter('you', 100, 60, 20)
troll = Fighter('troll', 200, 30, 10)

# Display the health at start
you.report()
troll.report()

#player attack troll
while True:

    print('You attack the troll')
    troll.defend(you.random_attack())  #minus the attack damage
   #show troll health after bieng attacked
    troll.report()
    time.sleep(5)
    print('')
    if troll.health <= 0:
        print('you win')
        break
    print('the troll attack you')
    

    you.defend(troll.random_attack())  
  
    you.report()
    time.sleep(5)
    if troll.health <= 0:
        print('the troll wins')
        break
    print('')

