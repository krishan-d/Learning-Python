import mysql.connector as con

con_param = {"host": "localhost", "user": "root", "password": "0000"}
cnx = con.connect(**con_param)
try:
    cursor = cnx.cursor()

    cursor.execute("CREATE DATABASE Python_DB")
except Exception as e:
    print("Exception:", e)
finally:
    cnx.close()

db = con.connect(host='localhost', user='root', password='0000', database='python_db')
try:
    cursor = db.cursor()
    query = """CREATE TABLE STUDENT (
                       NAME  VARCHAR(20) NOT NULL,
                       BRANCH VARCHAR(50),
                       ROLL INT NOT NULL,
                       SECTION VARCHAR(5),
                       AGE INT)"""

    # drop_query = "DROP TABLE IF EXISTS STUDENT"
    cursor.execute(query)
except Exception as e:
    print("Exception:", e)

in_query = "INSERT INTO STUDENT (NAME, ROLL) VALUES (%s, %s)"
cursor.execute(in_query, ('Edwina', '20'))
# NOTE:
# For Insert, Update and Delete call commit().
db.commit()
print(cursor.rowcount)

db.close()
