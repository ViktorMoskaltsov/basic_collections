def get_input_parameters():
    num = int(input('Введите число  N : '))
    return num
def display_result(odd_numbers):
   print('Список из нечётных чисел от 1 до N: ', odd_numbers )
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    # pass


def get_odd_numbers(number):
    num_list = []
    num_resault = []
    for i in range(1, number + 1):
        num_list.append(i)
    for numbers in num_list:
        if numbers % 2 > 0:
            num_resault.append(numbers)
    return num_resault

    # TODO: в этой функции получаем отсортированный
    #  по возрастанию список нечётных чисел от 1 до number.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    number = get_input_parameters()  # получаем параметры
    odd_numbers = get_odd_numbers(number)  # получаем нечётные числа
    display_result(odd_numbers)  # выводим результат
