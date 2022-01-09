from datetime import datetime
import pytz
import random

def change_list(func_x):
    def wrapper(any_list):
        final_set= set(any_list)
        final_set= list(final_set)
        wrapper(any_list)
    return wrapper

@change_list
def say_hi(name):
    return f'{name} helloooo'


if __name__ == '__main__':
    final=change_list(["Diego","Paula","Fernando","Emma","Fernando","Paula"])
    print(final)