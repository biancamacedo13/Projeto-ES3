from main import app
from flask import render_template
#rotas

@app.route("/")
def login():
        return render_template("login.html")