import mysql.connector

def obtener_profesor_por_id(id):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor(dictionary=True)

        sql = "SELECT * FROM usuario WHERE ID_Usuario = %s"
        cursor.execute(sql, (id,))
        profesor = cursor.fetchone()

        return profesor

    except mysql.connector.Error as err:
        print("ERROR MYSQL:", err)
        return None

    finally:
        cursor.close()
        conexion.close()

def actualizar_profesor(id_usuario, nombre, correo, materia, telefono):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        sql = """
        UPDATE usuario
        SET Nombre = %s,
            Email = %s,
            Materia = %s,
            Telefono = %s
        WHERE ID_Usuario = %s
        """

        valores = (nombre, correo, materia, telefono, id_usuario)
        cursor.execute(sql, valores)
        conexion.commit()

        return cursor.rowcount > 0  # ← clave

    except mysql.connector.Error as err:
        print("ERROR MYSQL UPDATE:", err)
        return False

    finally:
        cursor.close()
        conexion.close()