import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

load_dotenv('.env')
db = SQLAlchemy()
app = Flask(__name__)

host = os.environ.get('CICD_SALES_DB_HOST')   
port = os.environ.get('CICD_SALES_DB_PORT')
db_name = os.environ.get('CICD_SALES_DB_NAME')
user = os.environ.get('CICD_SALES_DB_USER')
password = os.environ.get('CICD_SALES_DB_PASS')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'

db.init_app(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String)

    def __repr__(self):
        return f'<user_id={self.id}; user first name {self.first_name}; user last name {self.last_name}'
@app.route('/')
def hello_world():
    user = db.get_or_404(User,1)   
    return f"Hello world from {user.first_name}"
