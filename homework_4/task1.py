from random import randint


number_of_players = int(input('Please enter number of players: '))


for i in range(0,number_of_players):
   dice_num=randint(1,6)
   print('Player Numer-',i+1,'Dice Number is-',dice_num) 
      
 
