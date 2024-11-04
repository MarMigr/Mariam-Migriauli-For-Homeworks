def my_sort(lista,listb):
    my_list=[]
    while lista and listb:
        if lista[0] < listb[0]:
            my_list.append(lista[0])
            lista = lista[1:]
        else:
            my_list.append(listb[0])
            listb = listb[1:]     

    my_list.extend(lista)
    my_list.extend(listb)

    return my_list

def main():

    test = [([1, 3, 10], [0, 4, 7, 9])]
    
    for lista, listb in test:
        result = my_sort(lista, listb)
        print("Sorted list:", result)

main()            
        