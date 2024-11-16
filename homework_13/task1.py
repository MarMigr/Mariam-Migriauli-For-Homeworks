from random import randint

my_list=[randint(10,1000000000) for i in range(100) ]
print(my_list)

min_len_element = min(my_list, key=lambda x: len(str(x)))
print(f"Element with minimal length is: {min_len_element}, length is: {len(str(min_len_element))}")

max_len_element = max(my_list, key=lambda x: len(str(x)))
print(f"Element with maximum length is: {max_len_element}, length is: {len(str(max_len_element))}")

print(f"sorted from minimum to maximum- {sorted(my_list, key=lambda x: len(str(x)))}")

print(f"sorted from maximum to minimum- {sorted(my_list, key=lambda x: len(str(x)),reverse=True)}")

