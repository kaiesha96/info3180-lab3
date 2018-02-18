from flask import Flask
from flask_mail import Mail

app = Flask(__name__)

app.config['SECRET_KEY'] = 'somerandompassphrase'
app.config['MAIL_SERVER'] = 'smtp.mailtrap.io'
app.config['MAIL_PORT'] = '2525'
app.config['MAIL_USERNAME'] = '4e8052b5ab5c9b'
app.config['MAIL_PASSWORD'] = '999ecd5d2559bd'

mail = Mail(app)
from app import views