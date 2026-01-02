#import lybraries
import os
from flask import Flask, render_template, request,redirect, session,url_for,flash

from Basedata.Gestion.realizadas import obtener_entregas_estudiante
from Controlador.controlador_login import validar_login
from Basedata.Datos_Profes.data  import conectar_db as cb
from Basedata.Datos_Profes.new  import agregar_profesor as cp
from Basedata.Datos_Profes.eliminar  import eliminar_profesor_db
from Basedata.Datos_Profes.editar  import actualizar_profesor, obtener_profesor_por_id, obtener_materias_profesor2
from Basedata.Datos_Profes.Cards import obtener_profesores
from Basedata.Gestion.Crear_trabajo import crear_trabajo, obtener_materias_profesor
from Basedata.Materias.obtener_materias import obtener_materias
from Basedata.Gestion.Obtener_materias_tareas import obtener_materias_con_tareas
from Basedata.Gestion.Obtener_tareas import obtener_tareas
from Basedata.Gestion.realizadas import obtener_entregas_estudiante
from Basedata.Gestion.subir_archvio import guardar_entrega
from Basedata.Grados.Grados import obtener_grupos, crear_grupo, obtener_estudiantes, obtener_estudiantes_asignados, asignar_estudiante
from Basedata.Estudiantes.crear_estudiantes import crear_estudiante, obtener_estudiante_por_id
from Basedata.Estudiantes.eliminar import eliminar_estudiante_db
from Basedata.Estudiantes.acualizar import actualizar_estudiante
from Basedata.Estudiantes.obtener_estudaintes import obtener_estudiantes_cards

#llamar librerias y clases

#instanciar: Dentro de mi paquete tengogo muchos aetes adicionales y unire la apicacion con todos los paquetes 
app=Flask(__name__)
app.secret_key = "clave-super-secreta-zoe"
#Para enviar correos
from flask_mail import Mail, Message

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'TU_CORREO@gmail.com'
app.config['MAIL_PASSWORD'] = 'TU_CONTRASEÑA_DE_APLICACIÓN'
app.config['MAIL_DEFAULT_SENDER'] = 'TU_CORREO@gmail.com'

mail = Mail(app)

#Inicip de rutas
@app.route('/')

#La siguiente ruta es temporal para los usuarios 
#@app.before_request
#def usuario_temporal():
    # SOLO PARA DESARROLLO
#    if 'id_usuario' not in session:
#        session['id_usuario'] = 1  # ID de un profesor de prueba
#    return render_template('Pages/main.html')


@app.route('/home')
#function call archive
def dir1():
    return render_template('Pages/Home.html')

@app.route('/main')
def main():
    return render_template('pages/Main.html')

#route gestion
@app.route('/gestion')
def gestion():
    return render_template('pages/Gestion.html')

@app.route('/tareas')
def tareas():
    tareas = obtener_tareas()
    return render_template('dash/gestion/das_1_g.html', tareas=tareas)

@app.route('/subir_tarea/<int:id_trabajo>')
def subir_tarea(id_trabajo):
    return render_template('dash/gestion/das_4_g.html', id_trabajo=id_trabajo)

@app.route('/enviar_tarea/<int:id_trabajo>', methods=['POST']) 
def enviar_tarea(id_trabajo): 
    archivo = request.files['archivo'] 
    # Carpeta donde guardarás los archivos 
    ruta = "uploads" 
    if not os.path.exists(ruta): 
        os.makedirs(ruta) 
    archivo_path = os.path.join(ruta, archivo.filename) 
    archivo.save(archivo_path) 
    # Estudiante simulado 
    id_estudiante = 1 
    # Guardar en la BD usando la función SQL 
    guardar_entrega(id_trabajo, id_estudiante, archivo.filename) 
    flash("Tarea enviada correctamente.") 
    return redirect(url_for('realizado'))

@app.route('/realizado')
def realizado():
    id_estudiante = 1  # estudiante simulado
    entregas = obtener_entregas_estudiante(id_estudiante)
    return render_template('dash/gestion/das_2_g.html', entregas=entregas)




@app.route('/crear_tareas')
def crear_tareas():
    id_usuario = 19 #session ['id_usuario']  
    materias = obtener_materias_con_tareas(id_usuario)
    return render_template('dash/gestion/das_3_g.html', materias=materias)

@app.route('/nueva_tarea') 
def nueva_tarea(): 
    id_usuario = 19 #session['id_usuario'] 
    materias = obtener_materias_profesor(id_usuario) 
    return render_template('dash/gestion/frm_tareas.html', materias=materias)

@app.route('/crear-tarea', methods=['POST']) 
def crear_tarea(): 
    titulo = request.form['descripcion'][:50] # o puedes agregar un campo "titulo" 
    descripcion = request.form['descripcion'] 
    fecha = request.form['fecha'] 
    id_profesor_materia = request.form['id_profesor_materia'] 
    crear_trabajo(titulo, descripcion, fecha, id_profesor_materia) 
    flash("Tarea creada correctamente.") 
    return redirect(url_for('crear_tareas'))



@app.route('/guias')
def guias():
    return render_template('pages/Guias.html')

@app.route('/cronograma')
def cronograma():
    return render_template('pages/Cronograma.html')

@app.route('/eventos')
def eventos():
    return render_template('dash/cronograma/frm_evento.html')

@app.route('/usuarios')
def usuarios():
    return render_template('pages/Usuarios.html')

@app.route('/profesores') 
def profesores(): 
    profesores = obtener_profesores() 
    return render_template('pages/Profesores.html', profesores=profesores)

@app.route('/enviar_mensaje', methods=['POST'])
def enviar_mensaje():
    nombre = request.form['nombre']
    correo = request.form['correo']
    asunto = request.form['asunto']
    mensaje = request.form['mensaje']

    try:
        msg = Message(asunto, recipients=[correo])
        msg.body = f"Mensaje enviado desde ZOE Docs:\n\n{mensaje}"
        mail.send(msg)

        flash("Mensaje enviado correctamente.")
    except Exception as e:
        print("ERROR AL ENVIAR:", e)
        flash("No se pudo enviar el mensaje.")

    return redirect(url_for('profesores'))


@app.route('/ver_profesores')
def ver_profesores():
    dato=cb()
    #return render_template('dash/Profesores/dash_ver_profes.html',materia=dato)
    return render_template('dash/Profesores/dash_ver_profes.html',usuario=dato)

@app.route('/crear_profesores', methods=['GET', 'POST'])
def agregar_profesores():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']
        materias = request.form.getlist('materias')  # ← AHORA ES LISTA 

        contraseña = cp(nombre, correo, telefono, materias)

        if contraseña:
            flash("Profesor agregado correctamente. Contraseña: " + contraseña)
        else:
            flash("Error al agregar profesor.")

        return redirect(url_for('ver_profesores'))

    # GET → cargar materias para el formulario
    materias = obtener_materias()
    return render_template('dash/Profesores/frm_profes.html', materias=materias)


@app.route('/eliminar_profesor/<int:id>')
def eliminar_profesor(id):
    if eliminar_profesor_db(id):
        flash("Profesor eliminado correctamente.")
    else:
        flash("Error al eliminar profesor.")

    return redirect(url_for('ver_profesores'))


@app.route('/editar_profesor/<int:id>', methods=['GET', 'POST'])
def editar_profesor(id):

    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        materias = request.form.getlist('materia')
        telefono = request.form['telefono']


        if actualizar_profesor(id, nombre, correo,materias, telefono):
            flash("Profesor actualizado correctamente.")
            print("ACTUALIZADO")

        else:
            flash("No se realizaron cambios.")

        return redirect(url_for('ver_profesores'))

    # GET → cargar datos
    profesor = obtener_profesor_por_id(id)
    materia = obtener_materias()
    materias_asignadas = obtener_materias_profesor2(id)

    print("MATERIAS:", materia) 
    print("ASIGNADAS:", materias_asignadas)

    return render_template(
        'dash/Profesores/editar_profeS.html',
        profesor=profesor
        ,materias=materia
        ,materias_asignadas=materias_asignadas
    )


@app.route('/estudiantes')
def estudiantes():
    estudiantes = obtener_estudiantes_cards()
    return render_template('pages/Estudiantes.html', estudiantes=estudiantes)

@app.route('/ver_estudiantes')
def ver_estudiantes():
    estudiantes = obtener_estudiantes_cards()
    return render_template('dash/Estudiantes/das_ver_estudiantes.html', estudiantes=estudiantes)

@app.route('/crear_estudiantes', methods=['GET', 'POST'])
def crear_estudiantes():
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']

        contraseña = crear_estudiante(nombre, correo, telefono)

        if contraseña:
            flash("Estudiante agregado correctamente. Contraseña: " + contraseña)
        else:
            flash("Error al agregar estudiante.")

        return redirect(url_for('ver_estudiantes'))

    return render_template('dash/Estudiantes/frm_estudiantes.html')

@app.route('/editar_estudiante/<int:id>', methods=['GET', 'POST'])
def editar_estudiante(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        correo = request.form['correo']
        telefono = request.form['telefono']

        if actualizar_estudiante(id, nombre, correo, telefono):
            flash("Estudiante actualizado correctamente.")
        else:
            flash("No se realizaron cambios.")

        return redirect(url_for('ver_estudiantes'))

    estudiante = obtener_estudiante_por_id(id)
    return render_template('dash/Estudiantes/editar_estudiantes.html', estudiante=estudiante)

@app.route('/eliminar_estudiante/<int:id>')
def eliminar_estudiante(id):
    if eliminar_estudiante_db(id):
        flash("Estudiante eliminado correctamente.")
    else:
        flash("Error al eliminar estudiante.")

    return redirect(url_for('ver_estudiantes'))




@app.route('/estadisticas')
def estadisticas():
    return render_template('pages/Estadisiticas.html')

@app.route('/foros')
def foros():
    return render_template('pages/Foros.html')

@app.route('/ver_foros')
def ver_foros():
    return render_template('dash/Foros/dash_foros.html')

@app.route('/crear_foros')
def crear_foros():
    return render_template('dash/Foros/frm_foros.html')


@app.route('/grupos')
def grupos():
    grupos = obtener_grupos()
    return render_template('dash/grupos/lista.html', grupos=grupos)


@app.route('/grupos/crear', methods=['GET', 'POST'])
def crear_grupo_route():
    if request.method == 'POST':
        nombre = request.form['nombre']
        crear_grupo(nombre)
        return redirect('/grupos')

    return render_template('dash/grupos/crear.html')


@app.route('/grupos/<int:id_grupo>/asignar', methods=['GET', 'POST'])
def asignar_estudiantes_route(id_grupo):

    if request.method == 'POST':
        id_usuario = request.form['id_usuario']
        print("ID RECIBIDO:", id_usuario) # ← AGREGA ESTO
        asignar_estudiante(id_usuario, id_grupo)

    estudiantes = obtener_estudiantes()
    print("ESTUDIANTES:", estudiantes)
    asignados = obtener_estudiantes_asignados(id_grupo)

    return render_template(
        'dash/grupos/asignar.html',
        estudiantes=estudiantes,
        asignados=asignados,
        id_grupo=id_grupo
    )



@app.route('/proyectos')
def proy():
    return render_template('pages/proyectos.html')

@app.route('/informacion')
def information():
    return render_template('dash/coordinador/Informacion.html')

#Call routes
@app.route('/login')
def dash():
    return render_template('login/frm_1.html',fallo={})

@app.route('/validar', methods=['POST'])
def login():
    usuuario = request.form.get('usuario')
    password = request.form.get('password')
    resul_validar=validar_login(usuuario,password)
    if resul_validar['success']:
        return render_template('pages/Main.html')
    else:
        error=resul_validar['error']
        return render_template('pages/Login.html',fallo=error)


# Eject app
if __name__ == ('__main__'):
    app.run(debug=True)
