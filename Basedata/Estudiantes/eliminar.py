import mysql.connector

def eliminar_estudiante_db(id_estudiante):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        sql = "DELETE FROM Usuario WHERE Id_Usuario = %s AND Rol = 'Estudiante'"
        cursor.execute(sql, (id_estudiante,))
        conexion.commit()

        return cursor.rowcount > 0

    except mysql.connector.Error as err:
        print("Error al eliminar estudiante:", err)
        return False

    finally:
        cursor.close()
        conexion.close()
