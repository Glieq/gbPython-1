# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками(то есть разломить шоколадку на два прямоугольника).

# *Пример: *

# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
k = int(input("Сколько долек вы хотите отломить? "))
if (k > m*n):
    print("no")
    exit()
if (k % n == 0 or k % m == 0):
    print("yes")
else:
    print("no")
