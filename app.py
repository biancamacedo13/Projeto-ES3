from flask import Flask

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'

from routes import *

if __name__ == "__main__":
    app.run(port=5002)