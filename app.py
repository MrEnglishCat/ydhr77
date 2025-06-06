import json
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from environs import Env
import os

env = Env()
env.read_env('.env')
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = env.str('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = env.bool('SQLALCHEMY_TRACK_MODIFICATIONS')

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    json = db.Column(db.JSON)



# $("#header") — получение элемента с id=«header»
# $(«h3») — получить все <h3> элементы
# $(«div#content .photo») — получить все элементы с классом =«photo» которые находятся в элементе div с id=«content»
# $(«ul li») — получить все <li> элементы из списка <ul>
# $(«ul li:first») — получить только первый элемент <li> из списка <ul>

@app.template_filter('to_nice_json')
def to_nice_json(value):
    return json.dumps(value)


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        form_data = request.form.to_dict()
        new_entry = Form(json=form_data)
        db.session.add(new_entry)
        db.session.commit()
        return redirect(url_for('results', data=new_entry.json))


    return render_template("index.html")


@app.route("/results")
def results():
    data = Form.query.all()

    print(data)

    return render_template("results.html", data=data)



if __name__ == "__main__":
    app.run(debug=True)
