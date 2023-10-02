cnt = int(input('Введите число'))
res = []
while cnt > 0:
    res.append(cnt % 10)
    cnt = cnt // 10
    res = res [::-1]
print(sum(res))