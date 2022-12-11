# TODO написать функцию генерации случайных паролей
import string
import random


def get_random_password() -> str:
    strr_ = string.digits + string.ascii_letters
    random_password = "".join(random.sample(strr_, 8))
    return random_password


print(get_random_password())

# Ответ
