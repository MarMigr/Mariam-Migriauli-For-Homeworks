import random
import math

n = int(input("Enter a natural number greater than 1: "))

if n <= 1:
    print("Please enter a natural number greater than 1.")
else:
    counter = 0
    for _ in range(n):
        num_1 = random.uniform(0, 1)
        num_2 = random.uniform(0, 1)
        if math.sqrt(num_1 ** 2 + num_2 ** 2) <= 1:
            counter += 1
    
    result = 4 * counter / n
    print(f"4 * counter / n for n = {n} is: {result}")

#Output ჰგავს პი რიცხვს, ყოველჯერ როცა n ის მნიშვნელობას ვზრდით, უფრო ვუახლოვდებით პი-ს მნიშვნელობას