import mysql.connector

def guardar_entrega(id_trabajo, id_estudiante, archivo_nombre):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO Entrega (Id_Trabajo, Id_Usuario, Archivo, Estado)
        VALUES (%s, %s, %s, 'entregado')
    """, (id_trabajo, id_estudiante, archivo_nombre))

    conexion.commit()
    cursor.close()
    conexion.close()
