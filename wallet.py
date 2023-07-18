from bs4 import BeautifulSoup
from conexion import Conexion



conexion = Conexion()

conexion.getConnection()

sql = "SELECT * FROM cargo"
conexion.cursor.execute(sql)

resultados = conexion.cursor.fetchall()

for resultado in resultados:
    print(resultado)



conexion.cursor.close()
conexion.connection.close()