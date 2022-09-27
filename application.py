import os
from flask import Flask, render_template

app = Flask(import_name=__name__,
            static_folder=os.getcwd() + r"\images")

username = 'Gustavo'

@app.route("/")
@app.route("/home")
def index():
    return render_template('index.html', title = 'Gerenciador de eventos', username=username)

@app.route("/login")
def login():
    return render_template('login.html', username=username)

@app.route("/registro")
def registro():
    return render_template('registro.html', username=username)

@app.route("/create_event")
def create_event():
    return render_template('create_event.html', username=username)

if __name__ == "__main__":
    app.run()