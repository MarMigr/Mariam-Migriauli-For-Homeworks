def gcd_iterative(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def gcd_recursive(a, b):
    if b == 0:
        return a
    return gcd_recursive(b, a % b)

if __name__ == "__main__":
    a = int(input("Enter a number between 1 and 9999: "))
    b = int(input("Enter b number between 1 and 9999: "))


    if 0 < a < 10000 and 0 < b < 10000:
        print(f"GCD of {a} and {b} is {gcd_iterative(a, b)} (Iterative method)")
        print(f"GCD of {a} and {b} is {gcd_recursive(a, b)} (Recursive method)")
    else:
        print("Please enter numbers between 1 and 9999.")

