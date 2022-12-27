def display_result(participants_names):
    print('первый день ',participants_names)
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    #pass


def get_participants_names(names):
    names_first_day = []
    a = len(names)
    for i in range (a):
        if i % 2 == 0 :
            names_first_day.append(names[i])
    return names_first_day
    #Получаем элементы списка только с чётными индексами.

    #:param names: список имён, например: ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    #:type names: List[str]

    #:return: список имён с чётными индексами , например: ["Артемий", "Влад", "Дима", "Женя"]
    #:rtype: List[str]

    # TODO: в этой функции получаем элементы списка только с чётными индексами..
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее инициализированные данные
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    #pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_participants_names и display_result
    participants_names = get_participants_names(
        ["Артемий", "Борис", "Влад", "Гоша", "Дима", "Евгений", "Женя", "Захар"]
    )  # получаем список имён с чётными индексами
    display_result(participants_names)  # выводим результат
