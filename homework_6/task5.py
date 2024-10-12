# Accept an integer n
n = int(input("Enter a number from 0 to 10: "))


if n <= 0 or n >= 10:
    print("Please enter a valid number in the range 0 to 10")
else:

    i = 0
    while i <= n:
        print(" " * (n - i), end="")


        j = i
        while j > 0:
            print(j, end=" ")
            j -= 1


        j = 0
        while j <= i:
            print(j, end=" ")
            j += 1

        print()

        i += 1
