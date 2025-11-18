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
    
     # Método para obtener un usuario por su id
    @classmethod
    def get_by_id(cls,id):
        query = "select * from usuario where id = %(id)s"
        data = {'id':id}
        resultado = connectToMySQL('personas').query_db(query,data)
        if resultado:
            return cls(resultado[0])
        return None
    #Método para eliminar datos
    @classmethod
    def delete(cls, id):
        query = "delete from usuario where id = %(id)s"
        data = {'id':id}
        result = connectToMySQL('personas').query_db(query, data)
        print(result)
        if result:
            return {"status": "success", "message": "Usuario eliminado con éxito."}
        else:
            return {"status": "error", "message": "No se encontró el usuario o no se pudo eliminar."}
        
    @classmethod
    def update(cls, data):
        query = "update usuario set nombre = %(nombre)s, apellido = %(apellido)s, edad = %(edad)s, fecha_nacimiento =  %(fecha_nacimiento)s where id = %(id)s"
        result = connectToMySQL('personas').query_db(query, data)
        if result:
            return {"status": "success", "message": "Usuario actualizado con éxito."}
        else:
            return {"status": "error", "message": "Usuario no encontrado."}