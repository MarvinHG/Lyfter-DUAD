'''
4. Cree un programa que elimine todos los números impares de una lista.
    1. Ejemplos:
    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`
'''
# Create the list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Loop through the list backwards using range(start, stop, step)
    # len(my_list) - 1 → last index
    # -1 → stop before index 0
    # -1 → step backwards
for index in range(len(my_list)-1, -1 , -1):
    # Check if the current number is not divisible by 2
    if my_list[index] % 2 != 0:
        # Remove the number
        my_list.pop(index)
# Print the final list
print(my_list)