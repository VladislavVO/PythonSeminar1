# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,2

from math import sqrt

xA = int(input("Input xA:"))
yA = int(input("Input yA:"))
xB = int(input("Input xB:"))
yB = int(input("Input yB:"))

dist = sqrt((xA-xB)**2+(yA-yB)**2)

print (round(dist,2))
