import mysql.connector

def eliminar_estudiante_de_grupo(id_usuario, id_grupo):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        cursor.execute("""
            DELETE FROM Usuario_Grupo
            WHERE Id_Usuario = %s AND Id_Grupo = %s
        """, (id_usuario, id_grupo))

        conexion.commit()
        return True

    except mysql.connector.Error as err:
        print("Error al eliminar estudiante del grupo:", err)
        return False

    finally:
        cursor.close()
        conexion.close()
