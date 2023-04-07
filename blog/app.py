from flask import Flask

app = Flask(__name__)

@app.route('/great/<name>/')
def index(name):
    return f'Start page. Hello, {name}'