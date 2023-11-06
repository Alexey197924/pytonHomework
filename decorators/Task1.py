"""
�������� ��������� ���������� ����� ���������� ������ �������.
"""
from time import time

# ��������� ����� ���
def decorate(func):
    def wrapper():
        start=time()
        func()
        end=time()
        print(end-start)
    return wrapper


@decorate
def func_to_decor():
    for i in range(1000):
        print(i)
func_to_decor()