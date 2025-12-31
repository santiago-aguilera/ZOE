import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoe"
    )

# -------------------------
# GRUPOS
# -------------------------

def obtener_grupos():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM grupo")
    grupos = cursor.fetchall()

    cursor.close()
    conexion.close()
    return grupos


def crear_grupo(nombre):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("INSERT INTO grupo (Nombre) VALUES (%s)", (nombre,))
    conexion.commit()

    cursor.close()
    conexion.close()


# -------------------------
# ESTUDIANTES EN GRUPOS
# -------------------------

def obtener_estudiantes():
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT * FROM usuario WHERE Rol = 'Estudiante'")
    estudiantes = cursor.fetchall()

    cursor.close()
    conexion.close()
    return estudiantes


def obtener_estudiantes_asignados(id_grupo):
    conexion = conectar()
    cursor = conexion.cursor(dictionary=True)

    cursor.execute("SELECT Id_Usuario FROM usuario_grupo WHERE Id_Grupo = %s", (id_grupo,))
    asignados = [row["Id_Usuario"] for row in cursor.fetchall()]

    cursor.close()
    conexion.close()
    return asignados


def asignar_estudiante(id_usuario, id_grupo):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO usuario_grupo (Id_Usuario, Id_Grupo)
        VALUES (%s, %s)
    """, (id_usuario, id_grupo))

    conexion.commit()
    cursor.close()
    conexion.close()
