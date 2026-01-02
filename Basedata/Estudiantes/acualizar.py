import mysql.connector

def actualizar_estudiante(id_estudiante, nombre, correo, telefono):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        sql = """
        UPDATE Usuario 
        SET Nombre = %s, email = %s, Telefono = %s
        WHERE Id_Usuario = %s AND Rol = 'Estudiante'
        """

        valores = (nombre, correo, telefono, id_estudiante)

        cursor.execute(sql, valores)
        conexion.commit()

        return cursor.rowcount > 0

    except mysql.connector.Error as err:
        print("Error al actualizar estudiante:", err)
        return False

    finally:
        cursor.close()
        conexion.close()
