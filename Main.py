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

@app.route('/guias')
def proyectos():
    return render_template('pages/Proyectos.html')

@app.route('/cronograma')
def cronograma():
    return render_template('pages/Cronograma.html')

@app.route('/profesores')
def profesores():
    return render_template('pages/Profesores.html')

@app.route('/estadisticas')
def estadisticas():
    return render_template('pages/Estadisiticas.html')

@app.route('/foros')
def foros():
    return render_template('pages/Foros.html')

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
