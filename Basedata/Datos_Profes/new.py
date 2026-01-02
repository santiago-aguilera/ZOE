import mysql.connector, random, string, bcrypt

def generar_contraseña():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

def encriptar_contraseña(contraseña):
    return bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def agregar_profesor(nombre, correo, telefono, materias, rol='Profesor'):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="zoe"
        )
        cursor = conexion.cursor()
        print("Intentando insertar:", nombre, correo)

        # 1. Generar contraseña aleatoria
        contrasena_plana = generar_contraseña()

        # 2. Encriptarla
        contrasena_hash = encriptar_contraseña(contrasena_plana)

        # 3. Insertar profesor en Usuario
        sql = """ 
        INSERT INTO Usuario (Nombre, email, Contraseña, Rol, Telefono) 
        VALUES (%s, %s, %s, %s, %s) 
        """

        valores = (nombre, correo, contrasena_hash, rol, telefono)

        print("contraseña generada:", contrasena_plana)
        cursor.execute(sql, valores)
        conexion.commit()

        # Obtener el ID del profesor recién creado
        id_profesor = cursor.lastrowid

        # 4. Insertar materias en Profesor_Materia
        sql_pm = """
        INSERT INTO Profesor_Materia (Id_Usuario, Id_Materia, Ano_Academico)
        VALUES (%s, %s, 2025)
        """

        for id_materia in materias:
            cursor.execute(sql_pm, (id_profesor, id_materia))

        conexion.commit()

        # 5. Retornar la contraseña generada para mostrarla al admin
        return contrasena_plana

    except mysql.connector.Error as err:
        print("Error al insertar:", err)
        return False

    finally:
        cursor.close()
        conexion.close()

