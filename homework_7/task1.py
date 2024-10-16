input_string=input('Please Enter Your word- ').strip()


for i in range(0,len(input_string)) :
    if i % 2 and input_string[i] != 'e':
        print(input_string[i])