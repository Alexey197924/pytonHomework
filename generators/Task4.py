"""
Напишите генераторное выражения. Для генерации словаря где ключем выступают числа от 0 до 10. А значения эти же числа в 16чной системе счисления.
Работу с 16чной системой найдите в документации Python
"""
generate={i:hex(i) for i in range(0,100)}
for i, v in generate.items():
    print(i,v)