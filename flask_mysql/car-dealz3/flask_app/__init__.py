from flask import  Flask
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "root"
DATABASE="car_dealz2"

bcrypt = Bcrypt(app) 