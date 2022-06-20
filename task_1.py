"""
Написати функцію `is_prime`, що приймає 1 аргумент - число від 0 до 1000,
і повертає `True`, якщо воно просте, і `False` - інакше.
(Прості числа - ті які діляться без залишку тільки на себе або 1, наприклад 2, 3, 5, 7, 11 ...)
"""
from random import randint


def is_prime(number: int) -> bool:
    if number % 2 == 0 and number < 1:
        return False
    for num in range(3, number):
        if number % num == 0:
            return False
    return True


def main():
    some_number = randint(0, 1000)
    if is_prime(some_number):
        print(f'Число {some_number} є простим.')
    else:
        print(f'Число {some_number} не є простим.')


if __name__ == '__main__':
    main()
