# Задание №1

print("--------------------- 1-е задание -------------------------")
import math

first_side = float(input("Длина первой стороны? "))
second_side = float(input("Длина второй стороны? "))
third_side = float(input("Длина третей стороны? "))

half_side = (first_side + second_side + third_side)/2
print("Полупериметр треугольника =", half_side)
area_geron = (half_side*(half_side - first_side)*(half_side - second_side)*(half_side - third_side))
print("Площадь треугольника по формуле Герона =", math.sqrt(area_geron))

# Задания №2

print("--------------------- 2-е задание -------------------------")
a = 50
b = 70
print(a, b)
a, b = b, a
print(a, b)

# Задание №3

print("--------------------- 3-е задание -------------------------")
one_var = -5432
two_var = 34567
print(one_var, two_var)
one_var = two_var - one_var
two_var = two_var - one_var
one_var = two_var + one_var
print(one_var, two_var)

# Задание №4

print("--------------------- 4-е задание -------------------------")
var_chet = float(input("Введите ваше число? "))
if var_chet % 2 == 0:
    print("Ваше число четное =", var_chet)
    var_chet **= 2
    print("Ваше число возводилось в квадрат =", var_chet)
else:
    print("Ваше число нечетное =", var_chet)
    var_chet *= 2
    print("Ваше число умножалось на 2 =", var_chet)
print("-----------------------------------------------------------")