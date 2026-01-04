import mysql.connector

def obtener_estadisticas(id_usuario):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    with conexion.cursor() as cursor:

        # TOTAL DE TAREAS ASIGNADAS AL ESTUDIANTE
        cursor.execute("""
            SELECT COUNT(*)
            FROM trabajo t
            JOIN trabajo_grupo tg ON tg.Id_Trabajo = t.Id_Trabajo
            JOIN usuario_grupo ug ON ug.Id_Grupo = tg.Id_Grupo
            WHERE ug.Id_Usuario = %s
        """, (id_usuario,))
        total = cursor.fetchone()[0]

        # TAREAS ENTREGADAS (estado = 'entregado')
        cursor.execute("""
            SELECT COUNT(*)
            FROM entrega e
            WHERE e.Id_Usuario = %s AND e.Estado = 'entregado'
        """, (id_usuario,))
        completadas = cursor.fetchone()[0]

        pendientes = total - completadas

    conexion.close()

    return {
        "total": total,
        "completadas": completadas,
        "pendientes": pendientes
    }