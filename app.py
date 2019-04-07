from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class TodoForm(FlaskForm):
    todo_item = StringField('TODO', validators=[DataRequired()])
    submit_button = SubmitField('Add item')

app = Flask(__name__)
# in a real app, these should be configured through Flask-Appconfig
app.config['SECRET_KEY'] = 'devkey'

Bootstrap(app)

@app.route('/', methods = ["GET", "POST"])
def hello():
    form = TodoForm()
    submitted_item = "<No item submitted>"
    if form.validate_on_submit():
        submitted_item = form.todo_item.data
        
    return render_template("index.html", form=form, submitted_item=submitted_item)

if __name__ == "__main__":
	app.run(debug=True)
