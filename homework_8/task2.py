str1 = input("Enter the first string: ").replace(" ", "").lower()
str2 = input("Enter the second string: ").replace(" ", "").lower()

alphabet = "abcdefghijklmnopqrstuvwxyz"


char_count = [0] * 26


for i in str1:
    index = alphabet.index(i)  
    char_count[index] += 1


possible = True
for i in str2:
    index = alphabet.index(i)  
    if char_count[index] == 0:  
        possible = False
        break
    else:
        char_count[index] -= 1

if possible:
    print("YES")
else:
    print("NO")

