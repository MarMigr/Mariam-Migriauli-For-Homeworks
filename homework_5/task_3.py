n=int(input('Please enter number from 0 to 20- '))


if n < 0 or n >= 20:
    print("Please enter a number between 0 and 19")
else:

    a = 0 
    b = 1  
    count = 0  
    
    while count <= n:
        print(a, end=" ")
        next_num = a + b
        a = b
        b = next_num
        count += 1



