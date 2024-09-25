
n = int(input('Please enter number from 1 to 20- '))

if 0 <= n < 20:

    n1 = 0 
    n2 = 1


    for i in range(2, n + 1):
        n1, n2 = n2, n1 + n2

    if n == 0:
        fibbonacci_num = n1
    else:
        fibbonacci_num = n2
        
        print('Fibbonacci number is- ',fibbonacci_num)   
         
else : print('Enter number from 1 to 20-')

            