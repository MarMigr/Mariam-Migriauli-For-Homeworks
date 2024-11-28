from random import randint

r_p_s=randint(1,3)

if r_p_s == 1:
    rock_paper_scisors='R'
elif r_p_s == 2:
    rock_paper_scisors='P'    
elif r_p_s == 3:
    rock_paper_scisors='S'    
    
def customer_input():
    return  
customers_r_p_s=input('Please enter R OR P OR S- ')    



def winner(r_p_s,customer_input):
    count=0
    result=''
    if r_p_s==customers_r_p_s and count<1:
            customer_input()
            count+=1
    elif r_p_s == 1 and  customer_input == 'S':
        result='Computer is winner'     
    elif r_p_s == 2 and  customer_input == 'P':
        result='Computer is winner'         
    elif r_p_s == 3 and  customer_input == 'R':
        result='Computer is winner'  
    else:   
        result='You Win!' 
    return result

