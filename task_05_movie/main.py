def get_input_parameters():
    lov_list = []
    films = int(input('Сколько фильмов хотите посмотреть : '))
    for i in range(films) :
        print('Введите название фильма : ',end='')
        a = input()
        lov_list.append(a)
    #Получаем список фильмов, которые пользователь хочет добавить в "любимые"

    #:return: добавляемые фильмы, например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    #:rtype: List[str]

    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    #pass
    return lov_list

def display_result(favorite_films, errors):
    for i in range (len(errors)) :
        print('Ошибка : фильма ',errors[i],' у нас нету')
    print('Ваш любимы список фильмов ',favorite_films)

    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    #pass


def add_favorite_film(new_favorite_films, available_films):
    love_list = []
    eror = []
    for i in new_favorite_films :
        if i in available_films :
            love_list.append(i)
        else:
            eror.append(i)
    return love_list , eror







#Добавляем фильмы в список "любимых".

    #:param new_favorite_films: фильмы, которые нужно добавить в "любимые",
     #      например: ["Леон", "Безумный Макс", "Мементо", "Царь горы"]
    #:type new_favorite_films: List[str]
    #:param available_films: фильмы, которые есть на киносайте,
          # например: ["Леон", "Назад в будущее", "Мементо"]
    #:type available_films: List[str]

    #:return: Список фильмов в списке "любимых" и список не найденных фильмов,
             #например: (["Леон", "Мементо"], ["Безумный Макс", "Царь горы"])
    #:rtype: Tuple[List[str], List[str]]
    # TODO: в этой функции пишем логику добавлениея фильмов в список "любимых".
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    #pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    available_films = [
        "Крепкий орешек", "Назад в будущее", "Таксист",
        "Леон", "Богемская рапсодия", "Город грехов",
        "Мементо", "Отступники", "Деревня"
    ]
    new_favorite_films = get_input_parameters()  # получаем параметры
    favorite_films, errors = add_favorite_film(
        new_favorite_films,
        available_films
    )  # добавлем фильмы в список "любимых".
    display_result(favorite_films, errors)  # выводим результат
