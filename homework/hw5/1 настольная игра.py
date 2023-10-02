games = list()
game = input("Введите настольную игру(0-остановить ввод):").lower()

while game != '0':
     if game in games:
        print("Эта игра уже записана")
     else:
        games.append(game)
     game = input("Введите настольную игру(0-остановить ввод):").lower()

games.sort()
print(games)