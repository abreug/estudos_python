from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://blog.sqlite3"

class Post(db.Model):       #modelo do banco de dados com tabela post
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    author = db.Column(db.String())


@app.route("/")
def home():
    nome = request.args.get("nome")
    return render_template("index.html", username=nome)

db.create_all()
app.run(debug=True)