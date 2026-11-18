from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Usuario
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db.init_app(app)

@app.route('/')
def home():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']

        if len(senha) < 8:
            flash('🔒 A senha deve ter no mínimo 8 caracteres', 'error')
            return redirect(url_for('cadastro'))
        elif not any(c.isupper() for c in senha):
            flash('🔒 A senha deve conter pelo menos 1 letra maiúscula', 'error')
            return redirect(url_for('cadastro'))
        
        telefone = telefone.strip()
        if not telefone.isdigit():
            flash('📞 O telefone deve conter apenas números', 'error')
            return redirect(url_for('cadastro'))
        elif len(telefone) != 11:
            flash('📞 O telefone deve ter 11 dígitos (incluindo DDD)', 'error')
            return redirect(url_for('cadastro'))
        
        if Usuario.query.filter_by(email=email).first():
            flash('Este email já está cadastrado!', 'error')
            return redirect(url_for('cadastro'))
        
        novo_usuario = Usuario(
            nome=nome,
            email=email,
            telefone=telefone
        )

        novo_usuario.senha = senha

        try:
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Cadastro realizado com sucesso! Faça login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Erro ao cadastrar usuário. Tente novamente.', 'error')

    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        senha = request.form['senha']

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario and usuario.verificar_senha(senha):
            flash('Login realizado com sucesso!', 'success')
            return redirect(url_for('home'))
        elif usuario:
            flash('Senha incorreta.', 'error')
            return redirect(url_for('login'))
        else:
            flash('Email ou senha inválidos.', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/testes')
def testes():
    return render_template('testes.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)