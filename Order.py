import pyodbc
from os import system, name
import os.path
import time
import pathlib
from pathlib import Path
import Check
import OrderCompletion
cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-OD7QUTU\MYSERVIS;Database=Carbonara;Trusted_Connection=yes;')
cursor = cnxn.cursor()
endIdCarbonara = []
def Orders(adminId, userId):
    _ = system('cls')
    try:
        count = int(input("Сколько карбнары желаете?\n"
                          "0 - Выйти на главную\n"))
    except ValueError:
        print("Введены неверные данные")
        time.sleep(2)
        Orders(userId)
    if (count > 0):
        Check.Cheque(userId, count)

        for i in range(count):
            print(f"Собираем пасту №{i+1}... \n")

            ingridients = []
            addIngridients = True

            while addIngridients ==True:
                nameIngridient, costIngridient, typeIngridient = [], [], []
                print("Ингридиенты: \n")

                for row in cursor.execute("select * from [Ingridient] inner join [Type_Ingridient] on [Type_ID] = [ID_Type]"):
                    nameIngridient.append(row.Name_Ingridient)
                    costIngridient.append(row.Cost_Ingridient)
                    typeIngridient.append(row.Name_Type)


                print("0 - Не выбирать ингридиент\n")
                for i in range(len(nameIngridient)):
                    print(i+1, " - ", typeIngridient[i], " - ", nameIngridient[i], " - ", costIngridient[i], "Рублей \n")
                            
                for count in range(len(nameIngridient)):
                    countIngridient = count+1

                print("Выберите ингридиент: \n")
                try:
                    ingridient = int(input())
                except ValueError:
                    print("Введены неверные данные")
                    time.sleep(2)
                    Orders(userId)
                        
                if (ingridient <= countIngridient and ingridient > 0):
                    ingridients.append(ingridient-1)
                elif ingridient == 0:
                    print("Пожелания учтены\n")
                else:
                    print("Неправильный ингридиент.")
                    Orders(userId)

                continueAdd = input("Добавить еще один ингредиент?\n").lower()
                if continueAdd == "yes" or continueAdd == "да":
                    addIngridients = True
                elif continueAdd == "no" or continueAdd == "нет":
                    addIngridients = False
                else:
                    print("Ошибка выбора\n"
                    "Сброс заказа пасты...\n")
                    time.sleep(2)
                    Orders(userId)

            print("Заканчиваем сборку... \n"
                "Добавляются ингридиенты:\n")
            for i in range(len(ingridients)):
                print(nameIngridient[ingridients[i]], " - ", costIngridient[ingridients[i]], "Рублей \n")
                    
            time.sleep(5)

            cursor.execute(f"insert into [Carbonara] ([Cost_Carbonara]) values (100)")
            cnxn.commit()

            for row in cursor.execute(f"select top 1 * from [Carbonara] order by [ID_Carbonara] desc"):
                idCarbonara = row.ID_Carbonara

            endIdCarbonara.append(idCarbonara)
            idCurrentCarbonara = idCarbonara

            for ingrid in range(len(ingridients)):
                cursor.execute(f"insert into [Carbonara_Ingridient] ([Carbonara_ID], [Ingridient_ID]) values (?, ?)", (idCurrentCarbonara, ingridients[ingrid]+1))
                cnxn.commit()
                
            idCheck = []

            for row in cursor.execute("select * from [Check]"):
                idCheck.append(row.ID_Check)

            for id in range(len(idCheck)):
                currentIdCheck = idCheck[id]

            Check.ChequeSumUpd(userId, currentIdCheck, endIdCarbonara)
            
            print("Собрали вашу пасту :)")

        commit = input("Завершить оформление заказа?\n").lower()

        if commit == "yes" or commit == "да":
            print("Завершаем оформление заказа...\n")
            time.sleep(2)
            count = 1        
            OrderCompletion.CloseOrder(adminId, userId, currentIdCheck, endIdCarbonara, count)
        elif commit == "no" or commit == "нет":
            try:
                toOrder = int(input("Выберите действие: \n"
                    "1 - Продолжить оформление заказа\n"
                    "2 - Сбросить заказ\n"))
            except ValueError:
                print("Введены неверные данные")
                Check.DropCheque(userId, currentIdCheck)
                time.sleep(2)
                Orders(userId)
            if toOrder > 0 and toOrder <= 2:
                match toOrder:
                    case '1':
                        print("Продолжаем заказ...\n")
                        time.sleep(2)
                        Orders(userId)
                    case '2':
                        print("Сбрасываем заказ...\n")
                        time.sleep(2)
                        Check.DropCheque(userId, currentIdCheck)
                    case _:
                        print("Сбрасываем заказ...\n")
                        time.sleep(2)
                        Check.DropCheque(userId, currentIdCheck)
            else:
                print("Неверное действие. Возврат к оформлению заказа.")
                time.sleep(2)
                Check.DropCheque(userId, currentIdCheck)
                Orders(userId)
        else:
            print("Неверное действие. Возврат к оформлению заказа.")
            Check.DropCheque(userId, currentIdCheck)
            time.sleep(2)
            Orders(userId)
    elif count == 0:
        CloseOrder.CloseOrder(adminId, userId, currentIdCheck, endIdCarbonara, count)
    else:
        print("Введены неверные данные")
        time.sleep(2)
        Orders(userId)