"""
Напишите программу создающую .txt файл и записывающую туда строку "Я гений и стараюсь учить питон".
Выведите первые 7 символов файла на экран.
"""


with open("example.txt", "w+") as file:
    file.write("Я гений и стараюсь учить питон")
    file.seek(0)
    text=file.read()
print(text[:7])
