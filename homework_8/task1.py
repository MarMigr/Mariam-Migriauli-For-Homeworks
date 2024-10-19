input = input("Enter a your text: ").split()


cleaned_text = ""


for i in input:
    
    if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
        cleaned_text += i.lower()  



if cleaned_text == cleaned_text[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")


