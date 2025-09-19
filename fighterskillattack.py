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
    
    def is_dead(self): #if the health reaches zero the player or the troll wins
        if self.health <= 0:
            return True
        else:
            return False

    def random_attack(self):
        attack_power = random.randint(self.weapon /2, self.weapon * 2)#generate random attacks multiplied by 2 or divided by 2
        print('Attack power:', attack_power)
        return attack_power
    
    def skill_attack(self):
        attack_power = random.randint(self.weapon /2, self.weapon * 2)#generate random attacks multiplied by 2 or divided by 2
        target = random.randint(2,6)
        print('hit enter in exactly' ,target, 'seconds')
        tic = time.time()
        input()
        toc = time.time()
        time_taken = toc - tic
        multiplier = 3
        multiplier = 3 - abs(3 - time_taken)
        if multiplier < 2:
            multiplier = 0

        print('Attack power:', attack_power)
        print('Multiplier', multiplier)
        return attack_power*multiplier
    
    def defend(self,attack_power): #make a shield to lower the amount of damage
        damage = attack_power - self.shield
        if damage > 0:
            self.health -= damage
            print('Damage:', damage)
        else:
            print('no damage')
       

    
#stats for player and troll
you = Fighter('you', 100, 60, 20)
troll = Fighter('troll', 300, 30, 10)

# Display the health at start
you.report()
troll.report()

#player attack troll
while True:

    print('You attack the troll')
    troll.defend(you.skill_attack())  #minus the attack damage
   #show troll health after bieng attacked
    troll.report()
    time.sleep(2)
    print('')
    if troll.is_dead():
        print('you win')
        break
    print('the troll attack you')
    
    #samse way the troll attacks you
    you.defend(troll.random_attack())  
  
    you.report()
    time.sleep(2)
    if you.is_dead():
        print('the troll wins')
        break
    print('')

