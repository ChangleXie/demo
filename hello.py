from flask import Flask, render_template, session, url_for, flash, redirect
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required




app = Flask(__name__)
app.config.from_object('config')

# manager = Manager(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[Required()])
    submit = SubmitField('submit')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():  
    return render_template('index.html')

@app.route('/templates/cv.html/')
def cv():
    return render_template('cv.html')

if __name__ == '__main__':
    app.run(debug=True)
