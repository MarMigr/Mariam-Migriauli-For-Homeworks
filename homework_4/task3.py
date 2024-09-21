number_to_devide=int(input('Please enter number from 1 to 1000- '))


j=1
for i in range(1,number_to_devide+1):
    j=number_to_devide % i ==0
    if j==True:
        print(i)
        