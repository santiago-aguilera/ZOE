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
