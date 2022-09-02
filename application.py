import os

dir = os.getcwd()

from flask import Flask, render_template

app = Flask(import_name=__name__,
            static_folder=dir + r"\images")

@app.route("/")
def index():
    username = 'Thiago'
    return render_template('main.html', username=username)

if __name__ == "__main__":
    app.run()