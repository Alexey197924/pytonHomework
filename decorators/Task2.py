"""
�������� ��������� ����������� � ������ ���������� ����������� "�����" � "�������" � ������� �����������.
"""
def decorate(func):
    def wrapper():
        x=input("Введите ингредиент")

        func()
        print(x)
    return wrapper

@decorate
def eat():
    print("Хлеб", "Ветчина")

eat()