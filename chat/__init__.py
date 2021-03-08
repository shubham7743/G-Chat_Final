from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.static_folder = 'static'
app.config['SECRET_KEY'] = '0ca5e3a1c2dc3391f9a2bb9c54a532a3'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from chat import routes
