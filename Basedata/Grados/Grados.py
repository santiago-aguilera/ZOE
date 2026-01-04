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
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        # Verificar si el estudiante ya pertenece a algún grupo
        cursor.execute("""
            SELECT 1 FROM Usuario_Grupo 
            WHERE Id_Usuario = %s
        """, (id_usuario,))

        if cursor.fetchone():
            print("⚠ El estudiante ya pertenece a un grupo.")
            return False

        # Insertar si no pertenece a ningún grupo
        cursor.execute("""
            INSERT INTO Usuario_Grupo (Id_Usuario, Id_Grupo)
            VALUES (%s, %s)
        """, (id_usuario, id_grupo))

        conexion.commit()
        return True

    except mysql.connector.Error as err:
        print("Error al asignar estudiante:", err)
        return False

    finally:
        cursor.close()
        conexion.close()


def obtener_estudiantes_asignados_global():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        cursor.execute("SELECT Id_Usuario FROM Usuario_Grupo")
        asignados = [fila[0] for fila in cursor.fetchall()]

        return asignados

    except mysql.connector.Error as err:
        print("Error al obtener asignados global:", err)
        return []

    finally:
        cursor.close()
        conexion.close()

def asignar_trabajo_a_grupo(id_trabajo, id_grupo):
    conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO trabajo_grupo (Id_Trabajo, Id_Grupo)
        VALUES (%s, %s)
    """, (id_trabajo, id_grupo))

    conexion.commit()
    cursor.close()
    conexion.close()
