import cx_Oracle
from conexion import Conexion
from beautifultable import BeautifulTable

# Crear una instancia de la clase Conexion
conexion = Conexion()

# Obtener una conexión a la base de datos
conexion.getConnection()

# Función para validar el inicio de sesión
def iniciar_sesion():
    # Obtener el nombre de usuario y contraseña
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    # Aquí puedes agregar la lógica para validar el nombre de usuario y contraseña
    # Ejemplo de validación básica (solo para fines demostrativos)
    cursor = conexion.connection.cursor()
    cursor.execute(f"SELECT * FROM USUARIO WHERE nombre_usuario = '{username}' AND clave = '{password}'")
    resultado = cursor.fetchone()
    cursor.close()

    if resultado is not None:
        return resultado[3]  # Retorna el perfil del usuario
    else:
        print("Nombre de usuario o contraseña incorrectos")
        return None

# Iniciar sesión
perfil = None

while perfil is None:
    perfil = iniciar_sesion()

opcion = 0
# Mostrar opciones disponibles según el perfil
while opcion != "0":
    if perfil == "rrhh":
        # Resto del código para el perfil de RR.HH.
        print("Bienvenido, RR.HH.")
        table = BeautifulTable()
        table.columns.header = ["Opción", "Descripción"]
        table.append_row(["1", "Listar trabajadores"])
        table.append_row(["2", "Llenar ficha del trabajador"])
        table.append_row(["0", "Salir"])
        print("Opciones disponibles:")
        print(table)

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            # Lógica para listar trabajadores
            print("Listado de trabajadores:")
            cursor = conexion.connection.cursor()
            cursor.execute("SELECT T.id_trabajador, T.rut_trabajador, S.nombre_sexo, T.nombre_trabajador, C.nombre_cargo, T.direccion, T.telefono, T.clave_trabajador FROM Trabajador T JOIN SEXO S ON T.id_sexo_fk = S.id_sexo JOIN CARGO C ON T.id_cargo_fk = C.id_cargo ORDER BY T.id_trabajador ASC")
            resultados = cursor.fetchall()
            cursor.close()

            # Mostrar resultados utilizando BeautifulTable
            table = BeautifulTable()
            table.columns.header = ["ID Trabajador", "RUT", "Sexo", "Nombre", "Cargo", "Dirección", "Teléfono","Clave_trabajador"]

            for resultado in resultados:
                table.append_row(resultado)

            print(table)

        elif opcion == "2":
            # Lógica para llenar ficha del trabajador
            print("Llenar ficha del trabajador:")

            while True:
                # Solicitar datos personales del trabajador
                id_trabajador = input("Ingrese el ID del trabajador (Ingrese '0' para volver al menú): ")
                if id_trabajador == '0':
                    break
                nombre = input("Ingrese el nombre completo del trabajador: ")
                rut = input("Ingrese el RUT del trabajador: ")

                # Solicitar sexo del trabajador
                print("Sexo del trabajador:")
                cursor = conexion.connection.cursor()
                cursor.execute("SELECT * FROM SEXO")
                sexos = cursor.fetchall()
                cursor.close()

                sexo_table = BeautifulTable()
                sexo_table.columns.header = ["ID Sexo", "Nombre Sexo"]
                for sexo in sexos:
                    sexo_table.append_row(sexo)

                print(sexo_table)
                sexo_id = input("Ingrese el ID del sexo del trabajador: ")

                # Solicitar datos laborales del trabajador
                print("Cargo del trabajador:")
                cursor = conexion.connection.cursor()
                cursor.execute("SELECT * FROM CARGO")
                cargos = cursor.fetchall()
                cursor.close()

                cargo_table = BeautifulTable()
                cargo_table.columns.header = ["ID Cargo", "Nombre Cargo", "Descripción Cargo"]
                for cargo in cargos:
                    cargo_table.append_row(cargo)

                print(cargo_table)
                cargo_id = input("Ingrese el ID del cargo del trabajador: ")

                # Solicitar dirección y teléfono del trabajador
                direccion = input("Ingrese la dirección del trabajador: ")
                telefono = input("Ingrese el teléfono del trabajador: ")
                
                # Solicitar clave del trabajador
                clave_trabajador = input("Ingrese la clave del trabajador: ")

                # Insertar datos en la tabla Trabajador
                cursor = conexion.connection.cursor()
                cursor.execute(f"INSERT INTO Trabajador (id_trabajador, rut_trabajador, id_sexo_fk, nombre_trabajador, id_cargo_fk, direccion, telefono, clave_trabajador) VALUES ({id_trabajador}, '{rut}', {sexo_id}, '{nombre}', {cargo_id}, '{direccion}', '{telefono}', {clave_trabajador})")
                conexion.connection.commit()
                cursor.close()

                # Solicitar el ID del trabajador al usuario
                id_trabajador_fk = input("Ingrese el ID del trabajador: ")

                # Generar nombre de usuario y contraseña
                usuario = nombre.replace(" ", "").lower()
                contraseña = str(clave_trabajador)

                # Insertar nombre de usuario, contraseña y ID de trabajador en la tabla USUARIO_TRABAJADOR
                cursor = conexion.connection.cursor()
                cursor.execute(f"INSERT INTO USUARIO_TRABAJADOR (nombre_usuario, contraseña, id_trabajador_fk) VALUES ('{usuario}', '{contraseña}', {id_trabajador_fk})")
                conexion.connection.commit()
                cursor.close()

                print("Datos del trabajador agregados correctamente.")
                print("Usuario y contraseña generados correctamente.")



                # Solicitar área del trabajador
                print("Área del trabajador:")
                cursor = conexion.connection.cursor()
                cursor.execute("SELECT * FROM AREA")
                areas = cursor.fetchall()
                cursor.close()

                area_table = BeautifulTable()
                area_table.columns.header = ["ID Área", "Nombre Área", "Descripción Área"]
                for area in areas:
                    area_table.append_row(area)

                print(area_table)
                area_id = input("Ingrese el ID del área del trabajador: ")

                # Solicitar departamento del trabajador
                print("Departamento del trabajador:")
                cursor = conexion.connection.cursor()
                cursor.execute("SELECT * FROM DEPARTAMENTO")
                departamentos = cursor.fetchall()
                cursor.close()

                departamento_table = BeautifulTable()
                departamento_table.columns.header = ["ID Departamento", "Nombre Departamento", "Descripción Departamento"]
                for departamento in departamentos:
                    departamento_table.append_row(departamento)

                print(departamento_table)
                departamento_id = input("Ingrese el ID del departamento del trabajador: ")

                # Solicitar fecha de ingreso a la compañía del trabajador
                fecha_ingreso = input("Ingrese la Fecha de Ingreso a la Compañía (formato: YYYY-MM-DD): ")

                # Insertar datos en la tabla DatosLaborales
                cursor = conexion.connection.cursor()
                cursor.execute(f"INSERT INTO DATOSLABORALES (id_datoslaborales, id_cargo_fk, id_area_fk, id_departamento_fk, fechaingreso) VALUES ({id_trabajador}, {cargo_id}, {area_id}, {departamento_id}, TO_DATE('{fecha_ingreso}', 'YYYY-MM-DD'))")
                conexion.connection.commit()
                cursor.close()

                print("Datos laborales del trabajador agregados correctamente.")

                # Opciones adicionales después de ingresar los datos personales
                opcion_datos = ""
                while opcion_datos != "0":
                    print("¿Desea agregar los siguientes datos del trabajador?")
                    table_datos = BeautifulTable()
                    table_datos.columns.header = ["Opción", "Descripción"]
                    table_datos.append_row(["1", "Contactos de emergencia"])
                    table_datos.append_row(["2", "Cargas familiares"])
                    table_datos.append_row(["0", "Volver al menú secundario"])

                    print("Opciones disponibles:")
                    print(table_datos)

                    opcion_datos = input("Ingrese el número de la opción deseada: ")

                    if opcion_datos == "1":
                        # Lógica para ingresar datos de contactos de emergencia
                        print("Contactos de emergencia del trabajador:")

                        while True:
                            # Solicitar datos de contacto de emergencia
                            id_contacto_emergencia = input("ID del contacto de emergencia (Ingrese '0' para volver al menú): ")
                            if id_contacto_emergencia == '0':
                                break

                            id_trabajador_fk = input("ID del trabajador: ")
                            nombre_contacto = input("Nombre del contacto: ")

                            print("Relaciones disponibles:")
                            cursor = conexion.connection.cursor()
                            cursor.execute("SELECT * FROM RELACION")
                            relaciones = cursor.fetchall()
                            cursor.close()

                            relaciones_table = BeautifulTable()
                            relaciones_table.columns.header = ["ID Relación", "Nombre Relación"]
                            for relacion in relaciones:
                                relaciones_table.append_row(relacion)

                            print(relaciones_table)
                            id_relacion_fk = input("Ingrese el ID de la relación del contacto: ")

                            telefono_contacto = input("Teléfono del contacto: ")

                            # Insertar datos en la tabla CONTACTODEEMERGENCIA
                            cursor = conexion.connection.cursor()
                            try:
                                cursor.execute(f"INSERT INTO CONTACTODEEMERGENCIA (id_contacto_emergencia, id_trabajador_fk, nombre_contacto, id_relacion_fk, telefono_contacto) VALUES ({id_contacto_emergencia}, {id_trabajador_fk}, '{nombre_contacto}', {id_relacion_fk}, '{telefono_contacto}')")
                                conexion.connection.commit()
                                print("Datos del contacto de emergencia agregados correctamente.")
                            except cx_Oracle.DatabaseError as e:
                                print("Error al ingresar los datos del contacto de emergencia. Por favor, vuelva a intentarlo.")
                                print(e)

                        # Volver a la parte donde se presentan las opciones

                    elif opcion_datos == "2":
                        # Lógica para ingresar cargas familiares
                        print("Cargas familiares del trabajador:")
                        cargas_familiares = []
                        while True:
                            nombre_carga = input("Nombre de la carga familiar (Ingrese '0' para volver al menú): ")
                            if nombre_carga == '0':
                                break
                            parentesco_carga = input("Parentesco con el trabajador: ")
                            id_carga_familiar = input("ID de la carga familiar: ")
                            id_trabajador_fk = input("ID del trabajador: ")
                            
                            # Solicitar sexo de carga familiar
                            print("Sexo de la carga familiar:")
                            cursor = conexion.connection.cursor()
                            cursor.execute("SELECT * FROM SEXO")
                            sexos = cursor.fetchall()
                            cursor.close()

                            sexo_table = BeautifulTable()
                            sexo_table.columns.header = ["ID Sexo", "Nombre Sexo"]
                            for sexo in sexos:
                                sexo_table.append_row(sexo)

                            print(sexo_table)
                            sexo_carga = input("Ingrese el ID del sexo de la carga familiar: ")

                            rut_carga = input("RUT de la carga familiar: ")

                            cargas_familiares.append((id_carga_familiar, id_trabajador_fk, nombre_carga, parentesco_carga, sexo_carga, rut_carga))

                        # Insertar datos en la tabla CargasFamiliares
                        cursor = conexion.connection.cursor()
                        for carga in cargas_familiares:
                            id_carga_familiar, id_trabajador_fk, nombre_carga, parentesco_carga, sexo_carga, rut_carga = carga
                            cursor.execute(f"INSERT INTO CargasFamiliares (id_carga_familiar, id_trabajador_fk, nombre_carga, parentesco, sexo_carga, rut_carga) VALUES ({id_carga_familiar}, {id_trabajador_fk}, '{nombre_carga}', '{parentesco_carga}', '{sexo_carga}', '{rut_carga}')")
                        conexion.connection.commit()
                        cursor.close()

                    print("Cargas familiares del trabajador agregadas correctamente.")

    # Volver a la parte donde se presentan las opciones

    elif perfil == "jefe_rrhh":
        # Resto del código para el perfil de jefe de RR.HH.
        print("Bienvenido, jefe de RR.HH.")
        table = BeautifulTable()
        table.columns.header = ["Opción", "Descripción"]
        table.append_row(["1", "Listar trabajadores"])
        table.append_row(["2", "Filtrar trabajadores"])
        table.append_row(["0", "Salir"])
        print("Opciones disponibles:")
        print(table)

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            # Lógica para listar trabajadores
            print("Listado de trabajadores:")
            cursor = conexion.connection.cursor()
            cursor.execute("SELECT T.id_trabajador, T.rut_trabajador, S.nombre_sexo, T.nombre_trabajador, C.nombre_cargo, T.direccion, T.telefono FROM Trabajador T JOIN SEXO S ON T.id_sexo_fk = S.id_sexo JOIN CARGO C ON T.id_cargo_fk = C.id_cargo ORDER BY T.id_trabajador ASC")
            resultados = cursor.fetchall()
            cursor.close()

            # Mostrar resultados utilizando BeautifulTable
            table = BeautifulTable()
            table.columns.header = ["ID Trabajador", "RUT", "ID Sexo", "Nombre", "ID Cargo", "Dirección", "Teléfono"]

            for resultado in resultados:
                table.append_row(resultado)

            print(table)

        elif opcion == "2":
            # Lógica para filtrar trabajadores
            print("Filtrando trabajadores...")
            table = BeautifulTable()
            table.columns.header = ["Opción", "Descripción"]
            table.append_row(["1", "Filtrar por sexo"])
            table.append_row(["2", "Filtrar por cargo"])
            table.append_row(["3", "Filtrar por área y departamento"])
            table.append_row(["0", "Volver"])
            print(table)

            subopcion = input("Ingrese el número de la opción deseada: ")

            if subopcion == "1":
                # Lógica para filtrar por sexo
                print("Filtrando por sexo...")
                cursor = conexion.connection.cursor()
                cursor.execute("SELECT * FROM SEXO")
                sexos = cursor.fetchall()
                cursor.close()

                sexos_table = BeautifulTable()
                sexos_table.columns.header = ["ID Sexo", "Nombre Sexo"]
                for sexo in sexos:
                    sexos_table.append_row(sexo)

                print(sexos_table)

                sexo_id = input("Ingrese el ID del sexo para filtrar los trabajadores: ")

                # Consultar trabajadores por sexo
                cursor = conexion.connection.cursor()
                cursor.execute(f"SELECT id_trabajador, rut_trabajador, id_sexo_fk, nombre_trabajador, id_cargo_fk, direccion, telefono FROM Trabajador WHERE id_sexo_fk = {sexo_id}")
                trabajadores_sexo = cursor.fetchall()
                cursor.close()

                trabajadores_sexo_table = BeautifulTable()
                trabajadores_sexo_table.columns.header = ["ID Trabajador", "RUT", "ID Sexo", "Nombre", "ID Cargo", "Dirección", "Teléfono"]

                for trabajador in trabajadores_sexo:
                    trabajadores_sexo_table.append_row(trabajador)

                print("Trabajadores filtrados por sexo:")
                print(trabajadores_sexo_table)

            elif subopcion == "2":
                # Lógica para filtrar por cargo
                print("Filtrando por cargo...")
                cursor = conexion.connection.cursor()
                cursor.execute("SELECT * FROM CARGO")
                cargos = cursor.fetchall()
                cursor.close()

                cargo_table = BeautifulTable()
                cargo_table.columns.header = ["ID Cargo", "Nombre Cargo", "Descripción Cargo"]

                for cargo in cargos:
                    cargo_table.append_row(cargo)

                print(cargo_table)

                cargo_id = input("Ingrese el ID del cargo para filtrar los trabajadores: ")

                # Consultar trabajadores por cargo
                cursor = conexion.connection.cursor()
                cursor.execute(f"SELECT id_trabajador, rut_trabajador, id_sexo_fk, nombre_trabajador, id_cargo_fk, direccion, telefono FROM Trabajador WHERE id_cargo_fk = {cargo_id}")
                trabajadores = cursor.fetchall()
                cursor.close()

                trabajadores_table = BeautifulTable()
                trabajadores_table.columns.header = ["ID Trabajador", "RUT", "ID Sexo", "Nombre", "ID Cargo", "Dirección", "Teléfono"]

                for trabajador in trabajadores:
                    trabajadores_table.append_row(trabajador)

                print("Trabajadores filtrados por cargo:")
                print(trabajadores_table)

            elif subopcion == "3":
                print("Filtrando por área y departamento...")
                table = BeautifulTable()
                table.column_headers = ["Opción", "Descripción"]
                table.append_row(["1", "Filtrar por área"])
                table.append_row(["2", "Filtrar por departamento"])
                print(table)

                subopcion_area_departamento = input("Ingrese el número de la opción deseada: ")

                if subopcion_area_departamento == "1":
                    # Filtrar por área
                    print("Filtrando por área...")
                    cursor = conexion.connection.cursor()
                    cursor.execute("SELECT * FROM AREA")
                    areas = cursor.fetchall()
                    cursor.close()

                    area_table = BeautifulTable()
                    area_table.column_headers = ["ID Área", "Nombre Área", "Descripción Área"]

                    for area in areas:
                        area_table.append_row(area)

                    print("Áreas disponibles:")
                    print(area_table)

                    area_id = input("Ingrese el ID del área para filtrar los trabajadores: ")

                    # Consultar trabajadores por área
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"""
                    SELECT T.id_trabajador, T.rut_trabajador, T.id_sexo_fk, T.nombre_trabajador, T.id_cargo_fk, T.direccion, T.telefono, DL.id_area_fk
                    FROM Trabajador T
                    JOIN FICHA F ON T.id_trabajador = F.id_trabajador_fk
                    JOIN DATOSLABORALES DL ON F.id_datoslaborales_fk = DL.id_datoslaborales
                    WHERE DL.id_area_fk = {area_id}
                """)


                    trabajadores = cursor.fetchall()
                    cursor.close()

                    trabajadores_table = BeautifulTable()
                    trabajadores_table.column_headers = ["ID Trabajador", "RUT", "ID Sexo", "Nombre", "ID Cargo", "Dirección", "Teléfono", "ID Área"]

                    trabajadores_table.max_width = None  # Cambiar la configuración de max_width

                    for trabajador in trabajadores:
                        trabajadores_table.append_row(trabajador)

                    print("Trabajadores filtrados por área:")
                    print(trabajadores_table)


                elif subopcion_area_departamento == "2":
                    # Filtrar por departamento
                    print("Filtrando por departamento...")
                    cursor = conexion.connection.cursor()
                    cursor.execute("SELECT * FROM DEPARTAMENTO")
                    departamentos = cursor.fetchall()
                    cursor.close()

                    departamento_table = BeautifulTable()
                    departamento_table.column_headers = ["ID Departamento", "Nombre Departamento", "Descripción Departamento"]

                    for departamento in departamentos:
                        departamento_table.append_row(departamento)

                    print("Departamentos disponibles:")
                    print(departamento_table)

                    departamento_id = input("Ingrese el ID del departamento para filtrar los trabajadores: ")

                    # Consultar trabajadores por departamento
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"SELECT T.id_trabajador, T.rut_trabajador, T.id_sexo_fk, T.nombre_trabajador, T.id_cargo_fk, T.direccion, T.telefono FROM Trabajador T JOIN FICHA F ON T.id_trabajador = F.id_trabajador_fk JOIN DATOSLABORALES DL ON F.id_datoslaborales_fk = DL.id_datoslaborales WHERE DL.id_departamento_fk = {departamento_id}")
                    trabajadores = cursor.fetchall()
                    cursor.close()

                    trabajadores_table = BeautifulTable()
                    trabajadores_table.column_headers = ["ID Trabajador", "RUT", "ID Sexo", "Nombre", "ID Cargo", "Dirección", "Teléfono"]

                    for trabajador in trabajadores:
                        trabajadores_table.append_row(trabajador)

                    print("Trabajadores filtrados por departamento:")
                    print(trabajadores_table)

                else:
                    print("Opción inválida. Por favor, elija una opción válida.")

            elif subopcion == "0":
                # Volver al menú principal
                continue

            else:
                print("Opción inválida. Por favor, elija una opción válida.")

        elif opcion == "0":
            # Salir del programa
            print("¡Hasta luego!")

        else:
            print("Opción inválida. Por favor, elija una opción válida.")


    elif perfil == "trabajador":
        print("Bienvenido, Trabajador.")
        opcion = ""

        while opcion != "0":
            table = BeautifulTable()
            table.columns.header = ["Opción", "Descripción"]
            table.append_row(["1", "Mirar tus Datos"])
            table.append_row(["0", "Salir"])
            print("Opciones disponibles:")
            print(table)

            opcion = input("Ingrese el número de la opción deseada: ")

            if opcion == "1":
                nombre_trabajador = input("Ingrese su nombre (Ingrese '0' para volver al menú): ")

                if nombre_trabajador == "0":
                    break

                clave_trabajador = input("Ingrese su clave: ")

                cursor = conexion.connection.cursor()
                cursor.execute(f"SELECT * FROM Trabajador WHERE nombre_trabajador = '{nombre_trabajador}' AND clave_trabajador = '{clave_trabajador}'")
                resultado = cursor.fetchone()
                cursor.close()

                if resultado is not None:
                    # Mostrar los datos del trabajador utilizando BeautifulTable
                    table_datos = BeautifulTable()
                    table_datos.columns.header = ["ID Trabajador", "RUT", "ID Sexo", "Nombre", "ID Cargo", "Dirección", "Teléfono", "Clave_trabajador"]
                    table_datos.append_row(resultado)

                    print("Tus Datos:")
                    print(table_datos)

                    pk_trabajador = resultado[0]  # Obtener el PK del trabajador

                    # Buscar en la tabla DATOSLABORALES utilizando el PK del trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"SELECT * FROM DATOSLABORALES WHERE id_datoslaborales = {pk_trabajador}")
                    resultado_datoslaborales = cursor.fetchone()
                    cursor.close()

                    if resultado_datoslaborales is not None:
                        # Mostrar los datos laborales del trabajador utilizando BeautifulTable
                        table_datoslaborales = BeautifulTable()
                        table_datoslaborales.columns.header = ["ID Datos Laborales", "ID Cargo", "ID Departamento", "Fecha Ingreso", "ID Área"]
                        fecha_ingreso = resultado_datoslaborales[3].strftime("%Y-%m-%d")
                        table_datoslaborales.append_row([resultado_datoslaborales[0], resultado_datoslaborales[1], resultado_datoslaborales[2], fecha_ingreso, resultado_datoslaborales[4]])

                        print("Tus Datos Laborales:")
                        print(table_datoslaborales)
                    else:
                        print("El trabajador no tiene datos laborales.")

                    # Buscar en la tabla CONTACTODEEMERGENCIA utilizando el PK del trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"SELECT * FROM CONTACTODEEMERGENCIA WHERE id_trabajador_fk = {pk_trabajador}")
                    resultado_contactoemergencia = cursor.fetchone()
                    cursor.close()

                    if resultado_contactoemergencia is not None:
                        # Mostrar los datos de contacto de emergencia utilizando BeautifulTable
                        table_contactoemergencia = BeautifulTable()
                        table_contactoemergencia.columns.header = ["ID Contacto Emergencia", "ID Trabajador", "Nombre Contacto", "ID Relación", "Teléfono Contacto"]
                        table_contactoemergencia.append_row(resultado_contactoemergencia)

                        print("Datos de Contacto de Emergencia:")
                        print(table_contactoemergencia)
                    else:
                        print("El trabajador no tiene datos de contacto de emergencia.")

                    # Buscar en la tabla CARGASFAMILIARES utilizando el PK del trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"SELECT * FROM CARGASFAMILIARES WHERE id_trabajador_fk = {pk_trabajador}")
                    resultados_cargasfamiliares = cursor.fetchall()
                    cursor.close()

                    if len(resultados_cargasfamiliares) > 0:
                        # Mostrar los datos de cargas familiares utilizando BeautifulTable
                        table_cargasfamiliares = BeautifulTable()
                        table_cargasfamiliares.columns.header = ["ID Carga Familiar", "ID Trabajador", "Nombre Carga", "Parentesco", "Sexo Carga", "RUT Carga"]
                        for carga_familiar in resultados_cargasfamiliares:
                            table_cargasfamiliares.append_row(carga_familiar)

                        print("Datos de Cargas Familiares:")
                        print(table_cargasfamiliares)

                    # Opción para editar los datos del trabajador
                    opcion_edicion = ""

                    while opcion_edicion != "0":
                        table_opciones_edicion = BeautifulTable()
                        table_opciones_edicion.columns.header = ["Opción", "Descripción"]
                        table_opciones_edicion.append_row(["1", "Sí"])
                        table_opciones_edicion.append_row(["0", "No"])
                        print("Desea editar sus datos?")
                        print(table_opciones_edicion)
                        opcion_edicion = input("Ingrese el número de la opción deseada: ")

                        if opcion_edicion == "1":
                            # Mostrar la lista de atributos para modificar
                            lista_atributos = ["Nombre", "Dirección", "Teléfono", "Nombre Contacto", "Teléfono Contacto", "Nombre Carga", "Parentesco", "RUT Carga"]
                            print("Atributos disponibles para modificar:")
                            table_atributos = BeautifulTable()
                            table_atributos.columns.header = ["Opción", "Atributo"]
                            for i, atributo in enumerate(lista_atributos):
                                table_atributos.append_row([i + 1, atributo])
                            print(table_atributos)
                        else:
                            print("Opción inválida. Por favor, elija una opción válida.")

                print("Tus credenciales no coinciden. Por favor, verifica tus datos.")
                break

                # Solicitar al usuario que ingrese el número del atributo a modificar
                opcion_atributo = input("Ingrese el número del atributo que desea modificar: ")
        
                if opcion_atributo == "1":
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")

                    # Actualizar el atributo en la tabla Trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"UPDATE Trabajador SET nombre_trabajador = '{nuevo_nombre}' WHERE id_trabajador = {pk_trabajador}")
                    conexion.connection.commit()
                    cursor.close()

                    print("El atributo 'nombre' ha sido modificado exitosamente.")

                elif opcion_atributo == "2":
                    nueva_direccion = input("Ingrese la nueva dirección: ")

                    # Actualizar el atributo en la tabla Trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"UPDATE Trabajador SET direccion = '{nueva_direccion}' WHERE id_trabajador = {pk_trabajador}")
                    conexion.connection.commit()
                    cursor.close()

                    print("El atributo 'dirección' ha sido modificado exitosamente.")

                elif opcion_atributo == "3":
                    nuevo_telefono = input("Ingrese el nuevo teléfono: ")

                    # Actualizar el atributo en la tabla Trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"UPDATE Trabajador SET telefono = '{nuevo_telefono}' WHERE id_trabajador = {pk_trabajador}")
                    conexion.connection.commit()
                    cursor.close()

                    print("El atributo 'teléfono' ha sido modificado exitosamente.")

                elif opcion_atributo == "4":
                    nuevo_nombre_contacto = input("Ingrese el nuevo nombre de contacto: ")

                    # Verificar si existe un registro en la tabla CONTACTODEEMERGENCIA para el trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"SELECT id_contacto_emergencia FROM CONTACTODEEMERGENCIA WHERE id_trabajador_fk = {pk_trabajador}")
                    resultado_contacto = cursor.fetchone()
                    cursor.close()

                    if resultado_contacto is not None:
                        id_contacto_emergencia = resultado_contacto[0]

                        # Actualizar el atributo en la tabla CONTACTODEEMERGENCIA
                        cursor = conexion.connection.cursor()
                        cursor.execute(f"UPDATE CONTACTODEEMERGENCIA SET nombre_contacto = '{nuevo_nombre_contacto}' WHERE id_contacto_emergencia = {id_contacto_emergencia}")
                        conexion.connection.commit()
                        cursor.close()

                        print("El atributo 'nombre de contacto' ha sido modificado exitosamente.")
                    else:
                        print("El trabajador no tiene datos de contacto de emergencia.")

                elif opcion_atributo == "5":
                    nuevo_telefono_contacto = input("Ingrese el nuevo teléfono de contacto: ")

                    # Verificar si existe un registro en la tabla CONTACTODEEMERGENCIA para el trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"SELECT id_contacto_emergencia FROM CONTACTODEEMERGENCIA WHERE id_trabajador_fk = {pk_trabajador}")
                    resultado_contacto = cursor.fetchone()
                    cursor.close()

                    if resultado_contacto is not None:
                        id_contacto_emergencia = resultado_contacto[0]

                        # Actualizar el atributo en la tabla CONTACTODEEMERGENCIA
                        cursor = conexion.connection.cursor()
                        cursor.execute(f"UPDATE CONTACTODEEMERGENCIA SET telefono_contacto = '{nuevo_telefono_contacto}' WHERE id_contacto_emergencia = {id_contacto_emergencia}")
                        conexion.connection.commit()
                        cursor.close()

                        print("El atributo 'teléfono de contacto' ha sido modificado exitosamente.")
                    else:
                        print("El trabajador no tiene datos de contacto de emergencia.")

                elif opcion_atributo == "6":
                    nuevo_nombre_carga = input("Ingrese el nuevo nombre de la carga: ")

                    # Verificar si existe una carga familiar con el mismo PK de trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"SELECT * FROM CARGASFAMILIARES WHERE id_trabajador_fk = {pk_trabajador}")
                    resultado_carga_familiar = cursor.fetchone()
                    cursor.close()

                    if resultado_carga_familiar is not None:
                        # Actualizar el atributo en la tabla CARGASFAMILIARES
                        cursor = conexion.connection.cursor()
                        cursor.execute(f"UPDATE CARGASFAMILIARES SET nombre_carga = '{nuevo_nombre_carga}' WHERE id_trabajador_fk = {pk_trabajador}")
                        conexion.connection.commit()
                        cursor.close()

                        print("El atributo 'nombre_carga' ha sido modificado exitosamente.")
                    else:
                        print("No se encontró ninguna carga familiar para el trabajador.")

                elif opcion_atributo == "7":
                    nuevo_parentesco = input("Ingrese el nuevo parentesco: ")

                    # Verificar si existe una carga familiar con el mismo PK de trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"SELECT * FROM CARGASFAMILIARES WHERE id_trabajador_fk = {pk_trabajador}")
                    resultado_carga_familiar = cursor.fetchone()
                    cursor.close()

                    if resultado_carga_familiar is not None:
                        # Actualizar el atributo en la tabla CARGASFAMILIARES
                        cursor = conexion.connection.cursor()
                        cursor.execute(f"UPDATE CARGASFAMILIARES SET parentesco = '{nuevo_parentesco}' WHERE id_trabajador_fk = {pk_trabajador}")
                        conexion.connection.commit()
                        cursor.close()

                        print("El atributo 'parentesco' ha sido modificado exitosamente.")
                    else:
                        print("No se encontró ninguna carga familiar para el trabajador.")

                elif opcion_atributo == "8":
                    nuevo_rut_carga = input("Ingrese el nuevo RUT de la carga: ")

                    # Verificar si existe una carga familiar con el mismo PK de trabajador
                    cursor = conexion.connection.cursor()
                    cursor.execute(f"SELECT * FROM CARGASFAMILIARES WHERE id_trabajador_fk = {pk_trabajador}")
                    resultado_carga_familiar = cursor.fetchone()
                    cursor.close()

                    if resultado_carga_familiar is not None:
                        # Actualizar el atributo en la tabla CARGASFAMILIARES
                        cursor = conexion.connection.cursor()
                        cursor.execute(f"UPDATE CARGASFAMILIARES SET rut_carga = '{nuevo_rut_carga}' WHERE id_trabajador_fk = {pk_trabajador}")
                        conexion.connection.commit()
                        cursor.close()

                        print("El atributo 'rut_carga' ha sido modificado exitosamente.")
                    else:
                        print("No se encontró ninguna carga familiar para el trabajador.")

                elif opcion_atributo == "0":
                    print("No se realizaron modificaciones.")
                    break
                else:
                    print("Opción inválida. Por favor, elija una opción válida.")

            elif opcion_edicion == "0":
                print("No se realizaron modificaciones.")
            else:
                print("Opción inválida. Por favor, elija una opción válida.")

# Cerrar la conexión
conexion.connection.close()