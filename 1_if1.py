"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь:
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат
  работы функции в переменную
* Вывести содержимое переменной на экран

"""


def main():
    """
    Запрашивает ввод возраста до тех пор, пока он не будет соответствовать условиям;
    выводит, чем занимается пользователь.
    """
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
        except ValueError:
            print("Введите целое положительное число от 0 до 150")
            continue
        if age < 0:
            print("Возраст не может быть отрицательным")
            continue
        else:
            break

    prediction = predict_life_stage(age)
    print(prediction)


def predict_life_stage(age: int):
    if age >= 0 and age < 7:
        return "Скорее всего, вы в детском саду."
    elif age >= 7 and age < 18:
        return "Скорее всего, вы учитесь в школе."
    elif age >= 18 and age < 23:
        return "Скорее всего, вы учитесь в ВУЗе."
    elif age >= 23 and age <= 150:
        return "Скорее всего, вы работаете."
    else:
        return "Некорректный ввод."


if __name__ == "__main__":
    main()
