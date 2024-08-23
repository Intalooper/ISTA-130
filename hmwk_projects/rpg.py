'''
John Diaz-Leal 
Start date: August 18th 
Finish date: August 22nd
Time spent on project: roughly 7 hours 

Purpose: Exploring classes
'''

import random 

class Fighter: 
    '''
    Purpose: Class Fighter creats an instance of a Fighter with several different methods and unique data
    '''
    def __init__(self, name):
        '''
        Purpose: Initializes each new instance with a name and establishes health/hit points
        Parameters:
            name (type: string): String for the name of the instance 
        '''
        self.name = name 
        #life points for each of the instances
        self.hit_points = 10
    def __repr__(self):
        '''
        Purpose: String representation of each instance/object of the class
        '''
        fighter_data = f'{self.name} (HP: {self.hit_points})'
        return fighter_data
    def take_damage(self, damage_amount):
        '''
        Purpose: Keeps track of the damage taken for each Fighter and indicates when a Fighter has died
        Paramaeter:
            damage_amount (Type: int): Represents the number of hit points of damage that have been inflicted on this Fighter
        '''
        #damage is calculated in the attack method and is stored in the damage_inflicted variable 
        self.damage_amount = damage_amount
        self.hit_points -= self.damage_amount
        if self.hit_points <= 0:
            print(f'\tAlas, {self.name} has fallen!') 
        else: 
            print(f'\t{self.name} has {self.hit_points} hit points remaining.')
    def attack(self, other):
        '''
        Purpose: Indicates to user that there is an attack and the damage of the attack inflicted
        Parameter: 
            other (Type: instance):
        '''
        
        print(f'{self.name} attacks {other.name}!')
        #generates a number to check if there is a hit inside of the game
        hit_check = random.randrange(1, 21)
        #if there is a hit the conditional below will determine the damage done and detract it from its total health
        if hit_check >= 12:
            damage_inflicted = random.randrange(1, 7)
            print(f'\tHits for {damage_inflicted} hit points!')
            other.take_damage(damage_inflicted)
        else:
            print('\tMisses!')

        return None

    def is_alive(self):
        '''
        Purpose: Returns boolean value depending on whether the fighter is alive or not 
        '''
        if self.hit_points > 0:
            return True 
        else:
            return False


def combat_round(fighter_one, fighter_two):
        '''
        Purpose: Determines which of the two fighters attacks first and also has the either both or one of the fighters attack
        Parameter:
            fighter_one (Type: Instance): Fighter Instance
            fighter_two (Type: Instance): Fighter Instance
        '''
        #roll where the higher number determines which fighter attacks first. The same number means both attack each other
        fighter_one_roll = random.randrange(1, 7)
        fighter_two_roll = random.randrange(1, 7)
        #conditional to check whether both fighters attack each other at the same time
        if fighter_one_roll == fighter_two_roll:
            print('Simultaneous!')
            fighter_one.attack(fighter_two)
            fighter_two.attack(fighter_one)
        #if fighter one has a higher roll then he attacks first then if fighter two is still alive he attacks 
        elif fighter_one_roll > fighter_two_roll: 
            fighter_one.attack(fighter_two)
            if fighter_two.is_alive() == True:
                fighter_two.attack(fighter_one)
        #the reverse is true here
        elif fighter_two_roll > fighter_one_roll:
            fighter_two.attack(fighter_one)
            if fighter_one.is_alive() == True:
                fighter_one.attack(fighter_two)
        
   
def main():
    print('')
    fighter_mac = Fighter('Death_Mongrel')
    fighter_pc = Fighter('Hurt_then_Pain')

    
    round = 1
    while fighter_mac.is_alive() == True and fighter_pc.is_alive(): 
        round_line = '\n' + '=' * 19 + ' ' + f'ROUND {round}' + ' ' + '=' * 19
        print(round_line)
        print(fighter_mac.__repr__())
        print(fighter_pc.__repr__())
        input('Enter to Fight!')
        combat_round(fighter_mac, fighter_pc)
        round += 1
    else: 
        print('\nThe battle is over!')
        print(fighter_mac.__repr__())
        print(fighter_pc.__repr__())


if __name__ == '__main__':
    main()




