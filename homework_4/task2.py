from random import randint

number=int(input('Please enter your positive number(from 1 to 30)- '))
b = [randint(0, 1000) for i in range(number)]

maximum_number=max(randint(0, 1000) for i in range(number))

print('The maximum is -',maximum_number,b)
