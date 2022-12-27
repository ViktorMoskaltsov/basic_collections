def get_input_parameters():
    amaunt_conteiner = int(input('Введите колличество контейнеров : '))
    container_list = []
    for _ in range (amaunt_conteiner):
        print('Введите вес контейнера ',end='')
        a = int(input())
        container_list.append(a)
    new_container = int(input('введите вес нового контейнера'))
    return container_list , new_container

    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(serial_number_new_container):
    print('Порядковый номер нового контейнера ',int(serial_number_new_container))
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def search_serial_number_new_container(list_container_weights, new_container_weight):
    new_number = 0
    for i  in range(len(list_container_weights)) :
        if new_container_weight == list_container_weights[len(list_container_weights)-1] :
            new_number = len(list_container_weights) + 1

        if new_container_weight > list_container_weights[i] :

            new_number = i + 1
            break

    return new_number



    # TODO: в этой функции пишем логику поиска куда вставим новый контейнер.
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
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат
