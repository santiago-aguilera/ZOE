#import lybraries
from flask import Flask, render_template, request,redirect,url_for
from Controlador.controlador_login import validar_login
#llamar librerias y clases
#instanciar: Dentro de mi paquete tengogo muchos aetes adicionales y unire la apicacion con todos los paquetes 
app=Flask(__name__)


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
    return render_template('dash/Profesores/dash_ver_profes.html')

@app.route('/crear_profesores')
def crear_profesores():
    return render_template('dash/Profesores/frm_profes.html')

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
