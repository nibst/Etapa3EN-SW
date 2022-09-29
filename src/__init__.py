import os
from flask import Flask
from flask_login import LoginManager


app = Flask(import_name=__name__,
            static_folder=os.getcwd() + r"\src\images")
            
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
login_manager = LoginManager(app)
from src import routes