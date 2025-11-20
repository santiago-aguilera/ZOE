import mysql.connector

def agregar_profesor(nombre, materia, correo, rol='Profesor'):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()
        sql = "INSERT INTO usuario (nombre, materia, email, rol) VALUES (%s, %s, %s, %s)"
        valores = (nombre, materia, correo, 'Profesor')
        cursor.execute(sql, valores)
        conexion.commit()
        return True
    except mysql.connector.Error as err:
        print("Error al insertar:", err)
        return False
    finally:
        cursor.close()
        conexion.close()
