from dotenv import load_dotenv
from os import getenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = getenv("SECRET_KEY")
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

login_manager = LoginManager(app)
login_manager.login_view = "login"

from src.routes.meals import create