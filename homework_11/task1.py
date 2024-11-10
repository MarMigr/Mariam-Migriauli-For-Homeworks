def farengheit_celsius (gradus_system,gradus):
    if gradus_system in 'C,c':
        return print(f"{gradus} to celsius is -  {(gradus - 32) * 5/9}") 
    elif gradus_system in 'F,f':
        return print(f"{gradus} to farengheit is -  {gradus * 9/5 + 32}")
    
    
def main():
    farengheit_celsius('C',259)
    farengheit_celsius('f',25)
    farengheit_celsius('c',157)
    farengheit_celsius('F',19)

if __name__ == "__main__":
    main()