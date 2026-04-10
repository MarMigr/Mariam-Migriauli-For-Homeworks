small = []
high = []

with open("data.txt","r") as file:
    for line in file:
        data = line.strip().split(',')
        if len(data) == 4:
                amount = int(data[2])
                price = float(data[3])
                total_price = amount * price
                if total_price < 10:
                    small.append(line.strip())
                else:
                    high.append(line.strip())

with open("small.txt", "w") as small_file:
    for line in small:
        small_file.write(line + "\n") 
        
with open("high.txt", "w") as high_file:
    for line in high:
        high_file.write(line + "\n")        
    
    