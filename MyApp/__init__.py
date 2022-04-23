from flask import Flask ,render_template,url_for,flash,session,request,redirect 

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import column,String,Integer,ForeignKey,table,DateTime


app = Flask(__name__)
app.secret_key = '5bfef38cecca6314b07863d3cbd93a790291f6161468bf6364d9bfd680eb301c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///batabase.db'

db = SQLAlchemy(app)


from MyApp.admin import route