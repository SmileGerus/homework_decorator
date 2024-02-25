import os
import datetime
from functools import wraps


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        start_time = datetime.datetime.now()
        result = old_function(*args, **kwargs)
        if args is list:
            args = ''.join(args)
        if kwargs == {}:
            kwargs = ''
        if kwargs is dict:
            kwargs = '; '.join([f'{key.capitalize()}: {value}' for key, value in kwargs[0].items()])
        with open('main.log', 'w', encoding='utf-8') as f:
            f.write(f'{start_time},{old_function.__name__},{args},{kwargs},{result}')
        return result
    return new_function


@logger
def hello_world():
    return 'Hello World'


@logger
def summator(a, b=0):
    return a + b


print(hello_world())
print(summator(2, b=2))
print(summator(4.3, b=2.2))