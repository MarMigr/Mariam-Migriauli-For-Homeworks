my_list=['Mar','Migriauli','python','bla','string','pix','Pho','SnaKe']
print(my_list)

filtered_list = [i.upper() for i in my_list if len(i) <= 3]
print(filtered_list)


