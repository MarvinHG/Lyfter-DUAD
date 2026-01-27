'''
3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
    1. Ejemplos:
    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`
'''
# Create the list
my_list = [4, 3, 6, 1, 7]
# Get the index of the last item in the list
last_item = len(my_list)-1
# Remove the las item on the list
deleted_item = my_list.pop(last_item)
# Insert the last item at the beginnig of the list
my_list.insert(0, deleted_item)
# Remove the original first element of the list
deleted_item2 = my_list.pop(1)
# Add the last deleted element to the endo of the list
my_list.append(deleted_item2)
# Print the final list with the first and last elements swapped
print(my_list)