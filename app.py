from flask import Flask
from flask import render_template

app = Flask(__name__)

users = [
    {"id": 1, "nome": "João Silva", "email": "joao@email.com", "perfil": "admin", "status": "ativo"},
    {"id": 2, "nome": "Maria Souza", "email": "maria@email.com", "perfil": "professor", "status": "ativo"},
    {"id": 3, "nome": "Carlos Lima", "email": "carlos@email.com", "perfil": "aluno", "status": "inativo"},
    {"id": 4, "nome": "Ana Paula", "email": "ana@email.com", "perfil": "aluno", "status": "ativo"},
    {"id": 5, "nome": "Pedro Santos", "email": "pedro@email.com", "perfil": "professor", "status": "ativo"},
    {"id": 6, "nome": "Juliana Alves", "email": "juliana@email.com", "perfil": "admin", "status": "ativo"},
    {"id": 7, "nome": "Fernanda Costa", "email": "fernanda@email.com", "perfil": "aluno", "status": "inativo"},
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def lista_users():
    return render_template("users.html", users=users)