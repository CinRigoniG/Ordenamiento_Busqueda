import Fcs_ordenamiento

#Búsqueda linel
print('\n-----LINEAR_SEARCH-----\n')
numbers = [1,2,3,4,5,6,7,8,9,10]
search_elem = 8

if(Fcs_ordenamiento.search_element(numbers, search_elem)):
    print(f'{search_elem} se encuentra en el arreglo.')
else:
    print(f'{search_elem} no se encuentra en el arreglo.')

print('\n-----LINEAR_SEARCH_2-----\n')
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
element = 9
result = Fcs_ordenamiento.search_element_2(array, element)

if result != -1:
    print(f"El elemento {element} se encuentra en el índice {result}.")
else:
    print(f"El elemento {element} no se encuentra en el arreglo.")

#Búsqueda binaria
print('\n-----BINARY_SEARCH-----\n')
array_2 = [1,2,3,4,5,6,7,8,9,10] #Esta lista debe estar ordenada, de lo contrario usar un método de ordenamiento.
element_2 = 5
result_2 = Fcs_ordenamiento.binary_search(array_2, element_2)

if(result_2 != -1):
    print(f"El elemento {element_2} se encuentra en el índice {result_2}.")
else:
    print(f"El elemento {element_2} no se encuentra en el arreglo.")
