print(f"Подсчтет дней в году")

god = float(input("Введите год: ")) 
Number = 0
if (god % 4 == 0 and god % 100 != 0) or god % 400 == 0:
    Mas = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for kol in range(len(Mas)):
        for Quantity in range(Mas[kol]):
            Quantity += 1
            Number += sum(map(int, str(Quantity)))
    print(Number)
else:
    Massiv = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for kol in range(len(Massiv)):
        for Quantity in range(Massiv[kol]):
            Quantity += 1
            Number += sum(map(int, str(Quantity)))   
    print(Number)