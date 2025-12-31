
import mysql.connector
def eliminar_profesor_db(id):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        sql = "DELETE FROM usuario WHERE ID_Usuario = %s AND rol = 'Profesor'"
        cursor.execute(sql, (id,))
        conexion.commit()

        return True

    except mysql.connector.Error as err:
        print("ERROR MYSQL:", err)
        return False

    finally:
        if cursor:
            cursor.close()
        if conexion:
            conexion.close()