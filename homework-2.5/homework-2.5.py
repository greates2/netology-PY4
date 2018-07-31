import os
import subprocess


def get_path():
    source = "Source"
    source_path = os.listdir(source)

    return source_path


def directory_exist():
    result = "Result"

    if not os.path.exists(result):  # создаем папку Result если её нет
        os.mkdir('Result')


def main():
    directory_exist()  # проверяем существование папки

    for i in get_path():
        subprocess.run("{} {}{} -resize 200 {}{}".format(os.path.join(os.getcwd(), 'convert.exe'),
                        os.path.join(os.getcwd(), 'Source', ''), i, os.path.join(os.getcwd(), 'Result', ''), i))


if __name__ == "__main__":
    main()
