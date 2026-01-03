import mysql.connector

def obtener_estudiantes_cards():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("""
            SELECT 
                e.ID_Usuario,
                e.Nombre,
                e.Email,
                e.Telefono,
                g.Nombre as Grupo
            FROM Usuario e
            LEFT JOIN Usuario_Grupo ug ON ug.Id_Usuario = e.ID_Usuario
            LEFT JOIN Grupo g ON g.Id_Grupo = ug.Id_Grupo
            WHERE e.Rol = 'Estudiante'
        """)

        estudiantes = cursor.fetchall()
        return estudiantes

    except mysql.connector.Error as err:
        print("Error al obtener estudiantes (cards):", err)
        return []

    finally:
        cursor.close()
        conexion.close()
