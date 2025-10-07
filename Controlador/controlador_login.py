def validar_login(usuario, password):
    usuarios_validos = {'admin': 'adm123', 'contra': 'pass123'}
    error = {}

    # Validación de campos vacíos
    if usuario == "":
        error['usuario'] = "El campo usuario es obligatorio"
    if password == "":
        error['password'] = "El campo password es obligatorio"

    # Si hay errores, no se valida el login
    if error:
        return {'success': False, 'errores': error}

   
   #2 validar que las dos cajas tengan usuarios y esten correctos
    if usuario in usuarios_validos and usuarios_validos[usuario] == password:
      return {'success':True}
    else:
      error["password_1"]="Usuario o contraseña incorrectos"
      return{'success':False, 'errores':error}
   
   # Si las credenciales no coinciden
    return {'success': False, 'errores': {'general': 'Usuario o contraseña incorrectos'}}