import random

computer_number = random.randrange(0,100)
max_attempts = 10


for attempt in range (1,max_attempts+1) :
    cusromer_number = int(input('Please Enter whole number from 0 to 100- '))


    if cusromer_number == computer_number:
        print("You are winner!")
        break

    elif cusromer_number > computer_number:
        print("High.")
     
    else:
        print("Low.")
    
if attempt == max_attempts:
    print(f"Computer is winner. The number was: {computer_number}")
       