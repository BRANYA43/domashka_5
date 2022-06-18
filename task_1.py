"""
Написати функцію `is_prime`, що приймає 1 аргумент - число від 0 до 1000,
і повертає `True`, якщо воно просте, і `False` - інакше.
(Прості числа - ті які діляться без залишку тільки на себе або 1, наприклад 2, 3, 5, 7, 11 ...)
"""
from random import randint


def is_prime(number: int) -> bool:
    div = 2
    while number > div:
        if number % div != 0:
            div += 1
        else:
            return False
    else:
        print(number)
        return True


count = 0
for i in range(2, 1000):
    if is_prime(i):
        count += 1

print(count)
