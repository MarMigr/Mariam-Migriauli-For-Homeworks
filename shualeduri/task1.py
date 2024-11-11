#Დაწერეთ პროგრამა რომელიც მომხმარებელს მოსთხოვს შეიყვანოს შემდეგი მონაცემები: 
# სახელი, გვარი, ასაკი და ქალაქი. 
# Ეს ინფორმაცია Პროგრამამ ეკრენზე უნდა დაბეჭდოს შემდეგ ფორმატში: 
# Hello სახელი გვარი. Age: ასაკი. City: ქალაქი.


def customer_input():
    name=input('Please enter your name- ')
    surname=input('Please enter your surname- ')
    age=input('Please enter your age- ')
    city=input('Please enter your city- ')
    print("Hello",name,' ',surname,' ',age,' ',city)
    
if __name__ == '__main__':
    customer_input()    