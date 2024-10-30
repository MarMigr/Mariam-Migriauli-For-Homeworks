from task2 import gcd_iterative

a = int(input("Enter a: "))
b = int(input("Enter b: "))

def lcm(a, b):
    return (a * b) // gcd_iterative(a, b)


if 0 < a < 10000 and 0 < b < 10000:
    print(f"LCM of {a} and {b} is {lcm(a, b)}")
else:
    print("Please enter numbers between 1 and 9999.")
