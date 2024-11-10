n = int(input('Please enter whole number from 1 to 1000- '))

if n > 0 and n < 1000:
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else : n = n *3 + 1    
    
        print ("->", n , end =' ')
else: print('Please Enter Valid Number')     