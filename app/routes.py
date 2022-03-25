from flask import Request, render_template, request
from app import app, db
from app.models.usuario import Usuario
from app.models.despesas import Despesas
from app.models.receitas import Receitas

@app.route('/')
@app.route('/index')
def index():

    usuario = {"nome": "", "sobrenome": ""}

    return render_template('index.html', usuario = usuario, titulo = 'Página inicial')

@app.route('/contato')
def contato():
    return render_template('contato.html', titulo='DIGIF - contato')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html', titulo='DIGIF - cadastro')

@app.route('/cadastro_de_despesas')
def cadastro_de_despesas():
    return render_template('cadastro_de_despesas.html', titulo='DIGIF - cadastro_de_despesas')

    @app.route('/cadastro_de_receitas')
    def cadastro_de_receitas():
        return render_template('cadastro_de_receitas.html', titulo='DIGIF - cadastro_de_receitas')
    
@app.route('/login')
def login():
    return render_template('login.html', titulo='DIGIF - login')

@app.route('/sobre')
def sobre():
    return render_template('sobre.html', titulo='DIGIF - sobre')


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    nome=request.form['nome']
    email=request.form['email']
    senha=request.form['senha']
    user = Usuario(nome, email, senha)
    db.session.add(user)
    db.session.commit()

    return "Dados inseridos com sucesso"

@app.route('/cadastro_de_despesas', methods=['POST'])
def cadastrar_despesas():
    valor=request.form['valor']
    descricao=request.form['descricao']
    data=request.form['data']
    despesa = Despesas(valor, descricao, data)
    db.session.add(despesa)
    db.session.commit()

    return "Dados inseridos com sucesso"


    @app.route('/cadastro_de_receitas', methods=['POST'])
    def cadastrar_receitas():
     valor=request.form['valor']
    descricao=request.form['descricao']
    data=request.form['data']
    receita = receitass(valor, descricao, data)
    db.session.add(receita)
    db.session.commit()

    return "Dados inseridos com sucesso"

@app.route('/autenticar')
def autenticar():
    return render_template('autenticar.html', titulo='DIGIF - autenticar')

def teste():
    u = Usuario.query.all()

    print(u)
    u = Usuario.query.get(1)

    return u.nome

def teste():
    u = Usuario.query.get(1)
    u.nome = "Anna Cristina"
    db.session.add(u)
    db.session.commit()

def teste():
    u = Usuario.query.get(1)
    db.session.delete(u)
    db.session.commit()