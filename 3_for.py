"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

from statistics import mean


def main():
    phones_list = [
        {
            "product": "iPhone 12",
            "items_sold": [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186],
        },
        {
            "product": "Xiaomi Mi11",
            "items_sold": [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316],
        },
        {
            "product": "Samsung Galaxy 21",
            "items_sold": [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247],
        },
    ]
    mean_all = 0
    sum_all = 0
    for phone in phones_list:
        m = mean(phone["items_sold"])
        s = sum(phone["items_sold"])
        print(f'{phone["product"]}: sum items sold {s}, mean items sold {round(m, 2)}')
        mean_all += m
        sum_all += s
    print(f"sum all sold: {sum_all / len(phones_list):.2f}")
    print(f"mean all sold: {mean_all / len(phones_list):.2f}")


if __name__ == "__main__":
    main()
