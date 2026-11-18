from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    cod_usuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha_hash = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    # Propriedade para evitar acesso direto à senha bruta
    @property
    def senha(self):
        raise AttributeError('Senha não é um atributo legível.')
    
    # Gera o hash da senha quando ela é definida
    @senha.setter
    def senha(self, senha):
        self.senha_hash = generate_password_hash(senha)

    # Verifica se a senha fornecida corresponde ao hash armazenado
    def verificar_senha(self, senha):
        return check_password_hash(self.senha_hash, senha)