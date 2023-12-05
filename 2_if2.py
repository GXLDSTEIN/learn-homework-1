"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main():
    print(check_str("hello", 2))
    print(check_str("hello", "hello"))
    print(check_str("very long hello", "hello"))
    print(check_str("hello", "learn"))


def check_str(first_str: str, second_str: str):
    if not (isinstance(first_str, str) and isinstance(second_str, str)):
        return 0
    if first_str is second_str:
        return 1
    if len(first_str) > len(second_str):
        return 2
    if second_str == "learn":
        return 3


if __name__ == "__main__":
    main()
