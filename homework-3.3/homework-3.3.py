import requests
import os.path


def directory_exist():  # проверяем существование папки Result
    result = "Result"

    if os.path.exists(result) is False:
        os.mkdir('Result')


def get_translations(API, URL, text, from_lang, to_lang):
    params = dict(
        key=API,
        text=text,
        lang='{}-{}'.format(from_lang, to_lang)
    )

    response = requests.get(url=URL, params=params)

    return response


def resp_status(resp):
    if resp.status_code == 200:
        print("Код ответа {}. Перевод завершён!".format(resp.status_code))
    else:
        print("Код ответа {}! Что-то пошло не так..".format(resp.status_code))


def main():
    # Вводим необходимые переменные для API
    API = 'trnsl.1.1.20170612T092844Z.3dcd61750a7d75da.c6b01f07b225444678a712a42d48f793185fe344'
    URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    # Проверяем существование папки для выходных данных
    directory_exist()

    # Выбираем то, что будем переводить
    from_lang = input("Введите переводимый текст\n de - немецкий\n es - Испанский\n fr - французский")
    if from_lang == "de":
        from_lang = "de"
        lang_file = "DE.txt"
    elif from_lang == "es":
        from_lang = "es"
        lang_file = "ES.txt"
    elif from_lang == "fr":
        from_lang = "fr"
        lang_file = "FR.txt"

    # вводим необходимые переменные
    with open(os.path.join(os.getcwd(), 'Source', lang_file), 'r') as text:
        text = text.read()

    # Выбираем направление перевода
    to_lang = input("Введите направление перевода\nru - русский\nen - английский\n")

    # Посылаем данные в Я.Переводчег
    resp = get_translations(API, URL, text, from_lang, to_lang)

    # Читаем полученный перевод с Я.Переводчега
    response_text = resp.json()

    # Проверяем респонс-код
    resp_status(resp)

    # записываем в файл полученный перевод
    with open(os.path.join(os.getcwd(), 'Result', from_lang + "-to-" + to_lang + ".txt"), 'w') as f:
        for i in response_text['text']:
            f.write(i)


main()
