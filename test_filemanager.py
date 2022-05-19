import bill
import filemanager
import victory


# тесты для каждой ""чистой"" функции
def test_author_info():
    assert filemanager.author_info() == 'Ural Kamaletdinov при сотрудничестве с neural-university.ru'


def test_check_for_correctness_input():
    assert victory.check_for_correctness_input('27.06.1977', 'мой день рождения')
    assert victory.check_for_correctness_input('27.Oб.I977', 'мой день рождения') == '    Введены не числа'


def test_date_to_str():
    assert victory.date_to_str('04.06.1975') == 'четвертого июня 1975 года'


# попробуем создать функционал через тестирование
# сначала пишем тест,
# потом добавляем фунционал и правки в программу
def test_wallet():
    wallet = bill.Wallet()
    assert wallet.get() == 0
    wallet.set(-100)            # установить счет в минус 100
    assert wallet.get() == 0    # счет не менятся
    wallet.set(100)             # установить счет в 100
    assert wallet.get() == 100
    wallet.refill(100)          # пополнить счет на 100
    assert wallet.get() == 200
    wallet.purchase(50)         # цена меньше или равна, чем доступно
    assert wallet.get() == 150
    wallet.purchase(500)        # цена больше, чем доступно
    assert wallet.get() == 150  # счет не менятся

# по идее можно в Wallet закинуть историю покупок,
# так же как история сохраняется и доступна в приложении Сбербанка
# Но это потом...
