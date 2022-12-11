# TODO написать функцию для получения списка уникальных целых чисел
import random


def get_unique_list_numbers() -> list[int]:
    while True:
        uniq = [random.randint(-10, 10) for _ in range(15)]
        if len(uniq) == len(set(uniq)):
            return uniq
        else:
            continue


list_unique_number = get_unique_list_numbers()
print(list_unique_number)
print(len(list_unique_number) == len(set(list_unique_number)))

# Ответ
