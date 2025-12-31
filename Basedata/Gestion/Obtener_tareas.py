import mysql.connector

def obtener_tareas():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            t.Id_Trabajo AS id,
            t.Titulo AS titulo,
            t.Descripcion AS descripcion,
            t.Fecha_Entrega AS fecha
        FROM Trabajo t
        ORDER BY t.Id_Trabajo DESC
    """)

    tareas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return tareas
