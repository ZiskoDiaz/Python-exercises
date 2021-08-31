import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Uv6tq4ry',
    database='mydatabase'
)

cursor = midb.cursor()

cursor.execute('select * from Usuario')
resultado = cursor.fetchall()

print(resultado)
