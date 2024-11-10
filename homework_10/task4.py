def simple_num(num):
    result = 0
    for i in range(2,num):
        if num % i ==0:
            return False
        return True

print(simple_num(5))        
print(simple_num(6))    
print(simple_num(10))  
print(simple_num(13))   
print(simple_num(3))        