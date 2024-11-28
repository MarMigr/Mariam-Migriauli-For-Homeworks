n = int(input('Please enter number between 10 and 5432- '))
counter = 0

if n < 10 or n > 5432:
    print('Invalid input')
else:   
    for i in range(1,n+1):
        if i % 13 ==0:
            counter+=1    
print(i, "number of devisors- ",counter)    