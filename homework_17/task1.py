def generate_seq_n(n):
    sequence = []    
    while n != 1:
        sequence.append(n)    
        if n % 2 == 0:
            n //= 2
        else: 
            n=n*3+1
    sequence.append(1)    
    return sequence           

seq_cache={}
def generate_seq_n_cache(n):
    sequence = []   
    if n in seq_cache:
        return seq_cache[n]    
    original_n = n
    sequence = []
    while n != 1:
        if n in seq_cache: 
            sequence.extend(seq_cache[n])
            break
        sequence.append(n)
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    sequence.append(1)  
    seq_cache[original_n] = sequence  
    return sequence

n = int(input("Please enter your number: "))

print("\nSequence without caching:")
print(generate_seq_n(n))

print("\nSequence with caching:")
print(generate_seq_n_cache(n))
print("\nCache :")
print(seq_cache)