import os
from flask import Flask, url_for, redirect, render_template

app = Flask(import_name=__name__,
            static_folder=os.getcwd() + r"\images")

username = 'Gustavo'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title = 'Gerenciador de eventos', username=username)

@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html', username=username)

@app.route("/registro", methods=['GET', 'POST'])
def registro():
    return render_template('registro.html', username=username)

@app.route("/create_event", methods=['GET', 'POST'])
def create_event():
    return render_template('create_event.html', username=username)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    return redirect(url_for('home'))

if __name__ == "__main__":
    app.run()