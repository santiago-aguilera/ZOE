#import lybraries
from flask import Flask, render_template, request,redirect,url_for,flash
from Controlador.controlador_login import validar_login



from Basedata.Datos_Profes.data  import conectar_db as cb
from Basedata.Datos_Profes.new  import agregar_profesor as cp
from Basedata.Datos_Profes.eliminar  import eliminar_profesor_db
from Basedata.Datos_Profes.editar  import actualizar_profesor, obtener_profesor_por_id
#llamar librerias y clases
#instanciar: Dentro de mi paquete tengogo muchos aetes adicionales y unire la apicacion con todos los paquetes 
app=Flask(__name__)
app.secret_key = "clave-super-secreta-zoe"

#Inicip de rutas
@app.route('/')

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
    return render_template('dash/gestion/das_1_g.html')

@app.route('/realizado')
def realizado():
    return render_template('dash/gestion/das_2_g.html')

@app.route('/crear_tareas')
def crear_tareas():
    return render_template('dash/gestion/das_3_g.html')

@app.route('/nueva_tarea')
def nueva_tarea():
    return render_template('dash/gestion/frm_tareas.html')

@app.route('/guias')
def guias():
    return render_template('pages/Guias.html')

@app.route('/cronograma')
def cronograma():
    return render_template('pages/Cronograma.html')

@app.route('/eventos')
def eventos():
    return render_template('dash/cronograma/frm_evento.html')

@app.route('/profesores')
def profesores():
    return render_template('pages/Profesores.html')

@app.route('/ver_profesores')
def ver_profesores():
    dato=cb()
    #return render_template('dash/Profesores/dash_ver_profes.html',materia=dato)
    return render_template('dash/Profesores/dash_ver_profes.html',usuario=dato)

@app.route('/crear_profesores', methods=['GET', 'POST'])
def agregar_profesores():
    if request.method == 'POST':
        nombre = request.form['nombre']
        materia = request.form['materia']
        correo = request.form['correo']

        # Llamar a la función para insertar el profesor en la base de datos
        if cp(nombre,materia, correo):
            flash("Profesor agregado correctamente.")
        else:
            flash("Error al agregar profesor.")

        # Redirigir al mismo formulario después de  enviar los datos
        return redirect(url_for('ver_profesores'))

    # Si es un GET (cuando se accede al formulario por primera vez)
    #datos = cp()  # Esta es la función que probablemente obtenga los datos de los profesores
    return render_template('dash/Profesores/frm_profes.html')#, usuario=datos)

@app.route('/eliminar_profesor/<int:id>')
def eliminar_profesor(id):
    if eliminar_profesor_db(id):
        flash("Profesor eliminado correctamente.")
    else:
        flash("Error al eliminar profesor.")

    return redirect(url_for('ver_profesores'))

@app.route('/editar_profesor/<int:id>', methods=['GET', 'POST'])
def editar_profesor(id):
    profesor = obtener_profesor_por_id(id)

    if not profesor:
        flash("Profesor no encontrado")
        return redirect(url_for('ver_profesores'))

    if request.method == 'POST':
        nombre = request.form['nombre']
        materia = request.form['materia']
        correo = request.form['correo']
        telefono = request.form['telefono']

        actualizar_profesor(id, nombre, materia, correo, telefono)
        flash("Profesor actualizado correctamente")

        return redirect(url_for('ver_profesores'))

    return render_template(
        'dash/Profesores/editar_profes.html',
        profesor=profesor
    )

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
