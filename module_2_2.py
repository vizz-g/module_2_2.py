first = int(input('число 1: '))
second = int(input('число 2: '))
third = int(input('число 3: '))
if first == second and third == second:
    print("ВСЕ числа равны")
elif first == second or second == third:
    print('2 числа равны')
else:
    print('0 совпадений')

