import Fcs_ordenamiento

#Ejemplo bubble sort
print('\n-----BUBBLE_SORT-----\n')
arr = [64, 25, 12, 22, 11]
print("Lista original:", arr)
Fcs_ordenamiento.bubble_sort(arr)
print("Lista ordenada:", arr)

#Ejemplo selection sort
print('\n-----SELECTION_SORT-----\n')
arr = [64, 25, 12, 22, 11]
print("Lista original:", arr)
Fcs_ordenamiento.selection_sort(arr)
print("Lista ordenada:", arr)

#Ejemplo insert sort
print('\n-----INSERT_SORT-----\n')
arr = [64, 25, 12, 22, 11]
print("Lista original:", arr)
Fcs_ordenamiento.insertion_sort(arr)
print("Lista ordenada:", arr)

#Ejemplo merge sort
print('\n-----MERGE_SORT-----\n')
arr = [64, 25, 12, 22, 11]
print("Lista original:", arr)
Fcs_ordenamiento.merge_sort(arr)
print("Lista ordenada:", arr)


'''Ejemplo count sort'''
arr = [4, 2, 2, 8, 3, 3, 1, 2, 4, 7]
ord_arr = Fcs_ordenamiento.count_sort(arr)
print("Lista ordenada por conteo:", ord_arr)