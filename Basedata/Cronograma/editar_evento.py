import mysql.connector

def actualizar_evento(id_evento, id_materia, titulo, descripcion, fecha, hora, tipo, lugar):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE cronograma
        SET Id_Materia = %s,
            Titulo = %s,
            Descripcion = %s,
            Fecha = %s,
            Hora = %s,
            Tipo = %s,
            Lugar = %s
        WHERE Id_Cronograma = %s
    """, (id_materia, titulo, descripcion, fecha, hora, tipo, lugar, id_evento))

    conexion.commit()
    cursor.close()
    conexion.close()
def eliminar_evento(id_evento):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM cronograma WHERE Id_Cronograma = %s", (id_evento,))
    conexion.commit()

    cursor.close()
    conexion.close()
