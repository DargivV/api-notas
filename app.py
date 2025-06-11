from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os


app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://sql3784159:KAFJiwhDdL@sql3.freesqldatabase.com:3306/sql3784159' #esta vaina tiene una estructura , no me acuerdo cual 

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
 

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    apellidoP = db.Column(db.String(100))
    apellidoM = db.Column(db.String(100))


class Curso(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_curso = db.Column(db.String(100))
    ciclo = db.Column(db.String(50))
    creditos = db.Column(db.Float)


class Unidad(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre_unidad = db.Column(db.String(100))
    id_curso = db.Column(db.Integer, db.ForeignKey('curso.id'))


class TipoNota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))  # INV, PC, EP, etc.


class Nota(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    id_unidad = db.Column(db.Integer, db.ForeignKey('unidad.id'))
    id_tipo_nota = db.Column(db.Integer, db.ForeignKey('tipo_nota.id'))
    valor = db.Column(db.Float)
    peso = db.Column(db.Float)

# =====================
# RUTAS
# =====================

@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    usuario = Usuario(**data)
    db.session.add(usuario)
    db.session.commit()
    return jsonify({"mensaje": "Usuario creado"})


@app.route('/cursos', methods=['POST'])
def crear_curso():
    data = request.json
    curso = Curso(**data)
    db.session.add(curso)
    db.session.commit()
    return jsonify({"mensaje": "Curso creado"})


@app.route('/unidades', methods=['POST'])
def crear_unidad():
    data = request.json
    unidad = Unidad(**data)
    db.session.add(unidad)
    db.session.commit()
    return jsonify({"mensaje": "Unidad creada"})


@app.route('/tiponotas', methods=['POST'])
def crear_tipo_nota():
    data = request.json
    tipo = TipoNota(**data)
    db.session.add(tipo)
    db.session.commit()
    return jsonify({"mensaje": "Tipo de nota creado"})


@app.route('/notas', methods=['POST'])
def registrar_nota():
    data = request.json
    nota = Nota(**data)
    db.session.add(nota)
    db.session.commit()
    return jsonify({"mensaje": "Nota registrada"})

@app.route('/')
def index():
    return 'API de Notas activa desde Render 🎉'



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
