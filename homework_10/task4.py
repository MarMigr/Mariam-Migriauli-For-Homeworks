def simple_num(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


print(simple_num(200))    
print(simple_num(11))   
print(simple_num(17))  
print(simple_num(25))  

