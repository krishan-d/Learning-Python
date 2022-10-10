"""
Connect MYSQL database:
    pip install mysql-connector-python
"""
import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="0000", database="world")

try:
    print(dataBase)
    cursor = dataBase.cursor()
    query = "SELECT * FROM country LIMIT 4"
    cursor.execute(query)

    res = cursor.fetchall()
    for i in res: print(i)

except Exception as e:
    print(e)
finally:
    if dataBase.is_connected(): dataBase.close()

