import cx_Oracle
from conexion import Conexion
from beautifultable import BeautifulTable

# Crear una instancia de la clase Conexion
conexion = Conexion()

# Obtener una conexión a la base de datos
conexion.getConnection()

opcion = 0
# Funcionalidades interactivas
while True:
    # Mostrar opciones disponibles al usuario
    table = BeautifulTable()
    table.column_headers = ["Opción", "Descripción"]
    table.append_row(["1", "Consultar datos de una tabla"])
    table.append_row(["2", "Realizar otra acción"])
    table.append_row(["0", "Salir"])

    print("Opciones disponibles:")
    print(table)

    # Obtener la opción del usuario
    opcion = input("Ingresa el número de la opción deseada: ")

    if opcion == "1":
        # Obtener el nombre de todas las tablas
        cursor = conexion.connection.cursor()
        cursor.execute("SELECT table_name FROM user_tables")
        tablas = [row[0] for row in cursor.fetchall()]
        cursor.close()

        # Mostrar nombres de las tablas utilizando BeautifulTable
        table = BeautifulTable()
        table.column_headers = ["Nombre de la tabla"]
        for tabla in tablas:
            table.append_row([tabla])

        print("Tablas disponibles:")
        print(table)

        # Consultar datos de una tabla
        tabla = input("Ingresa el nombre de la tabla: ")
        if tabla in tablas:
            cursor = conexion.connection.cursor()
            sql = f"SELECT * FROM {tabla}"
            cursor.execute(sql)
            resultados = cursor.fetchall()
            cursor.close()

            # Mostrar resultados utilizando BeautifulTable
            table = BeautifulTable()
            # Obtén los nombres de las columnas de la tabla
            cursor = conexion.connection.cursor()
            cursor.execute(f"SELECT column_name FROM user_tab_columns WHERE table_name = '{tabla}'")
            columnas = [row[0] for row in cursor.fetchall()]
            cursor.close()
            table.column_headers = columnas

            for resultado in resultados:
                table.append_row(resultado)

            print(f"Resultados de la tabla {tabla}:")
            print(table)
        else:
            print("¡La tabla ingresada no existe!")

    elif opcion == "2":
        # Otra acción
        # Implementa aquí la lógica para la otra acción que desees realizar
        print("Otra acción")

    elif opcion == "0":
        # Salir del programa
        break

    else:
        print("Opción inválida. Por favor, elige una opción válida.")

# Cerrar la conexión
conexion.connection.close()
