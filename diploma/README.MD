# Описание программы

Программа для сравнения групп исходного пользователя с его друзьями, на наличие общих групп и групп, в которых нет исходного пользователя.


# Запуск программы

Программа запускается при сохранении в py-файл и запуске в консоли или через IDE для python.

Сначала в ней нужно указать token для доступа к API-Вконтакте, для этого необходимо создать переменную окружения с
именем vk_token и вложить в неё токен для доступа в ВК (в поле 'token' на 6-й строке), после чего выбрать id пользователя
за которым необходимо следить.


# Переменные окружения

В Windows заходим в "панель управления" - "система" - "дополнительные параметры системы" - "переменные среды" и создать
переменную в разделе "системные переменные" и "переменные среды пользователя", где указать имя переменной - vk_token и
сам токен.

В Linux делаем так, в терминале пишем 'export vk_token=хэш-токена', чтобы оно сохранилось после перезагрузки, добавляем
эту переменную в файл ~/.bashrc (если стоит BASH).


# Пример результата

Результат выполнения программы будет сохранен в файле groups.json в виде JSON-файла.

Пример сохраненной выдачи:

[
  {
    "name": "Exist.ru",
    "gid": 37283330,
    "member_count": 78510
  },
  {
    "name": "Allrezina.ru- Wheels&Tyres",
    "gid": 37970626,
    "member_count": 640
  }
]