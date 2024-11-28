from random import randint
my_dict_values=[randint(1,1000) for i in range(100)]
my_dict_keys=['even','odd']

even_count=sum(1 for i in my_dict_values if i % 2 == 0)
odd_count=sum(1 for i in my_dict_values if i % 2 != 0)

my_dict={my_dict_keys[0]: even_count, my_dict_keys[1]: odd_count}

print(my_dict)


