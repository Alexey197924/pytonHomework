"""
������������ ���������, ������� ����� ���������� ����� (��� �����),
���� ��������� ������������� � ��������� �����(���� ��� �������� ����� ������� �������). ������� ������������
������ ������ ��� ����� ��� ���������. ����� ����� �� ������ �������
���� �  ���������������� ��� ���������, �������� ��� ���� ������ ��
������ � �������� �� ��� ������� � ����� ����������. ����� ��� �������� ������� ��������� ���� � ����� ��� ����� ������������ ��������
"""
with open("example3.txt", "r", encoding='utf-8') as f:
    text=f.readlines()
    dictt = dict()
    for strings in text:
        string = strings.split()
        for sym in string:
            if dictt.get(sym) is not None:
                dictt[sym] += 1
            else:
                dictt[sym] = 1
    dictt = sorted(list(list(dictt.items())), key=lambda x: x[1], reverse=True)
    print(list(dictt)[0][0])