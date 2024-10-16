input_from_customer=input('Please Enter your word- ').strip()

for i in range(0,len(input_from_customer)) :
   if input_from_customer[i] not in 'aeoiuy':
        print(input_from_customer[i])