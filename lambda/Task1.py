"""
�������� ��������� ������� ����� ���������� ������������ ���� ����� ���� ������������ �� ������ off.
��������� ������ ��������� lambda-������� ��������� � ������� ����� ������� "�����".
"""
while True:
    name = input("Введите имя")
    if name == "off":
        break
    if name != "off":
        new_name=(lambda name:(name+" гений"))
        print(new_name(name))