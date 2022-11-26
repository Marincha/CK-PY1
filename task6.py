list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maximum, index_max = list_numbers[0], 0

for key, value in enumerate(list_numbers):
    if value >= maximum:
        maximum, index_max = value, key

list_numbers[index_max], list_numbers[-1] = list_numbers[-1], maximum

print(list_numbers)

# Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
