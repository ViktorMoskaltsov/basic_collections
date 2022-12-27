def get_input_parameters():
    original_lis = []
    shift_inp = int(input('Введите сдвиг '))
    for _ in range (5):
        a = int(input())
        original_lis.append(a)
    return shift_inp , original_lis

    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(shifted_list):
    print('Сдвинутый список',shifted_list)
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def shift_list(shift, original_list):
    new_list = []
    for i in range (len(original_list)) :
        new_list.append(original_list[i-shift])
    return new_list
    # TODO: в этой функции пишем логику сдвига списка вправо на shift элементов.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
