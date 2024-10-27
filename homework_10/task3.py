def factorial_of_number(num):
    result = 1
    while num > 1 :
        result *= num
        num -= 1
    return result
    
print(factorial_of_number(3))    
print(factorial_of_number(5))    
print(factorial_of_number(2))  
print(factorial_of_number(7))      