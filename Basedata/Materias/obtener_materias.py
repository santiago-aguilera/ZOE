import mysql.connector

def obtener_materias():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT Id_Materia, nombre_materia FROM Materia")
    materias = cursor.fetchall()

    cursor.close()
    conexion.close()
    return materias

def insertar_materia(nombre, descripcion):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO materia (nombre_materia, Descripcion) VALUES (%s, %s)", (nombre, descripcion))
    conexion.commit()

def obtener_materias():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    with conexion.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM materia")
        return cursor.fetchall()

def obtener_materia_por_id(id_materia):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    with conexion.cursor(dictionary=True) as cursor:
        cursor.execute("SELECT * FROM materia WHERE id_materia = %s", (id_materia,))
        return cursor.fetchone()

def actualizar_materia(id_materia, nombre, descripcion):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE materia SET nombre_materia = %s, Descripcion = %s WHERE id_materia = %s",
                       (nombre, descripcion, id_materia))
    conexion.commit()

def eliminar_materia_por_id(id_materia):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM materia WHERE id_materia = %s", (id_materia,))
    conexion.commit()