def get_input_parameters():
    words = input('Введите слово : ' )
    word_list = list(words)
    return word_list
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(is_palindrome):
    if is_palindrome == True :
        print('Слово является палиндромом')
    else:
        print('Слово не является  палиндромом')

    pass


def check_palindrome(word):
    check = False
    count = 0
    for i in range (int(len(word)/2)):
        if word[i] == word[-1-i] :
            count += 1
    if count == int(len(word)/2):
        check = True
    return check
    # TODO: в этой функции пишем логику проверки строки на палиндром.
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
    is_palindrome = check_palindrome(word)  # является ли слово палиндромом.
    display_result(is_palindrome)  # выводим результат
