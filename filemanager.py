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
from decorator import add_separators

def user_input():
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

'''
def copy_file_or_directory(name, new_name):
    if os.path.isdir(name):
        shutil.copytree(name, new_name)
    else:
        shutil.copyfile(name, new_name)
'''

def copy_file_or_directory(name, new_name):
    '''
    + тернарный оператор
    + обработка исключений
    :param name:
    :param new_name:
    :return:
    '''
    try:
        shutil.copytree(name, new_name) if os.path.isdir(name) else shutil.copyfile(name, new_name)
    except OSError:
        print("Копирование не удалось")
    else:
        print("Копирование выполнено")


def list_directorys():
    '''
    Здесь применен генератор для создания списка
    :return:
    '''
    return (list(i for i in os.listdir() if os.path.isdir(i)))


def list_files():
    '''
    Здесь применен генератор для создания списка
    :return:
    '''
    return (list(i for i in os.listdir() if os.path.isfile(i)))

@add_separators
def author_info():
    print('Ural Kamaletdinov при сотрудничестве с neural-university.ru')
    # return 'Ural Kamaletdinov при сотрудничестве с neural-university.ru'


if __name__ == '__main__':
    while True:
        print("\n")
        print('1. создать папку')
        print('2. удалить (файл/папку)')
        print('3. копировать (файл/папку)')
        print('4. просмотр содержимого рабочей директории')
        print('5. сохранить содержимое рабочей директории в файл')
        print('6. посмотреть только папки')
        print('7. посмотреть только файлы')
        print('8. просмотр информации об операционной системе')
        print('i. создатель программы')
        print('g. играть в викторину')
        print('b. мой банковский счет')
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
            # 6. Добавить пункт "сохранить содержимое рабочей директории в файл";
            print(list_files())
            print(list_directorys())
            try:  # создать файл listdir.txt (если он есть то пересоздать)
                # files: victory.py, bill.py, main.py
                # dirs: modules, packages
                with open("listdir.txt", "w") as file:
                    file.write(f"files: {', '.join(list_files())}\n" +
                               f"dirs: {', '.join(list_directorys())}")
            except FileNotFoundError:
                print("Невозможно открыть файл")
        elif choice == '6':
            # посмотреть только папки
            print(list_directorys())
        elif choice == '7':
            # посмотреть только файлы
            print(list_files())
        elif choice == '8':
            # вывести информацию об операционной системе (можно использовать пример из 1-го урока);
            print(f'Имя текущей ОС: {os.name}')
            print(os.environ)
        elif choice == 'i':
            # вывод информации о создателе программы;
            author_info()
            # print(author_info())
        elif choice == 'g':
            # запуск игры викторина из предыдущего дз;
            print('Запускаем приложение Victory')
            run_victory()
        elif choice == 'b':
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
