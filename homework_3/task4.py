import random


random_num_for_suits = random.randint(0, 3)
random_num_for_ranks = random.randint(0, 12)



if random_num_for_suits == 0:
    suit = '♣'
elif random_num_for_suits == 1:
    suit = '♦'
elif random_num_for_suits == 2:
    suit = '♥'
else:
    suit = '♠'    

    
print(random_num_for_suits,suit)



if random_num_for_ranks == 0:
    rank = 'A'
elif random_num_for_ranks == 1:
    rank = 'K'
elif random_num_for_ranks == 2:
    rank = 'Q'
elif random_num_for_ranks == 3:
    rank = 'J'   
elif random_num_for_ranks == 4:
    rank= '10'    
elif random_num_for_ranks == 5:
    rank= '9'
elif random_num_for_ranks == 6:
    rank= '8'           
elif random_num_for_ranks == 7:
    rank= '7'         
elif random_num_for_ranks == 8:
    rank= '6'   
elif random_num_for_ranks == 9:
    rank= '5'      
elif random_num_for_ranks == 10:
    rank= '4'        
elif random_num_for_ranks == 11:
    rank= '3'    
else: rank= '2'             

  
print(random_num_for_ranks,rank)

print("The randomly selected card is: ",suit,rank)