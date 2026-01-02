import mysql.connector, random, string, bcrypt

def generar_contraseña():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

def encriptar_contraseña(contraseña):
    return bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def crear_estudiante(nombre, correo, telefono):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()

        # 1. Generar contraseña aleatoria
        contraseña_plana = generar_contraseña()

        # 2. Encriptarla
        contrasena_hash = encriptar_contraseña(contraseña_plana)

        # 3. Insertar estudiante
        sql = """ 
        INSERT INTO Usuario (Nombre, email, Contraseña, Rol, Telefono) 
        VALUES (%s, %s, %s, %s, %s) 
        """
        valores = (nombre, correo, contrasena_hash, "Estudiante", telefono)
        cursor.execute(sql, valores)
        conexion.commit()

        return contraseña_plana

    except mysql.connector.Error as err:
        print("Error al insertar:", err)
        return False

    finally:
        cursor.close()
        conexion.close()

def obtener_estudiante_por_id(id_estudiante):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor(dictionary=True)

        cursor.execute("SELECT * FROM Usuario WHERE Id_Usuario = %s AND Rol = 'Estudiante'", (id_estudiante,))
        estudiante = cursor.fetchone()

        return estudiante

    except mysql.connector.Error as err:
        print("Error al obtener estudiante:", err)
        return None

    finally:
        cursor.close()
        conexion.close()
