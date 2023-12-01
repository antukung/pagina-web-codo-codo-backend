from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend


# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/proyecto'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow


# defino la tabla
class Libro(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    link_descarga=db.Column(db.String(400))
    grupo=db.Column(db.String(400))
    imagen=db.Column(db.String(400))
    def __init__(self,nombre,link_descarga,grupo,imagen):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.link_descarga=link_descarga
        self.grupo=grupo
        self.imagen=imagen





    #  si hay que crear mas tablas , se hace aqui




with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class LibroSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','link_descarga','grupo','imagen')




libro_schema=LibroSchema()            # El objeto libro_schema es para traer un producto
libros_schema=LibroSchema(many=True)  # El objeto libros_schema es para traer multiples registros de producto




# crea los endpoint o rutas (json)
@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Libro.query.all()         # el metodo query.all() lo hereda de db.Model
    result=libros_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Libro.query.get(id)
    return libro_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro




@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Libro.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return libro_schema.jsonify(producto)   # me devuelve un json con el registro eliminado


@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    link_descarga=request.json['link_descarga']
    grupo=request.json['grupo']
    imagen=request.json['imagen']
    new_producto=Libro(nombre,link_descarga,grupo,imagen)
    db.session.add(new_producto)
    db.session.commit()
    return libro_schema.jsonify(new_producto)


@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Libro.query.get(id)
 
    nombre=request.json['nombre']
    link_descarga=request.json['link_descarga']
    grupo=request.json['grupo']
    imagen=request.json['imagen']


    producto.nombre=nombre
    producto.link_descarga=link_descarga
    producto.grupo=grupo
    producto.imagen=imagen


    db.session.commit()
    return libro_schema.jsonify(producto)
 


# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000from flask import Flask ,jsonify ,request
# del modulo flask importar la clase Flask y los métodos jsonify,request
from flask_cors import CORS       # del modulo flask_cors importar CORS
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
app=Flask(__name__)  # crear el objeto app de la clase Flask
CORS(app) #modulo cors es para que me permita acceder desde el frontend al backend


# configuro la base de datos, con el nombre el usuario y la clave
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:root@localhost/proyecto'
# URI de la BBDD                          driver de la BD  user:clave@URLBBDD/nombreBBDD
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False #none
db= SQLAlchemy(app)   #crea el objeto db de la clase SQLAlquemy
ma=Marshmallow(app)   #crea el objeto ma de de la clase Marshmallow


# defino la tabla
class Libro(db.Model):   # la clase Producto hereda de db.Model    
    id=db.Column(db.Integer, primary_key=True)   #define los campos de la tabla
    nombre=db.Column(db.String(100))
    link_descarga=db.Column(db.String(400))
    grupo=db.Column(db.String(400))
    imagen=db.Column(db.String(400))
    def __init__(self,nombre,link_descarga,grupo,imagen):   #crea el  constructor de la clase
        self.nombre=nombre   # no hace falta el id porque lo crea sola mysql por ser auto_incremento
        self.link_descarga=link_descarga
        self.grupo=grupo
        self.imagen=imagen





    #  si hay que crear mas tablas , se hace aqui




with app.app_context():
    db.create_all()  # aqui crea todas las tablas
#  ************************************************************
class LibroSchema(ma.Schema):
    class Meta:
        fields=('id','nombre','link_descarga','grupo','imagen')




libro_schema=LibroSchema()            # El objeto libro_schema es para traer un producto
libros_schema=LibroSchema(many=True)  # El objeto libros_schema es para traer multiples registros de producto




# crea los endpoint o rutas (json)
@app.route('/productos',methods=['GET'])
def get_Productos():
    all_productos=Libro.query.all()         # el metodo query.all() lo hereda de db.Model
    result=libros_schema.dump(all_productos)  # el metodo dump() lo hereda de ma.schema y
                                                 # trae todos los registros de la tabla
    return jsonify(result)                       # retorna un JSON de todos los registros de la tabla




@app.route('/productos/<id>',methods=['GET'])
def get_producto(id):
    producto=Libro.query.get(id)
    return libro_schema.jsonify(producto)   # retorna el JSON de un producto recibido como parametro




@app.route('/productos/<id>',methods=['DELETE'])
def delete_producto(id):
    producto=Libro.query.get(id)
    db.session.delete(producto)
    db.session.commit()
    return libro_schema.jsonify(producto)   # me devuelve un json con el registro eliminado


@app.route('/productos', methods=['POST']) # crea ruta o endpoint
def create_producto():
    #print(request.json)  # request.json contiene el json que envio el cliente
    nombre=request.json['nombre']
    link_descarga=request.json['link_descarga']
    grupo=request.json['grupo']
    imagen=request.json['imagen']
    new_producto=Libro(nombre,link_descarga,grupo,imagen)
    db.session.add(new_producto)
    db.session.commit()
    return libro_schema.jsonify(new_producto)


@app.route('/productos/<id>' ,methods=['PUT'])
def update_producto(id):
    producto=Libro.query.get(id)
 
    nombre=request.json['nombre']
    link_descarga=request.json['link_descarga']
    grupo=request.json['grupo']
    imagen=request.json['imagen']


    producto.nombre=nombre
    producto.link_descarga=link_descarga
    producto.grupo=grupo
    producto.imagen=imagen


    db.session.commit()
    return libro_schema.jsonify(producto)
 


# programa principal *******************************
if __name__=='__main__':  
    app.run(debug=True, port=5000)    # ejecuta el servidor Flask en el puerto 5000