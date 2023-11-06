"""
Напишите программу-имитатор подбрасывания 2 кубиков.
Программа выводит на экран "подбрасываю кубики" и спустя 2 секунды выводит значения на кубиках в одну строку.
"""
from random import randint

first = 0
second = 0

while True:
    info = input("Введите 'off' для завершения ")

    if info == "off":
        break

    random_number = randint(1, 2)
    print("Ваш номер:", random_number)

    if random_number == 1:
        first+= 1
    else:
        second += 1

    print("Участников в первом забеге:", first)
    print("Участников во втором забеге:", second)