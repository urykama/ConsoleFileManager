"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы
При выполнении задания можно пользоваться любыми средствами
Для реализации основного меню можно использовать пример ниже или написать свой
"""
from decorator import add_separators


class Wallet():
    def __init__(self):
        self.__balance = 0

    def set(self, value):
        if value >= 0:
            self.__balance = value

    def get(self):
        return self.__balance

    @add_separators
    def purchase(self, product, price):
        '''
        Вся работа с файлами идет через: обработку исключений.
        Здесь замена if:else: на тернарный оператор не улучшит читаемость кода.
        :param product:
        :param price:
        :return:
        '''
        if self.__balance >= price:
            self.__balance -= price
            try:
                with open("purchase_history.txt", "a") as file:
                    file.write(f"{product} : {price}\n")
            except FileNotFoundError:
                print("Невозможно открыть файл")
                return
            self.safe_to_file()  # здесь сохраним в файл изменение баланса
            print(f'Покупка {product} : {price} руб.')
        else:
            print('Недостаточно средств')

    def refill(self, value):
        '''
        пополнение счета
        :param value:
        :return:
        '''
        if value > 0:
            self.__balance += value

    def safe_to_file(self):
        try:
            with open("balance.txt", "w") as file:
                file.write(str(self.__balance))
        except FileNotFoundError:
            print("Невозможно открыть файл")
        except TypeError:
            print('TypeError: int() argument must be a string, a bytes-like object or a real number, not ')

    def read_from_file(self):
        try:
            with open("balance.txt", "r") as file:
                self.__balance = int(file.readline())
        except FileNotFoundError:
            print("Невозможно открыть файл")
        except ValueError:
            self.__balance = 0

    @add_separators
    def history(self):
        try:
            with open("purchase_history.txt", "r") as file:
                for i in file.readlines():
                    print(i, end="")
                return  # file.readlines()
        except FileNotFoundError:
            print("Невозможно открыть файл")
        except ValueError:
            print('Нет истории покупок')


def run_bill():
    """
    Функция запускает программу личный счет
    :return:
    """
    wallet = Wallet()
    wallet.read_from_file()

    history = []
    run = True
    while run:
        print()
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        print(f'Ваш счет {wallet.get()}')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            cost = int(input('Введите сумму: '))
            wallet.refill(cost)
        elif choice == '2':
            product = input('Введит название покупки: ')
            cost = int(input('Введите сумму покупки: '))
            wallet.purchase(product, cost)
            # history.append((product, cost))

        elif choice == '3':
            wallet.history()
            '''
            history = (wallet.history())
            for i in history:
                print(i, end="")
            '''
        elif choice == '4':
            wallet.safe_to_file()
            run = False
        else:
            print('Неверный пункт меню')


if __name__ == '__main__':
    run_bill()
