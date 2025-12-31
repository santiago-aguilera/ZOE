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

def actualizar_profesor(id_usuario, nombre, correo, materias, telefono):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        # 1. Actualizar datos del profesor
        sql = """
        UPDATE Usuario
        SET Nombre = %s,
            Email = %s,
            Telefono = %s
        WHERE ID_Usuario = %s
        """
        cursor.execute(sql, (nombre, correo, telefono, id_usuario))

        # 2. Eliminar materias anteriores
        cursor.execute("DELETE FROM Profesor_Materia WHERE Id_Usuario = %s", (id_usuario,))

        # 3. Insertar nuevas materias
        sql_pm = """
        INSERT INTO Profesor_Materia (Id_Usuario, Id_Materia, Ano_Academico)
        VALUES (%s, %s, 2025)
        """
        for id_materia in materias:
            cursor.execute(sql_pm, (id_usuario, id_materia))

        conexion.commit()
        return True

    except mysql.connector.Error as err:
        print("ERROR MYSQL UPDATE:", err)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_materias_profesor2(id_usuario):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    sql = """
    SELECT Id_Materia 
    FROM Profesor_Materia 
    WHERE Id_Usuario = %s
    """
    cursor.execute(sql, (id_usuario,))
    materias = cursor.fetchall()

    cursor.close()
    conexion.close()

    # Convertir [{'Id_Materia': 1}, {'Id_Materia': 3}] → [1, 3]
    return [m['Id_Materia'] for m in materias]
