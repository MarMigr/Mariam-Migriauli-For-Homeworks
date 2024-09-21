number_to_devide=int(input('Please Enter Number from 1 to 10- '))



if number_to_devide <= 1 or number_to_devide > 10:
    exit(1)
else :    
    if number_to_devide % 2 == 0  and number_to_devide % 3 == 0:
        print('2,3')
    elif number_to_devide % 2 == 0 and number_to_devide % 3 != 0 and number_to_devide % 5 != 0:
        print('2')
    elif number_to_devide % 2 == 0 and number_to_devide % 5 == 0:
        print('2,5')
    elif number_to_devide % 3 == 0 and number_to_devide % 2 != 0:
        print('3')
    elif number_to_devide % 5 == 0 and number_to_devide % 2 != 0:
        print('5')
    else: print('7')     