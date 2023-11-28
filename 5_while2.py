"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например:
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user() которая с помощью функции input()
  просит пользователя ввести вопрос, а затем, если вопрос есть
  в словаре, программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""

questions_and_answers = {
    "what's the weather today?": "sunny",
    "got milk?": "no",
    "request": "response",
    "one": "two",
}


def ask_user(answers_dict: dict):
    while True:
        try:
            question = input("your question: ")
            try:
                print(answers_dict[question])
            except KeyError:
                print("sorry, try again")
        except (EOFError, KeyboardInterrupt):
            print("\n\ngood bye")
            break


if __name__ == "__main__":
    ask_user(questions_and_answers)
