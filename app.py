from flask import Flask, render_template, redirect, request # Importação das bibliotecas
from db import DB # Importação das bibliotecas

app = Flask(__name__) # Criação de uma instância do FLASK
db = DB() # Criação de uma instância da Classe do db.py

@app.route("/") # Criando rota padrão de acesso
def Home():
    contatos = db.pesquisartodos()
    return render_template("home.html", contatos=contatos) # Retornando HTML de login

@app.route("/adicionar") # Criando rota para renderizar o HTML de adição de novos contatos
def adicionar():
    return render_template("adicionar.html") # Retornando HTML de Adição de contatos


@app.route("/adicionando", methods=['POST']) # Criando rota para executar as funções de adição do banco de dados.
def Adicionando():
    numero = request.form["numero"]
    nome = request.form["nome"]
    cidade = request.form["cidade"]
        
    db.adicionar(nome,numero,cidade)
    return redirect("/") # Retorna um redirecionamento para a rota padrão

@app.route("/remover/<int:id>") # Criação de rota para remover um contato da lista baseando-se no ID.
def remover(id):
    db.remover(id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)