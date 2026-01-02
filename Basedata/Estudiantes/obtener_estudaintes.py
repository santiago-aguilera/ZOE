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
                ID_Usuario,
                Nombre,
                Email,
                Telefono
            FROM Usuario
            WHERE Rol = 'Estudiante'
        """)

        estudiantes = cursor.fetchall()
        return estudiantes

    except mysql.connector.Error as err:
        print("Error al obtener estudiantes (cards):", err)
        return []

    finally:
        cursor.close()
        conexion.close()
