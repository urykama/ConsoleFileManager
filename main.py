# 1. Создать новый проект ""Консольный файловый менеджер"
# 2. В проекте реализовать следующий функционал:
# После запуска программы пользователь видит меню, состоящее из следующих пунктов:
# - создать папку;
# - удалить (файл/папку);
# - копировать (файл/папку);
# - просмотр содержимого рабочей директории;
# - посмотреть только папки;
# - посмотреть только файлы;
# - просмотр информации об операционной системе;
# - создатель программы;
# - играть в викторину;
# - мой банковский счет;
# - смена рабочей директории (*необязательный пункт);
# - выход.
# Так же можно добавить любой дополнительный функционал по желанию.

import os
import shutil
from victory import run_victory
from bill import run_bill

def user_input():
    '''
    ввод пользовательских данных
        можно вставить проверку правильности ввода:
    '''
    text = input('Введите имя папки: ')
    return text


def make_directory():
    path = user_input()
    try:
        os.mkdir(path)
    except OSError:
        print("Создать директорию %s не удалось" % path)
    else:
        print("Успешно создана директория %s " % path)


def remove_directory(path):
    try:
        os.rmdir(path)
    except OSError:
        print("Удалить директорию %s не удалось" % path)
    else:
        print("Успешно удалена директория %s" % path)


def remove_file_or_directory():
    path = user_input()
    if os.path.isfile(path):
        os.remove([path])
        print("Успешно удален файл %s" % path)
    else:
        print("Файл %s не существует!" % path)

    if os.path.isdir(path):
        remove_directory(path)


def copy_file_or_directory(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)


def list_directorys():
    return (list(i for i in os.listdir() if os.path.isdir(i)))


def list_files():
    return (list(i for i in os.listdir() if os.path.isfile(i)))


if __name__ == '__main__':
    while True:
        print("\n")
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. посмотреть только папки')
        print('6. посмотреть только файлы')
        print('7. просмотр информации об операционной системе')
        print('8. создатель программы')
        print('9. играть в викторину')
        print('0. мой банковский счет')
        print('c. смена рабочей директории (*необязательный пункт)')
        print('x. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            # после выбора пользователь вводит название папки, создаем её в рабочей директории;
            make_directory()
        elif choice == '2':
            # после выбора пользователь вводит название папки или файла,
            # удаляем из рабочей директории если такой есть
            remove_file_or_directory()
        elif choice == '3':
            # после выбора пользователь вводит название папки/файла и новое название папки/файла. Копируем;
            name = input('Введите имя папки/файла: ')
            new_name = input('Введите новое имя папки/файла: ')
            copy_file_or_directory(name, new_name)
        elif choice == '4':
            # вывод всех объектов в рабочей папке;
            print(os.listdir())
        elif choice == '5':
            # посмотреть только папки
            print(list_directorys())
        elif choice == '6':
            # посмотреть только файлы
            print(list_files())
        elif choice == '7':
            # вывести информацию об операционной системе (можно использовать пример из 1-го урока);
            print(f'Имя текущей ОС: {os.name}')
            print(os.environ)
        elif choice == '8':
            # вывод информации о создателе программы;
            print('Урал Аданисович Камалетдинов')
        elif choice == '9':
            # запуск игры викторина из предыдущего дз;
            print('Запускаем приложение Victory')
            run_victory()
        elif choice == '0':
            # запуск программы для работы с банковским счетом из предыдущего дз
            # (задание учебное, после выхода из программы управлением счетом
            # в главной программе сумму и историю покупок можно не запоминать);
            print('Запускаем приложение мой банковский счет')
            run_bill()
        elif choice == 'x':
            print('Завершение работы программы')
            break
        else:
            print('Неверный пункт меню')
