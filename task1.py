# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

day = int(input("Input day:"))
if day > 7 or day < 1:
    print("Wrong data")
elif day ==6 or day == 7:
    print("Weekend")
else:
    print("Workday")
