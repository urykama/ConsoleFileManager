def add_separators(func):
    '''
    функция func должна что-то выводить в консоль...
    и тогда ее вывод красиво выделяется сверху и снизу
    :param func:
    :return:
    '''

    def wrapper(*args, **kwargs):
        print('*' * 23)
        result = func(*args, **kwargs)
        print('*' * 23)
        return result

    return wrapper


@add_separators
def hello():
    print('Hello World!')


@add_separators
def my_sum(a, b):
    print(a + b)
    # return a + b


if __name__ == '__main__':
    hello()
    print(my_sum(2, 7))
