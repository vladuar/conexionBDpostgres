import psycopg2


try:
    connection=psycopg2.connect(
        host="localhost",
        user="postgres",
        password="admin",
        database="mitienda"
    )
    print("conexion exitosa")
    cursor=connection.cursor()
    cursor.execute("SELECT version()")
    row=cursor.fetchone()
    print(row)
except Exception as ex:
    print(ex)

finally:
    connection.close()
    print("conexion finalizada.")