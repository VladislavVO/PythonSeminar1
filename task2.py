# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат



def table_of_truth():
    print(f'X\tY\tZ\tResult')#\t, \n
    print('-'*30)
    for x in [True, False]:
        for y in [True, False]:    
            for z in [True, False]:
                print(f'{x}\t{y}\t{z}\t{not(x or y or z) == (not x and not y and not z)}')

table_of_truth()