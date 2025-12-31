import mysql.connector
def obtener_materias_con_tareas(id_usuario):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    # 1. Obtener materias del profesor
    cursor.execute("""
        SELECT pm.Id_Profesor_Materia, m.nombre_materia
        FROM Profesor_Materia pm
        JOIN Materia m ON pm.Id_Materia = m.Id_Materia
        WHERE pm.Id_Usuario = %s
    """, (id_usuario,))
    materias = cursor.fetchall()

    resultado = []

    for materia in materias:
        id_pm = materia['Id_Profesor_Materia']

        # 2. Obtener tareas de esa materia
        cursor.execute("""
            SELECT Id_Trabajo AS id, Titulo AS titulo, Fecha_Entrega AS fecha
            FROM Trabajo
            WHERE Id_Profesor_Materia = %s
        """, (id_pm,))
        tareas = cursor.fetchall()

        resultado.append({
            "Id_Profesor_Materia": id_pm,
            "nombre_materia": materia['nombre_materia'],
            "tareas": tareas
        })

    cursor.close()
    conexion.close()
    return resultado
