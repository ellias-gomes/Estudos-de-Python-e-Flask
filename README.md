# Estudos de Python e Flask

Repositório de estudos com exercícios de estruturas de dados, algoritmos em Python, interface gráfica com Tkinter e aplicações web iniciais utilizando Flask e SQLAlchemy.

## Estrutura do Projeto

```text
.
├── Codigos/                # Exercícios de busca, fila e pilha
│   ├── busca.py
│   ├── fila.py
│   └── pilha.py
├── flask/                  # Projetos web iniciais com Flask
│   ├── app.py              # Protótipo inicial com Flask e MySQL
│   ├── models.py           # Modelo Usuario com hash de senha
│   ├── sql.sql             # Script auxiliar de configuração do banco MySQL
│   ├── static/             # CSS e JS do protótipo inicial
│   ├── templates/          # Templates HTML (index, cadastro)
│   └── app_server/         # Versão estruturada com .env e login funcional
│       ├── app.py
│       ├── models.py
│       ├── static/
│       └── templates/
├── Fib_Mem.py              # Sequência de Fibonacci com memoização
├── Fila.py                 # Implementação de estrutura de Fila
├── Filas_Banco.py          # Simulação de atendimento em filas de banco
├── Gerador_Senhas.py       # Script gerador de senhas aleatórias
├── Pilha.py                # Implementação de estrutura de Pilha
└── sim.py                  # Interface gráfica simples com Tkinter
```

## Tecnologias e Dependências

- **Python 3**
- **Tkinter** (biblioteca padrão para GUI em `sim.py`)
- **Flask** e **Flask-SQLAlchemy**
- **PyMySQL** e **Werkzeug**
- **python-dotenv** (carregamento de variáveis de ambiente em `flask/app_server/`)
- **MySQL** (banco de dados utilizado nas aplicações Flask)

## Como Executar

### Scripts Python

Execute qualquer exercício diretamente com o Python:

```bash
python3 Fib_Mem.py
python3 Gerador_Senhas.py
python3 Filas_Banco.py
```

### Aplicação Flask (`flask/app_server`)

1. Instale as dependências necessárias:
   ```bash
   pip install flask flask-sqlalchemy pymysql python-dotenv
   ```
2. Configure o arquivo `.env` dentro de `flask/app_server/` com as variáveis de ambiente:
   ```env
   FLASK_SECRET_KEY=sua_chave_secreta
   DATABASE_URL=mysql+pymysql://usuario:senha@localhost/nome_do_banco
   ```
3. Inicie o servidor:
   ```bash
   cd flask/app_server
   python3 app.py
   ```
4. Acesse `http://localhost:8080` no navegador.
