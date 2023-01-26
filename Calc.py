print(f"Калькулятор")

Operation = float(input("Введите количество операций: ")) 
Chislo1 = float(input("Введите первое число: ")) 


i = 0

while i < Operation:
    Chislo2 = float(input("Введите второе число: ")) 
    Action = input("1. Сложение " " 2. Вычитание " " 3. Деление " " 4. Умножение") 

    if Action == "1":
        Res = Chislo1 + Chislo2
        i+=1
        Chislo1 = Res
        print("Итог: " + str(Res))
        

    elif Action == "2":
        Res = Chislo1 - Chislo2
        i+=1
        Chislo1 = Res
        print("Итог: " + str(Res))

    elif (Action == "3") & (Chislo2 == 0):
        print("Делить нельзя")
    
    elif Action == "3":
        Res = Chislo1 / Chislo2
        i+=1
        Chislo1 = Res
        print("Итог: " + str(Res))

    elif Action == "4":
        Res = Chislo1 * Chislo2
        i+=1
        Chislo1 = Res
        print("Итог: " + str(Res))
