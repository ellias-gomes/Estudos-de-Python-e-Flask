from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from models import db, Usuario

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask_user:flasksenha@localhost/flask_db'
db.init_app(app)

@app.route('/')
def home():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        # Coletar dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']
        telefone = request.form['telefone']
        # Validação básica de senha
        if len(senha) < 8:
            flash('🔒 A senha deve ter no mínimo 8 caracteres', 'error')
            return redirect(url_for('cadastro'))
        elif not any(c.isupper() for c in senha):
            flash('🔒 A senha deve conter pelo menos 1 letra maiúscula', 'error')
            return redirect(url_for('cadastro'))

        # Validação de telefone
        telefone = telefone.strip()  # Remove espaços
        if not telefone.isdigit():
            flash('📞 O telefone deve conter apenas números', 'error')
            return redirect(url_for('cadastro'))
        elif len(telefone) != 11:
            flash('📞 O telefone deve ter 11 dígitos (incluindo DDD)', 'error')
            return redirect(url_for('cadastro'))

        # Verificar se email já existe
        if Usuario.query.filter_by(email=email).first():
            flash('Este email já está cadastrado!', 'error')
            return redirect(url_for('cadastro'))

        # Criar novo usuário
        novo_usuario = Usuario(
            nome=nome,
            email=email,
            telefone=telefone
        )
        novo_usuario.senha = senha  # A propriedade setter vai gerar o hash

        try:
            db.session.add(novo_usuario)
            db.session.commit()
            flash('Cadastro realizado com sucesso! Faça login.', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash('Erro ao registrar: ' + str(e), 'error')

    return render_template('cadastro.html')

@app.route('/login')
def login():
    return "Página de login (a implementar)"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8080, debug=True)