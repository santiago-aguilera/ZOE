import mysql.connector

def conectar_db(nombre, correo):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        sql = "INSERT INTO usuario (nombre, email) VALUES (%s, %s, %s, %s)"
        valores = (nombre, correo)
        cursor.execute(sql, valores)
        conexion.commit()

        print("Profesor agregado correctamente.")
        return True
    except mysql.connector.Error as err:
        print("Error al insertar:", err)
        return False
    finally:
        cursor.close()
        conexion.close()
