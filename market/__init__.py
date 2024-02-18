from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '03defa46bf740bdbe81d7601'
db = SQLAlchemy(app)  # to pass our application instance to SQLAlchemy
from market import routes
