from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    todo_item = StringField('todo_item', validators=[DataRequired()])
    submit_button = SubmitField('Add item')

app = Flask(__name__)
# in a real app, these should be configured through Flask-Appconfig
app.config['SECRET_KEY'] = 'devkey'

Bootstrap(app)

@app.route('/')
def hello():
    form = TodoForm()
    return render_template("index.html", form=form)

if __name__ == "__main__":
	app.run(debug=True)
