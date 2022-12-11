
from pprint import pprint


def dictate(i):
    return{'bin': bin(i), 'dec': i, 'hex': hex(i), 'oct': oct(i)}


pprint([dictate(_) for _ in range(16)])

# Ответ
