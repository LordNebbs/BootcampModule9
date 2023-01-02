from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello World"

#skilldrill create a simple route 
@app.route('/GreenTea')
def tuna():
    return '<h2>Arizona Green Tea is my favorite drink<h2>'