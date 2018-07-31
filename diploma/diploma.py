from pprint import pprint
import requests
import time
import json
import os

token = os.getenv('vk_token')
VERSION = "5.67"
# вводим 5030613 при запросе
input_user = int(input("Введите id пользователя за которым следим!\n"))


def groups_our_user():
    """
    получаем номера групп пользователя за которым следим
    в ключе 'user_id' записываем ВК-id нужного пользователя
    в ключе 'count' ограничиваем кол-во найденных групп у друга пользователя
    """
    params = {
        'access_token': token,
        'v': VERSION,
        'user_id': input_user,
        'count': 50,  # выбираем количество
    }

    response = requests.get('https://api.vk.com/method/groups.get', params)
    all_groups = response.json()['response']['items']
    print(".")

    return all_groups


def get_friends_our_user():
    """
    получаем друзей пользователя
    в ключе 'user_id' записываем ВК-id нужного пользователя
    в ключе 'count' огранич. количество найденных групп у друга пользователя
    в ключе 'fields' записываем доп. параметры которые необходимо получить
    """
    params = {
        'access_token': token,
        'v': VERSION,
        'user_id': input_user,
        'count': 50,  # выбираем количество
        'fields': 'screen_name',
    }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    friends_our_user = response.json()['response']['items']
    print(".")

    return friends_our_user


def get_all_groups_friends(all_groups=""):
    """
    получаем группы друзей пользователя
    в ключе 'user_id' записываем ВК-id нужного пользователя
    ключ 'extended' включает доп. поля из ключа 'fields'
    в ключе 'count' огранич. кол-во найденных групп у  друга пользователя
    в ключе 'fields' записываем доп. параметры которые необходимо получить

    Секция выполнения основной части программы:
    try - основная логика работы,
    проверяет отсутствие группы у группы исходного пользователя
    except в случае ошибки, выполняет эту секцию, чтобы не "ломать" программу
    """
    our_user_friends = get_friends_our_user()

    all_groups_on_user_friends = list()
    try:
        if all_groups:
            groups_name_count = list()
            for i in all_groups:
                params = {
                    'access_token': token,
                    'v': VERSION,
                    'user_id': i,
                    'extended': 1,
                    'fields': 'members_count',
                    'count': 50
                }
                resp = requests.get('https://api.vk.com/method/groups.get',
                                    params)
                groups_name_count.extend(resp.json()['response']['items'])
                print(".")
                time.sleep(1)

                return groups_name_count

        else:

            for i in our_user_friends:
                params = {
                    'access_token': token,
                    'v': VERSION,
                    'user_id': i['id'],
                    'extended': 0,
                    'count': 50
                }
                resp = requests.get('https://api.vk.com/method/groups.get',
                                    params)
                all_groups_on_user_friends.extend(resp.json()
                                                  ['response']['items'])
                print(".")
                time.sleep(0.4)

    except KeyError:
        for i in our_user_friends:
            params = {
                'access_token': token,
                'v': VERSION,
                'user_id': i['id'],
                'extended': 0,
                # 'fields': 'members_count',
                'count': 1
            }
            resp = requests.get('https://api.vk.com/method/groups.get', params)
            print(".")
            time.sleep(0.4)

    return all_groups_on_user_friends


def main():
    """
    Логика выполнения программы, последовательные шаги
    В конце - сохранение результатов в файл
    """
    our_user_group = groups_our_user()
    all_groups_on_user = get_all_groups_friends()

    user_friends_without_user_groups = list()
    for i in our_user_group:
        if i not in all_groups_on_user:
            user_friends_without_user_groups.append(i)

    result_groups = get_all_groups_friends(user_friends_without_user_groups)

    all_groups = list()
    for i in result_groups:
        result = {
            'name': i['name'],
            'gid': i['id'],
            'member_count': i['members_count']
        }

        all_groups.append(result)

    # закидываем полученные данные в файл
    with open('groups.json', 'w', encoding='utf8') as f:
        json.dump(all_groups, f, indent=2, ensure_ascii=False)
        print("Все данные в файле groups.json!")

if __name__ == "__main__":
    main()
