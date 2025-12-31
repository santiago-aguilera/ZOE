import mysql.connector

def crear_trabajo(titulo, descripcion, fecha_entrega, id_profesor_materia):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor()

    sql = """
    INSERT INTO Trabajo (Titulo, Descripcion, Fecha_Entrega, Id_Profesor_Materia)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (titulo, descripcion, fecha_entrega, id_profesor_materia))
    conexion.commit()

    cursor.close()
    conexion.close()


def obtener_materias_profesor(id_usuario):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    sql = """
    SELECT pm.Id_Profesor_Materia, nombre_materia
    FROM Profesor_Materia pm
    JOIN Materia m ON pm.Id_Materia = m.Id_Materia
    WHERE pm.Id_Usuario = %s
    """

    cursor.execute(sql, (id_usuario,))
    materias = cursor.fetchall()

    cursor.close()
    conexion.close()
    return materias
