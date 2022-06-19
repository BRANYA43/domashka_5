"""
Написати функцію яка поверне площу фігури: за замовчуванням трикутника, опціонально.
На вході 2 величини та параметр типу фігури.
"""
from random import randint


def get_area_figure(n1: int, n2=0, n3=0, figure=0) -> int | float:
    if figure == 0:
        return n1 * n2 / 2

    elif figure == 1:
        return n1 * n2

    elif figure == 2:
        return n1 ** 2

    elif figure == 3:
        return (n1 + n2) * n3 / 2

    elif figure == 4:
        return n1 ** 2 * 3.14

    elif figure == 5:
        return n1 * n2 * n3 / 2


def main():
    print(f'Трикутник S = {get_area_figure(randint(2, 25), randint(2, 25))}')
    print(f'Ромб S = {get_area_figure(randint(2, 25), randint(2, 25))}')
    print(f'Прямокутник S = {get_area_figure(randint(2, 25), randint(2, 25), figure=1)}')
    print(f'Параллелограмм S = {get_area_figure(randint(2, 25), randint(2, 25), figure=1)}')
    print(f'Квадрат S = {get_area_figure(randint(2, 25), figure=2)}')
    print(f'Трапеція S = {get_area_figure(randint(2, 25), randint(2, 25), randint(2, 25), figure=3)}')
    print(f'Коло S = {get_area_figure(randint(2, 25), figure=4)}')
    print(f'n-угольник S = {get_area_figure(randint(2, 25), randint(2, 25), randint(2, 25), figure=5)}')


if __name__ == '__main__':
    main()
