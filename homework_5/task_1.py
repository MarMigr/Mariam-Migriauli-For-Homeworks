n = int(input("Please Enter  number between 1 and 49: "))

if n <= 0 or n >= 50:
    print("Please enter a number between 1 and 49: ")
else:
    for i in range(1, n + 1):
        print(f"{i} – ", end="")
        count = 0  
        divisor = 1
        while divisor <= i and count < 3:  
            if i % divisor == 0: 
                print(divisor, end=" ")
                count += 1
            divisor += 1
        print()  
