from datetime import datetime


customer_year = int(input('Please enter year you where born: '))
customer_month = int(input('Please enter month you where born from 1 to 12: '))
customer_day = int(input('Please enter day you where born from 1 to 31: '))


customer_date_of_birth = datetime(customer_year,customer_month, customer_day)


print('You were born on :',customer_date_of_birth) #.strftime('%A'))

