from mysqlconnection import connectToMySQL

class Usuario:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.fecha_nacimiento = data['fecha_nacimiento']
        self.created_at = data['created_at']
        self.updated_data = data['updated_at'] 

    @classmethod
    def get_all(cls):
        query = "select * from usuario;"
        resultados = connectToMySQL('personas').query_db(query)

        usuarios = []
        for i in resultados:
            usuarios.append(cls(i))
        return usuarios
    @classmethod
    def create(cls, data):
        query = "insert into usuario (nombre, apellido, edad, fecha_nacimiento) values ( %(nombre)s, %(apellido)s, %(edad)s, %(fecha_nacimiento)s );"
        return connectToMySQL('personas').query_db(query, data)