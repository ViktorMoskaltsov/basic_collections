def get_input_parameters():
    num_list = []
    a = int(input('Введите колличество цифр в сиске :'))
    for _ in range(a) :
        print('Ввеите знчение  ', end='')
        d = int(input())
        num_list.append(d)
    return num_list

    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(sorted_list):
    print('Отсортировнный список ',sorted_list)

    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def sort_list(original_list):
    for i_mn in range(len(original_list)) :
        for curr in range (i_mn,len(original_list)) :
            if original_list[curr] < original_list[i_mn]:
                original_list[curr],original_list[i_mn] = original_list[i_mn],original_list[curr]


    return original_list

    # TODO: в этой функции пишем логику сортировки списка.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    original_list = get_input_parameters()  # получаем параметры
    sorted_list = sort_list(original_list)  # сортируем список.
    display_result(sorted_list)  # выводим результат
