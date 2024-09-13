car_speed=int(input('Please enter speed of the car- '))


if car_speed < 0:
    exit(1)
else: 
    if car_speed< 30:
        print('SLOW')
    else: 
        if car_speed >= 30 and car_speed < 60:
            print('MODERATE')
        else:
            if car_speed >= 60  and car_speed < 120:
                print('FAST')
            else:
                if car_speed>=120:
                    print('VERY FAST')
                else: print('')        
            