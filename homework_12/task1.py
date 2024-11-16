temperatures=[22, 25, 19, 23, 25, 26, 23]

def average_temperature(temperatures):
    avg_temp = sum(temperatures)/len(temperatures)
    return print(avg_temp)    
       
def main():
    average_temperature(temperatures)

if __name__=="__main__":
    main()