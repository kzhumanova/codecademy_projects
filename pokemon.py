class Pokemon:
    
    def __init__(self, name, level, type, health, max_health, is_knocked_out):
        self.name = name
        self.level = level
        self.type = type
        self.health = health
        if self.health > 0:
            self.is_knocked_out = False
        if self.health == 0:
            self.is_knocked_out = True
        self.max_health = max_health
        
      
    def lose_health(self, damage):
        self.health = self.health - damage
        print('{name} is injured! Health is now {health}.'.format(name = self.name, health = self.health))

    def regain_health(self, gain):
        self.health = self.health + gain
        print('{name} regained health! Health is now {health}.'.format(name = self.name, health = self.health))

    def knocked_out(self):
        if self.health == 0:
            self.is_knocked_out = True
            print('{name} is knocked out!'.format(name = self.name))
        else:
            print('{name} is still alive!'.format(name = self.name))

    def attack(self, opponent):
        if self.is_knocked_out:
            print('Pokemon is knocked out and cannot attack!')
        else:
            if self.type == 'Fire' and (opponent.type == 'Water' or opponent.type == 'Grass'):
                damage = self.level * 2
            if self.type == 'Water' and opponent.type == 'Fire':
                damage = self.level / 2
            if self.type == 'Water' and opponent.type == 'Grass':
                damage = self.level * 2
            if self.type == 'Grass' and (opponent.type == 'Fire' or opponent.type == 'Water'):
                damage = self.level / 2
            print('{name} attacked {oname}! Damage is {damage}.'.format(name = self.name, oname = opponent.name, damage = damage))
            return damage

class Trainer:
    
    def __init__(self, pokemons, name, potions, current_pokemon):
        self.pokemons = pokemons
        self.name = name
        self.potions = potions
        self.current_pokemon = current_pokemon
    
    def use_potion(self):
        if self.potions > 0 and self.pokemons[self.current_pokemon].health < self.pokemons[self.current_pokemon].max_health:
            gain = self.pokemons[self.current_pokemon].max_health - self.pokemons[self.current_pokemon].health
            self.pokemons[self.current_pokemon].regain_health(gain)
            self.potions = self.potions - 1
            print('{name} used potion for {pokemon}. Potions left: {potions}.'.format(name = self.name, pokemon = self.pokemons[self.current_pokemon].name, potions = self.potions))
        elif self.pokemons[self.current_pokemon].health == self.pokemons[self.current_pokemon].max_health:
            print('No potions needed!')
        else:
            print('No potions!')
    
    def attack_trainer(self, other_trainer):
        if self.pokemons[self.current_pokemon].is_knocked_out:
            print('Pokemon is knocked out and cannot attack!')
        else:
            print('{name} attacked {other}!'.format(name = self.name, other = other_trainer.name))
            self.pokemons[self.current_pokemon].attack(other_trainer.pokemons[other_trainer.current_pokemon])

    def switch_pokemon(self):
        number_of_pokemons = len(self.pokemons)
        if self.current_pokemon == (number_of_pokemons - 1) and self.pokemons[self.current_pokemon - 1].is_knocked_out == False:
            self.current_pokemon = self.current_pokemon - 1
            print('Pokemon is switched from {old} to {new}.'.format(old = self.pokemons[self.current_pokemon + 1].name, new = self.pokemons[self.current_pokemon].name))
        if self.current_pokemon < (number_of_pokemons - 1) and self.pokemons[self.current_pokemon + 1].is_knocked_out == False:
            self.current_pokemon = self.current_pokemon + 1
            print('Pokemon is switched from {old} to {new}.'.format(old = self.pokemons[self.current_pokemon - 1].name, new = self.pokemons[self.current_pokemon].name))
        else:
            print('No available Pokemon to switch!')



pikachu = Pokemon('Pikachu', 20, 'Fire', 60, 100, None)
#pikachu.lose_health(100)
#pikachu.regain_health(10)
#pikachu.knocked_out()

bulba = Pokemon('Bulbasaur', 30, 'Grass', 70, 100, None)
squirtle = Pokemon('Squirtle', 10, 'Water', 80, 100, None)

#damage = pikachu.attack(bulba)
#bulba.attack(pikachu)
#squirtle.attack(pikachu)
#pikachu.attack(squirtle)

#bulba.lose_health(damage)

ash_pok = [pikachu, bulba]
ash = Trainer(ash_pok, 'Ash', 5, 0)
#print(ash.current_pokemon.name)
#ash.use_potion()

bobby_pok = [squirtle]
bobby = Trainer(bobby_pok, 'Bobby', 3, 0)

#sh.attack_trainer(bobby)

print(ash.current_pokemon)
ash.switch_pokemon()
print(ash.current_pokemon)
