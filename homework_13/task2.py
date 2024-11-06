from random import randint
first_list=[randint(1,100) for _ in range(10)]
second_list=[randint(1,100) for _ in range(10)]
third_list=[randint(1,100) for _ in range(10)]

print(f"first list- {first_list}")
print(f"second list- {second_list}")
print(f"third list- {third_list}")

sum_of_lists=[first_list[i]+second_list[i]+third_list[i] for i in range(len(first_list))]
print(f"sum of this lists in a new list- {sum_of_lists}")