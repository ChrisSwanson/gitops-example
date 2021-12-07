from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name="World"):
    return f'Hello, {name}!'

@app.route("/smile")
def smiles():
    return '😊'

@app.route('/health')
def health():
    return Response("👍", status=418)