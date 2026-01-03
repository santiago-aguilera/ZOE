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

def obtener_tareas_por_grupo(id_grupo):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT t.*
        FROM trabajo t
        JOIN trabajo_grupo tg ON tg.Id_Trabajo = t.Id_Trabajo
        WHERE tg.Id_Grupo = %s
    """, (id_grupo,))

    tareas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return tareas

def obtener_grupos_usuario(id_usuario):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT g.Id_Grupo, g.Nombre
        FROM usuario_grupo ug
        JOIN grupo g ON g.Id_Grupo = ug.Id_Grupo
        WHERE ug.Id_Usuario = %s
    """, (id_usuario,))

    grupos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return grupos


def obtener_todos_los_grupos():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM grupo")
    grupos = cursor.fetchall()

    cursor.close()
    conexion.close()
    return grupos
