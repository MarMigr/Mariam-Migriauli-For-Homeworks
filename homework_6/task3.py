n = int(input('Please Enter whole number from 0 to 10000- '))


if n <0 or n >= 10000 :
    print('Wrong Input!')
else: 
      sum = 0
      reverse = 0
      original_num = n
         
while n > 0:
    digit = n % 10  
    reverse = reverse* 10 + digit  
    sum += digit  
    n = n // 10  
    
    
print(f"Reversed number is {reverse}")
print(f"Sum of digits: {sum}")