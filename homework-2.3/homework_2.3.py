import json
import re
from pprint import pprint
from collections import Counter


def get_news_json(file, encoding):
    with open(file, encoding=encoding) as f:
        news_json = json.load(f)

    return news_json


def get_news(country_values):  # получаем словарь со значениями для разбора

    all_words = list()
    for item in country_values['rss']['channel']['item']:
        if isinstance(item['title'], str):
            it_values = item['title'] + item['description']
            all_words.append(it_values)
        else:
            it_values = item['title']['__cdata'] + item['description']['__cdata']
            all_words.append(it_values)

    # ищем регэкспом нужные значения, отбрасываем теги и прочее англицЫзмы, выбираем слова от 7 знаков
    cnt = Counter(x for x in re.findall(r'[А-я\']{7,}', str(all_words)))
    pprint(cnt.most_common(10))


def get_country_news():
    # данные о странах для поиска значений
    country_info = {
        'fr': ('newsfr.json', 'ISO-8859-5'),
        'cy': ('newscy.json', 'koi8-r'),
        'afr': ('newsafr.json', 'utf8'),
        'it': ('newsit.json', 'cp1251')
    }

    input_country = input("Введите страну \n it - Италия, cy - Кипр, afr - Африка, fr - Франция \n")

    file, encoding = country_info[input_country]

    country_values = get_news_json(file, encoding)

    get_news(country_values)


get_country_news()
