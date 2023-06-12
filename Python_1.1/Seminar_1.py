'''Задача 2: Найдите сумму цифр трехзначного числа.

*Пример:*

123 -> 6 (1 + 2 + 3)
100 -> 1 (1 + 0 + 0) |'''

'''Решение:

n = input("Введите трехзначное число: ")
n = int(n)
 
d1 = n % 10
d2 = n % 100 // 10
d3 = n // 100
 
print("Сумма цифр числа:", d1 + d2 + d3)'''


'''Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество 
журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?'''

'''Решение:

S = int(input())
Sergey = S / 6
Petr = Sergey
Ekaterina = (Sergey + Petr) * 2
print(int(Sergey), int(Ekaterina), int(Petr))

'''

'''Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали 
билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых 
трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
Вам требуется написать программу, которая проверяет счастливость билета.'''


'''
n = input("Введите шестизначный номер билета: ")
s1 = int(n[0]) + int(n[1]) + int(n[2])
s2 = int(n[3]) + int(n[4]) + int(n[5])
if s1 == s2:
  print("Билет счастливый")
else:
  print("Билет обычный")

'''

'''Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если 
разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).'''

'''
n = input("Введите длину шоколадки: ")
n = int(n)
m = input("Введите ширину шоколадки: ")
m = int(m)
k = input("Сколько долек нужно отломить: ")
k = int(k)
if k < n * m and ((k  % n == 0) or (k  % m == 0)):
    print("Можно отломить")
else:
    print("Нельзя отломить")

'''