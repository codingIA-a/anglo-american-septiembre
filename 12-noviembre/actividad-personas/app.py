from flask import Flask, render_template, request, redirect, url_for
from usuario import Usuario
from mysqlconnection import connectToMySQL

app = Flask(__name__)

@app.route('/')
def index():
    usuarios = Usuario.get_all()
    return render_template('index.html', usuarios=usuarios)

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/insertar_usuario', methods=['POST'])
def insertar_usuario():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    fecha_nacimiento = request.form['fecha_nacimiento']

    data = {
        'nombre' : nombre,
        'apellido': apellido,
        'edad': edad,
        'fecha_nacimiento' : fecha_nacimiento
    }
    resultado = Usuario.create(data)

    if resultado:
        return redirect(url_for("index"))
    else:
        return "Error!!!!!!!!!!"



if __name__ == '__main__':
    app.run(debug=True)