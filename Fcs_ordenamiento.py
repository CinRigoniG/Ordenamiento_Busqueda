#Función para ordenamiento BUBBLE SORT
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # El último i elementos ya están en su lugar correcto, así que no es necesario revisarlos nuevamente
        for j in range(0, n-i-1):
            # Intercambia si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

#Función para ordenamiento SELECTION SORT
def selection_sort(arr):
    n = len(arr)
    
    # Iterar a través de todos los elementos del arreglo
    for i in range(n):
        # Encontrar el valor mínimo en el arreglo sin ordenar
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Intercambiar el elemento mínimo encontrado con el primer elemento sin ordenar
        arr[i], arr[min_index] = arr[min_index], arr[i]

#Función para ordenamiento INSERT SORT
def insertion_sort(arr):
    n = len(arr)
    
    # Recorremos desde el segundo elemento hasta el último
    for i in range(1, n):
        # Guardamos el valor actual para compararlo e insertarlo en la posición correcta
        current_value = arr[i]
        position = i
        
        # Movemos los elementos mayores hacia la derecha
        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1
        
        # Insertamos el valor actual en la posición correcta
        arr[position] = current_value

#Función para ordenamiento MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        # Dividir la lista en dos mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamada recursiva para ordenar ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Fusionar las dos mitades ordenadas
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

#Función búsqueda lineal
def search_element(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return True
    return False

def search_element_2(array, element):
    for i in range(len(array)):
        if array[i] == element:
            return i  # Se encontró el elemento, devolvemos su índice
    return -1  # El elemento no se encuentra en la lista

#Función búsqueda binaria
def binary_search(array, element):
    left = 0
    right = len(array)-1

    while left <= right:
        half = (left + right) // 2

        if array[half] == element:
            return half  # Se encontró el elemento, devolvemos su índice
        elif array[half] < element:
            left = half + 1
        else:
            right = half - 1

    return -1  # El elemento no se encuentra en la lista

'''Función COUNT_SORT'''
def count_sort(array):
    # Encuentra el valor máximo en la lista
    maxim = max(array)
    
    # Crea un arreglo auxiliar para contar las apariciones de cada número
    count = [0] * (maxim + 1)
    
    # Llena el arreglo de conteo con las apariciones de cada número
    for num in array:
        count[num] += 1
    
    # Reconstruye la lista ordenada a partir del arreglo de conteo
    array_ord = []
    for i in range(len(count)):
        for j in range(count[i]):
            array_ord.append(i)
    
    return array_ord

