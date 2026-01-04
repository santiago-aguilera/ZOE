import mysql.connector

def crear_evento_cronograma(id_materia, titulo, descripcion, fecha, hora, tipo, lugar):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO cronograma (Id_Materia, Titulo, Descripcion, Fecha, Hora, Tipo, Lugar)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (id_materia, titulo, descripcion, fecha, hora, tipo, lugar))

    conexion.commit()
    cursor.close()
    conexion.close()