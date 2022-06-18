"""
Написати функцію яка поверне площу фігури: за замовчуванням трикутника, опціонально.
На вході 2 величини та параметр типу фігури.
"""


def get_area_figure(n1: int, n2=0, n3=0, figure=0) -> int | float:
    figures = {
        'triangle': 0,
        'rhombus': 1,
        'polygon': 2,
        'squad': 3,
        'rectangle': 4,
        'parallelogram': 5,
        'trapezoid': 6,
        'circle': 7
    }
    if figures['triangle'] <= figure <= figures['polygon']:
        if n2 > 0:
            return n1 * n2 / 2

    elif figures['squad'] <= figure <= figures['parallelogram']:
        if n2 > 0:
            return n1 * n2
        else:
            return n1 ** 2

    elif figure == figures['trapezoid']:
        if n2 > 0 and n3 > 0:
            return (n1 + n2) * n3 / 2

    elif figure == figures['circle']:
        return n1 ** 2 * 3.14


def main():
    print(get_area_figure(10, 12))
    print(get_area_figure(10, 12, figure=1))
    print(get_area_figure(10, 12, figure=2))
    print(get_area_figure(10, figure=3))
    print(get_area_figure(10, 12, figure=4))
    print(get_area_figure(10, 12, figure=5))
    print(get_area_figure(10, 12, 8, figure=6))
    print(get_area_figure(10, figure=7))


if __name__ == '__main__':
    main()
