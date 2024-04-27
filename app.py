from flask import Flask, render_template, request
from random import randint

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    
    variavel = "Game: adivinhe o número."

    if request.method == "GET":
        return render_template("index.html", variavel=variavel)
    else:
        numero = randint(1, 2)
        palpite = int(request.form.get("name"))
            
        if numero == palpite:
            return '<h1>Você ganhou<h1>'
            
        else:
            return '<h1>Você perdeu</h1>'
    
@app.route('/<string:nome>')
def erro404(nome):
    variavel = f'<h1>Olá, a pagína: {nome} que você tentou acessar não existe</h1>'
    return render_template('error.html', variavel=variavel)

if __name__ == '__main__':
    app.run()