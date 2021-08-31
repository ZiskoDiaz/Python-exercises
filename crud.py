import mysql.connector

midb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Uv6tq4ry',
    database='mydatabase'
)

cursor = midb.cursor()
# ver datos de la base de datos
cursor.execute('select * from Usuario')
resultado = cursor.fetchall()
print(resultado)

# ingresar datos a la db
sql = 'insert into Usuario (nombre, email, username) values(%s, %s, %s)'
values = ('juanchoman','juanchoman@mail.com','juanchomanxD')
# pasamos los datos para el ingreso
cursor.execute(sql, values)

midb.commit()
print(cursor.rowcount)
resultado = cursor.fetchall()

print(resultado)

# update

sql = 'update Usuario set email = %s where id = %s'
values = ('micorreodemierda@correo.com', 2)
cursor.execute(sql, values)

midb.commit()

# delete

sql = 'delete from Usuario where id = %s'
values(4, )
cursor.execute(sql, values)
midb.commit()
