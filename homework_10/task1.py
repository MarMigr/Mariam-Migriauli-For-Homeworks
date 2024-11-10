vowels = "aeiouAEIOU" 

def vowel_count(text):  
    count=0    
    for i in text: 
        if i in vowels:
            count+=1
    return count
    
print(vowel_count("Mariam Migriauli'"))
print(vowel_count("Python programming"))
print(vowel_count("this is my homework"))  
