costumer_input = input('Please enter your word- ')
count={}
i=0

for i in costumer_input:
    if i in count:
        count[i]+=1
    else:  
        count[i]=1
        
for i, i_count in count.items():
    print(f"{i} - {i_count}")     
    
    