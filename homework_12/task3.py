from random import randint
nums = []

for  i in range (50):
    nums.append(randint(1, 30)) 
print(f"This is original list-{nums}")

nums_new = []

for num in nums:
    if num not in nums_new:
        nums_new.append(num)

print(f"Here's the list without duplicates {nums_new}")
print(f"length of this list is- {len(nums_new)}")        

