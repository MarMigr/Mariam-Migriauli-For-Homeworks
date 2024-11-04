from random import randint
nums = []

for  i in range (50):
    nums.append(randint(1, 30)) 
print(f"This is original list-{nums}")

nums_new = []

for num in nums:
    for _ in range(num):
        nums_new.append(num)
        
print(f"Here's a new list- {(nums_new)}")    
print(f"Length of this list is - {len(nums_new)}")      
