# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string


def generate_random_name():
    while True:
        # string.ascii_lowercase возвращает строку содержащую все строчные латинские буквы
        name1 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 15)))
        name2 = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(1, 15)))
        yield f"{name1} {name2}"


gen = generate_random_name()

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
