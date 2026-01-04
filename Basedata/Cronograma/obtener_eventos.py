import mysql.connector

def obtener_eventos_cronograma():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT c.*, m.nombre_materia
        FROM cronograma c
        JOIN materia m ON m.Id_Materia = c.Id_Materia
        ORDER BY c.Fecha, c.Hora
    """)

    eventos = cursor.fetchall()
    cursor.close()
    conexion.close()
    return eventos

def obtener_evento(id_evento):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT c.*, m.nombre_materia
        FROM cronograma c
        JOIN materia m ON m.Id_Materia = c.Id_Materia
        WHERE c.Id_Cronograma = %s
    """, (id_evento,))

    evento = cursor.fetchone()

    cursor.close()
    conexion.close()
    return evento