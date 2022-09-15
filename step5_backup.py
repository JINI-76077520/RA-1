import pandas as pd
import numpy as np

pokemon = pd.read_csv ('C:/Users/Brian Kim/Desktop/Programming project/Pokemon.csv');

pokemon_simple = pokemon[['Name', 'Type 1', 'HP', 'Attack', 'Defense', 'Legendary']]

global k
k = 0

global HP_save
HP_save = []

global x
x = 0

global y
y = 0

global potent1
potent1 = 3

global potent2
potent2 = 3

global Types
Types = []
            
class pokemon:
    
    def __init__(self, Name):
        self.Name = Name
        global pokemon_select
        pokemon_select = pokemon_simple[pokemon_simple['Name'] == self.Name]
        global Type
        Type = pokemon_select.iat[0,1]
        global max_HP
        max_HP = pokemon_select.iat[0,2]
        global HP
        HP = max_HP
        global Legendary
        Legendary = pokemon_select.iat[0,5]
        
    def info(self):
        if Legendary == False:
            print ('The ', self.Name, 'has a type', Type, 'and its HP is', max_HP, '.')
        else:
            print ('Congratulations! You have the legendary pokemon!\n',
                   'The', self.Name, 'has a type', Type, 'and its HP is', max_HP, '.')
        return 0

    def health(self):
        global HP
        print ('The ', self.Name, 'has a type', Type, 'and its HP is', HP, '.')
        return HP

    def lose_health(self, value):
        global HP
        HP = HP - value
        if HP <= 0:
            print ('The', self.Name, 'has lost health of value', value, 
                   'and has now health of 0.\n')
            HP = 0
            pokemon.knocked_out(self)
        else:
            print ('The', self.Name, 'has lost health of value', value, 
                   'and has now health of', HP, '.\n')
        return HP
        
    def gain_health(self, value):
        global HP
        global max_HP
        HP = HP + value
        if HP > max_HP:
            max_heal = value - (HP - max_HP)
            print ('Cannot add more than', max_heal, '. It is already at Its maximum value of', max_HP, '.')
            HP = max_HP
            pokemon.health(self)
        else:    
            print ('The', self.Name, 'has gain health of value', value, 
                   'and has now health of', HP, '.')
        return 0

    def knocked_out(self):
        print ('The pokemon', self.Name, 'is knocked out.\n')
        return 0
        
    def revive(self):
        global HP
        global max_HP
        if HP == 0:
            print ('The pokemon', self.Name, 'is revived.')
            HP = max_HP
            pokemon.health(self)
        else:
            print ('The pokemon is alive!, Cannot be revived.')
        return 0   

class trainer(pokemon):
    
    def __init__(self, Name, Name1, Name2, Name3, Name4):
        super().__init__(Name1)
        self.Name = Name
        self.Name1 = Name1
        self.Name2 = Name2
        self.Name3 = Name3
        self.Name4 = Name4
        self.potent = 3
    
    def info(self):
        print('The Trainer', self.Name, 'has pokemons\n', 
              self.Name1, '\n',
              self.Name2, '\n',
              self.Name3, '\n',
              self.Name4, '\n',
              'and the current pokemon is', self.Name1)
        
    def current_pokemon(self):
        global pokemon_select
        pokemon_select = pokemon_simple[pokemon_simple['Name'] == self.Name1]
        global Type
        Type = pokemon_select.iat[0,1]
        Types.append(Type)
        global max_HP
        max_HP = pokemon_select.iat[0,2]
        global Attack 
        Attack = pokemon_select.iat[0,3]
        global Defense 
        Defense = pokemon_select.iat[0,4]
        
        print ('          ', self.Name1, '\n',
               '          Type :', Type, '\n',
               '          HP :', max_HP, '\n',
               '          Attack :', Attack, '\n',
               '          Defense :', Defense, '\n')
        Attack = 0
        Defense = 0
    
        return 0
    
    def current_pokemon_Name(self):
        global pokemon_select
        pokemon_select = pokemon_simple[pokemon_simple['Name'] == self.Name1]
        return self.Name1

    def current_pokemon_ATK(self):
        global Attack
        pokemon_select = pokemon_simple[pokemon_simple['Name'] == self.Name1]
        Attack = pokemon_select.iat[0,3]
        return Attack
    
    def current_pokemon_DEF(self):
        global Defense
        pokemon_select = pokemon_simple[pokemon_simple['Name'] == self.Name1]
        Defense = pokemon_select.iat[0,4]
        return Defense    
    
    def attack_pokemon(self, enemy):
        global HP
        global HP_save
        global x
        global y
        A = trainer.current_pokemon_ATK(self)
        B = enemy.current_pokemon_DEF()
        C = enemy.current_pokemon_Name()
        Pokemon = pokemon(C)
        if x == 0:
            pass
        else:
            HP = HP_save[x-1]
        damage =  abs(A - B)
        print ("!!!", self.Name1, 'is attacking ', C, '!!!\n')
        HP = Pokemon.lose_health(damage)
        HP_save.append(HP)
        y = y + 1
        if y <= 1:
            pass
        else:
            x = x + 1
        if HP == 0:
            print(self.Name, 'won!\n')
            global k
            k = 1
    
    def use_potent(self):
        if HP_save[x] <= 10 and self.potent !=0:
            pokemon.gain_health(self, 100)
            self.potent = self.potent - 1
        return 0

trainer_1 = trainer("대웅", 'Combusken', 'BlazikenMega Blaziken', 'Carracosta', 'Mudkip')
trainer_1.info()
trainer_1.current_pokemon()

trainer_2 = trainer("희루", 'Infernape', 'Numel', 'Suicune', 'Gorebyss')
trainer_2.info()
trainer_2.current_pokemon()

print ("Pokemon Battle Start!\n")

while (k == 0):
    trainer_1.attack_pokemon(trainer_2)
    if k == 1:
        break
    trainer_2.use_potent()
    if k == 1:
        break
    trainer_2.attack_pokemon(trainer_1)
    if k == 1:
        break
    trainer_1.use_potent()
    if k == 1:
        break

print ("Pokemon Battle End!")
    