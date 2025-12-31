import mysql.connector

def obtener_entregas_estudiante(id_estudiante):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("""
        SELECT 
            e.Id_Entrega,
            e.Id_Trabajo,
            e.Archivo,
            e.Fecha_Entrega,
            e.Estado,
            e.Calificacion,
            e.Comentarios,
            t.Titulo AS titulo,
            t.Descripcion AS descripcion
        FROM Entrega e
        JOIN Trabajo t ON e.Id_Trabajo = t.Id_Trabajo
        WHERE e.Id_Usuario = %s
        ORDER BY e.Id_Entrega DESC
    """, (id_estudiante,))

    entregas = cursor.fetchall()

    cursor.close()
    conexion.close()

    return entregas
