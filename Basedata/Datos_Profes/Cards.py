import  mysql.connector

def obtener_materias_profesor(id_usuario):
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    sql = """
    SELECT pm.Id_Profesor_Materia, nombre_materia
    FROM Profesor_Materia pm
    JOIN Materia m ON pm.Id_Materia = m.Id_Materia
    WHERE pm.Id_Usuario = %s
    """

    cursor.execute(sql, (id_usuario,))
    materias = cursor.fetchall()

    cursor.close()
    conexion.close()
    return ", ".join([m['nombre_materia'] for m in materias])

def obtener_profesores():
    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT ID_Usuario, Nombre, Email FROM usuario WHERE Rol = 'Profesor'")
    profesores = cursor.fetchall()

    resultado = []

    for p in profesores:
        materias = obtener_materias_profesor(p['ID_Usuario'])
        resultado.append({
            "ID_Usuario": p['ID_Usuario'],
            "Nombre": p['Nombre'],
            "Email": p['Email'],
            "Materia": materias
        })

    cursor.close()
    conexion.close()
    return resultado
