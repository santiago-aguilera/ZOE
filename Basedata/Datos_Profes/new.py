import mysql.connector

def agregar_profesor(nombre, materia, correo, rol='Profesor'):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()
        print("Intentando insertar:", nombre, correo)

        sql = """
        INSERT INTO usuario (Nombre,Email,Contraseña,Rol)
        VALUES (%s, %s, %s, %s)
        """

        password_por_defecto = "123456"   # luego puedes cifrarla
        rol = "Profesor"

        valores = (nombre, correo, password_por_defecto, rol)

        cursor.execute(sql, valores)
        conexion.commit()

        return True

    except mysql.connector.Error as err:
        print("Error al insertar:", err)
        return False

    finally:
        cursor.close()
        conexion.close()
