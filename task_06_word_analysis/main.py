def get_input_parameters():
    words = input('Введите слово: ')
    return words
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(number_unique_letters):
    print('Колличество уникальных символов ',number_unique_letters)
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def count_number_unique_letters(word):
    symbol = list(word)
    unique = 0
    count = 0
    for i in symbol:
        count = 0
        for n in symbol :
            if n != i :
                count += 1
        if count == len(symbol) - 1 :
            unique += 1
    return unique


    # TODO: в этой функции пишем логику считаем количество уникальных букв в слове.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    word = get_input_parameters()  # получаем параметры
    number_unique_letters = count_number_unique_letters(word)  # считаем количество уникальных букв.
    display_result(number_unique_letters)  # выводим результат
