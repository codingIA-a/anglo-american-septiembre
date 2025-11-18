from flask import Flask, render_template, request, redirect, url_for, flash
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
##############
@app.route('/usuario/<int:id>')
def ver_usuario(id):
    usuario = Usuario.get_by_id(id)

    if usuario:
        return render_template('ver_usuario.html', usuario=usuario)
    else:
        return redirect(url_for('index'))

#####
@app.route('/eliminar_usuario/<int:id>', methods=['POST'])
def eliminar_usuario(id):
    resultado = Usuario.delete(id)
    print(resultado)
    if resultado:
        return redirect(url_for('index'))
    else:
        return "Error!!!!"
#############
@app.route('/actualizar/<int:id>', methods=['GET'])
def mostrar_formulario(id):
    usuario = Usuario.get_by_id(id)
    if usuario:
        return render_template('actualizar.html', usuario=usuario)
    
######
@app.route('/actualizar_usuario/<int:id>', methods=['POST'])
def actualizar_data(id):
    data = {
        'id': id,
        'nombre': request.form['nombre'],
        'apellido':request.form['apellido'],
        'edad': request.form['edad'],
        'fecha_nacimiento': request.form['fecha_nacimiento']
    }
    usuario = Usuario.update(data)
    print(usuario)
    if usuario:
        return redirect(url_for('ver_usuario', id=id))
    
if __name__ == '__main__':
    app.run(debug=True)