import numpy as np

original_array = np.array(list(range(10)))  
print("Original Array:", original_array)

modified_array = np.where(original_array % 2 == 1, -1, original_array)
print("Modified Array (odd numbers replaced with -1):", modified_array)

two_dimensional_array = original_array.reshape(2, -1)
print("2D Array with two rows:\n", two_dimensional_array)

even_sums = np.sum(original_array[original_array % 2 == 0])
print("Sum of all even numbers:", even_sums)