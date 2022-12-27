def get_input_parameters():
    cell_list = []
    cell = int(input('Введиет колво клеток : '))
    for i in range(cell):
        print('эфективность ', i+1, 'клетки', end='')
        a = int(input(':'))
        cell_list.append(a)
    return cell_list
    #:return: набор клеток, например: [3, 0, 6, 2, 10]
    #:rtype: List[int]
    #"""
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    #pass


def display_result(cells):
    print('Не подходящие значения',cells)
    #Выводим список клеток у которых значение меньше индекса

    #:param cells: набор клеток, например: [0, 2]
    #:type cells: List[int]
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    #pass


def select_cells(cells):
    cell_min = []
    for i in range(len(cells)) :
        if (i+1 ) > cells[i] :
            cell_min.append(cells[i])
    return cell_min


    #Отбираем список клеток, у которых значение меньше индекса.

    #:param cells: набор клеток, например: [3, 0, 6, 2, 10]
    #:type cells: List[int]

    #:return: набор подходящих клеток, например: [0, 2]
    #:rtype: List[int]
    #"""
    # TODO: в этой функции пишем логику отбора клеток.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    #pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    cells = get_input_parameters()  # получаем параметры
    result_cells = select_cells(cells)  # отбираем клетки
    display_result(result_cells)  # выводим результат
