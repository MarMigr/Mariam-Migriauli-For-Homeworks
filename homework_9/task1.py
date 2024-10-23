n = int(input("Enter a whole number more than 1: "))

if n <= 1:
    print("Please enter a whole number more than 1.")
else:
    x = 0
    y = 1
    for i in range(1, 2 * n, 2):
        x += y * (1 / i)
        y *= -1
    x *= 4
    print(f"x for n = {n} is: {x}")


#Output ჰგავს პი რიცხვს, ყოველჯერ როცა n ის მნიშვნელობას ვზრდით, უფრო ვუახლოვდებით პი-ს მნიშვნელობას