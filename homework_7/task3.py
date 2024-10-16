input_from_customer=input('Please Enter your Word- ').strip()

i=0
middle=(len(input_from_customer))//2


while i<5: 
    if len(input_from_customer) % 2 == 0:
        print(f"middle symbols are: {input_from_customer[middle-1]} and {input_from_customer[middle]}") 
    else:
        print(f"The last Symbol is- {input_from_customer[-1]} the first symbol is- {input_from_customer[0]}, the middle symbol is-{input_from_customer[middle]}")
    i+=1
    
    
