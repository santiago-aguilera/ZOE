import mysql.connector

def agregar_profesor(nombre, correo, telefono, materias, rol='Profesor'):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()
        print("Intentando insertar:", nombre, correo)

        # 1. Insertar profesor en Usuario (igual que antes, pero sin Materia)
        sql = """ 
        INSERT INTO Usuario (Nombre, email, Contraseña, Rol, Telefono) 
        VALUES (%s, %s, %s, %s, %s) 
        """

        password_por_defecto = "123456"   # luego puedes cifrarla
        rol = "Profesor"

        valores = (nombre, correo, password_por_defecto, rol, telefono)

        cursor.execute(sql, valores)
        conexion.commit()

        # Obtener el ID del profesor recién creado
        id_profesor = cursor.lastrowid

        # Insertar materias en Profesor_Materia
        sql_pm = """
        INSERT INTO Profesor_Materia (Id_Usuario, Id_Materia, Ano_Academico)
        VALUES (%s, %s, 2025)
        """

        for id_materia in materias:
            cursor.execute(sql_pm, (id_profesor, id_materia))

        conexion.commit()

        return True

    except mysql.connector.Error as err:
        print("Error al insertar:", err)
        return False

    finally:
        cursor.close()
        conexion.close()
