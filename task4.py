# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input("Input quarter:"))

if x < 1 or x > 4:
    print("Wrong data")
elif x ==1:
    print("x > 0, y > 0")
elif x ==2:
    print("x < 0, y > 0")
elif x ==3:
    print("x < 0, y < 0") 
elif x ==4:
    print("x > 0, y < 0")


