
keyboard = 'qwertyuiopasdfghjklzxcvbnm'
keyboard_asc = {keyboard[i]: keyboard[(i + 1) % len(keyboard)] for i in range(len(keyboard))}
keyboard_desc = {keyboard[i]: keyboard[i - 1] for i in range(len(keyboard))}


while True:
    encode_decode = input("Enter e or d (e for encode / d for decode): ").lower()
    
    if encode_decode not in ('e', 'd'):
        print("Invalid encode_decode. Please enter 'e' to encode or 'd' to decode.")
        continue
    
    text = input("Please Enter text: ").lower() 
    result = ""

    if encode_decode == 'e':  
        for i in text:
            if i in keyboard_asc:
                result += keyboard_asc[i]
            else:
                result += i  

    elif encode_decode == 'd':  
        for i in text:
            if i in keyboard_desc:
                result += keyboard_desc[i]
            else:
                result += i 
    
    print(result)
