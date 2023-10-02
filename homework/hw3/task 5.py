num = input("Введите число")
num_last = int(num) % 10
num_mid = int(num) // 10
num_first = num_mid % 10
if int(num[-1]) %2 ==0 and sum([num_last, num_first])% 1 == 0:
    print("ваше число делится на 6")
else:
    print("Ваше число не делится на 6")