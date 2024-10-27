def num_factorial(num):
    result = 1
    while num > 1:
        result *= num
        num -= 1
    return result    
  

print(num_factorial(3))
print(num_factorial(7))
print(num_factorial(5))