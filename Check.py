import pyodbc
from os import system, name
import os.path
import time
import toOrder
import random
import datetime
now = datetime.datetime.now()
cnxn = pyodbc.connect('Driver={SQL Server};Server=DESKTOP-OD7QUTU\MYSERVIS;Database=Carbonara;Trusted_Connection=yes;')
cursor = cnxn.cursor()

def ChequeSumUpd(userId, currentIdCheck, endIdCarbonara):
    for row in cursor.execute(f"select * from [Check] inner join [User] on [User_ID] = [ID_User] where [ID_Check] = {currentIdCheck}"):
        count = row.Count_Carbonara
        cost = row.Cost_Carbonara
        sum = row.Sum_Order
    sum = 0
    sum += count * cost
    ingridientId = []
    for i in range(len(endIdCarbonara)):
        for row in cursor.execute(f"select * from [Carbonara_Ingridient] where [Carbonara_ID] = {endIdCarbonara[i]}"):
            ingridientId.append(row.Ingridient_ID)
    
    for id in range(len(ingridientId)):
        for row in cursor.execute(f"select * from [Ingridient] where [ID_Ingridient] = {ingridientId[id]}"):
            costIngridient = row.Cost_Ingridient
        sum += costIngridient

    cursor.execute(f"update [Check] set [Sum_Order] = {sum} where [ID_Check] = {currentIdCheck}")
    cnxn.commit()


def Cheque(userId, count):
    for row in cursor.execute("select * from [Carbonara]"):
        cost = row.Cost_Carbonara
    sum = count * cost
    currentTime = now.strftime("%d-%m-%Y %H:%M")
    random.seed()
    if random.randint(1, 10) > 5:
        ear = True
        random.seed()
        if random.randint(1, 10) > 5:
            detected = True
        else:
            detected = False
    else:
        ear = False
        detected = False
    
    
    cursor.execute("insert into [Check] ([User_ID], [Count_Carbonara], [Cost_Carbonara], [Sum_Order], [Time_Order], [Ear], [Noticed]) values (?, ?, ?, ?, ?, ?, ?)", 
                   (userId, count, cost, sum, currentTime, (1 if ear else 0), (1 if detected else 0)))
    cnxn.commit()

def DropCheque(userId, currentIdCheck):
    carbonaras = []
    for row in cursor.execute(f"select * from [Check_Carbonara] where [Check_ID] = {currentIdCheck}"):
        carbonaras.append(row.Carbonara_ID)
    for id in range(len(carbonaras)):
        cursor.execute(f"delete [Carbonara] where [ID_Carbonara] = {carbonaras[id]}")
        cnxn.commit()
    cursor.execute(f"delete [Check] where [ID_Check] = {currentIdCheck}")
    cnxn.commit()
    
    print("Возвращаемся в главное меню...")
    time.sleep(2)
    toOrder.toOrder(userId)